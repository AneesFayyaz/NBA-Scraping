from selenium import webdriver
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
url = "https://www.oddsportal.com/basketball/usa/nba-2022-2023/results/"
driver.get(url)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
time.sleep(30)

def scroll_to_bottom():
    while True:
        current_height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
        driver.execute_script(f"window.scrollTo(0, {current_height});")
        time.sleep(2)
        new_height = driver.execute_script("return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);")
        if new_height == current_height:
            break
def scroll_to_top():
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
def click_next_page():
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@class='pagination-link' and contains(text(), 'Next')]")))
        driver.execute_script("arguments[0].scrollIntoView();", next_button)
        time.sleep(1)
        driver.execute_script("arguments[0].click();", next_button)
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "eventRow")))

        return True
    except Exception as e:
        print("Pagination Ended")
        return False
date=[]
team=[]
opposition=[]
team_score=[]
opp_score=[]
team_odd=[]
opposition_odd=[]
bs=[]
ot_list=[]

page_number = 0
while True:
    print(f"Scraping Page {page_number}")
    event_rows = soup.find_all("div", class_="eventRow flex w-full flex-col text-xs")
    current_date = None
    for event_row in event_rows:
        date_element = event_row.find("div", class_="text-black-main font-main w-full truncate text-xs font-normal leading-5")
        if date_element:
            current_date = date_element.text.strip()
        match_info = event_row.find("a", class_="justify-content min-mt:!gap-2 flex basis-[50%] cursor-pointer items-center gap-1 overflow-hidden")
        if match_info:
            match_title = match_info.get('title', '')
        match_info1 = event_row.find("a", class_="min-mt:!justify-end flex basis-[50%] cursor-pointer items-start justify-start gap-1 overflow-hidden")
        if match_info1:
            match_title2 = match_info1.get('title', '')
        divs = event_row.find_all("div", class_="next-m:min-w-[80%] next-m:min-h-[26px] next-m:max-h-[26px] flex cursor-pointer items-center justify-center font-bold hover:border hover:border-orange-main min-w-[50px] min-h-[50px]")
        if divs:
            team_odds = divs[0].find("p").text.strip() if len(divs) >= 1 else 'N/A'
            opp_odds = divs[1].find("p").text.strip() if len(divs) >= 2 else 'N/A'
        else:
            team_odd, opp_odd = 'N/A', 'N/A'
        Bs = event_row.find("div", class_="height-content text-black-main text-[10px] leading-5").text.strip()
        


        scores_div=event_row.find("div", class_="flex gap-1 font-bold font-bold")
        i=0
        n=scores_div.text
        m=n.split('–')
        score1,score2=m        
        
        ot = event_row.find("p", class_="min-mt:hidden mr-1")
        ot_data = ot.text.strip() if ot else 'NULL'

        date.append(current_date)
        team.append(match_title2)
        opposition.append(match_title)
        team_odd.append(team_odds)
        opposition_odd.append(opp_odds)
        bs.append(Bs)
        ot_list.append(ot_data)
        team_score.append(score1)
        opp_score.append(score2)

    if not click_next_page():
        print('NEXT ADDED')
        break
    page_number += 1    
    page_source_after_scroll = driver.page_source
    soup = BeautifulSoup(page_source_after_scroll, 'html.parser')
    scroll_to_top()
    time.sleep(10)
driver.quit()

df = pd.DataFrame({
    'Date': date,
    'Team': team,
    'Opposition': opposition,
    'Team Score':team_score,
    'Opposition Score':opp_score,
    'OT':ot_list,
    'Team Odd': team_odd,
    'Opposition Odd': opposition_odd,
    'Bs': bs
    
})

print(df)
df.to_csv('output_file.csv', index=False)