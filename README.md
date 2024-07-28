## NBA Odds Scraping

This repository contains three Python scripts for scraping NBA odds and match data from OddsPortal. The scripts use Selenium for web automation and BeautifulSoup for HTML parsing. They target different sets of data, including upcoming matches, and results from the 2022-2023 and 2023-2024 seasons.

## Prerequisites

Before running any of the scripts, ensure you have the following installed:

- Python 3.x
- Selenium
- BeautifulSoup
- chromedriver_autoinstaller
- pandas

## Scripts
1. upcoming_nba_matches.py

This script scrapes the odds of upcoming NBA matches.

## Functionality:

- Opens the OddsPortal NBA page for upcoming matches.
- Scrolls to the bottom of the page to load all content.
- Extracts the date, team names, and odds.
- Saves the data to upcoming_nba_matches.csv.

2. nba_2022_2023_results.py

This script scrapes NBA match results and odds for the 2022-2023 season.

## Functionality:

- Opens the OddsPortal NBA results page for the 2022-2023 season.
- Scrolls to the bottom of the page to load all content.
- Clicks through pagination to load additional results.
- Extracts the date, team names, scores, and odds.
- Saves the data to nba_2022_2023_results.csv.

3. nba_2023_2024_results.py

This script scrapes NBA match results and odds for the 2023-2024 season.

## Functionality:

- Opens the OddsPortal NBA results page for the 2022-2023 season.
- Scrolls to the bottom of the page to load all content.
- Clicks through pagination to load additional results.
- Extracts the date, team names, scores, and odds.
- Saves the data to nba_2023_2024_results.csv.
