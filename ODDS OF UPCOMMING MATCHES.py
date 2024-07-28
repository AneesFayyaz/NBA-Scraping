from selenium import webdriver
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
import time
import pandas as pd

chromedriver_autoinstaller.install()
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
url = "https://www.oddsportal.com/basketball/usa/nba/"
driver.get(url)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')
time.sleep(30)
def scroll_to_bottom():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)
def scroll_to_top():
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(2)
scroll_to_bottom()
page_source_after_bottom_scroll = driver.page_source
soup = BeautifulSoup(page_source_after_bottom_scroll, 'html.parser')
scroll_to_top()
page_source_after_top_scroll = driver.page_source
soup = BeautifulSoup(page_source_after_top_scroll, 'html.parser')



date=[]
team=[]
opposition=[]
team_odd=[]
opposition_odd=[]
bs=[]




event_rows = soup.find_all("div", class_="eventRow flex w-full flex-col text-xs")
current_date = None
driver.quit()
for event_row in event_rows:
    date_element = event_row.find("div", class_="text-black-main font-main w-full truncate text-xs font-normal leading-5")  # Replace with the actual class or tag name
    if date_element:
        current_date = date_element.text.strip()
        
    match_info = event_row.find("a", class_="justify-content min-mt:!gap-2 flex basis-[50%] cursor-pointer items-center gap-1 overflow-hidden")
    if match_info:
        match_title = match_info.get('title', '')
    match_info1 = event_row.find("a", class_="min-mt:!justify-end flex basis-[50%] cursor-pointer items-start justify-start gap-1 overflow-hidden")
    if match_info1:
        match_title2 = match_info1.get('title', '')

    divs = event_row.find_all("div", class_="next-m:min-w-[80%] next-m:min-h-[26px] next-m:max-h-[26px] flex cursor-pointer items-center justify-center font-bold hover:border hover:border-orange-main min-w-[50px] min-h-[50px]")  # Replace with the actual class or tag name
    if divs:
        team_odds = divs[0].find("p").text.strip() if len(divs) >= 1 else 'N/A'
        opp_odds = divs[1].find("p").text.strip() if len(divs) >= 2 else 'N/A'
    else:
        team_odd, opp_odd = 'N/A', 'N/A'
        

    Bs = event_row.find("div", class_="height-content text-black-main text-[10px] leading-5").text.strip()


        
        
        
        
        
        
        
#     print(f"Date: {current_date}, Match: {match_title2}, vs {match_title} ,teamodd {team_odds}, opposition_odd {opp_odds} , BS {Bs}")
    
    
    
    
    
    
    date.append(current_date)
    team.append(match_title2)
    opposition.append(match_title)
    team_odd.append(team_odds)
    opposition_odd.append(opp_odds)
    bs.append(Bs)


df = pd.DataFrame({
    'Date': date,
    'Team': team,
    'Opposition': opposition,
    'Team Odds': team_odd,
    'Opposition Odds': opposition_odd,
    
})

print(df)
df.to_csv('output_file.csv', index=False)