import webScraperModule as wsm
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
  
  link = 'https://scrapethissite.com/pages/simple/'
  page = requests.get(link)
  soup = BeautifulSoup(page.content, 'html.parser')

  all_names = soup.find_all(class_ = 'country-name')
  all_capitals = soup.find_all(class_ = 'country-capital')
  all_populations = soup.find_all(class_ = 'country-population')
  all_areas = soup.find_all(class_ = 'country-area')

