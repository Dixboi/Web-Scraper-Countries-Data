import requests #pip install requests
from bs4 import BeautifulSoup #pip install beautifulsoup4
import webScraperModule as wsm

if __name__ == "__main__":
  
  link = 'https://scrapethissite.com/pages/simple/'
  page = requests.get(link)
  soup = BeautifulSoup(page.content, 'html.parser')

  all_names = soup.find_all(class_ = 'country-name')
  all_capitals = soup.find_all(class_ = 'country-capital')
  all_populations = soup.find_all(class_ = 'country-population')
  all_areas = soup.find_all(class_ = 'country-area')

  wsm.instructions()
  user = "Python:\wsm\command>"
  
  while True:
    command = input(user).split()
    if len(command) > 0:
      if command[0] == "//term":
        wsm.exitProgram()
      elif command[0] != "//term":
        try:
          if command[0] == "//a":
            wsm.displayAllInfos(all_names, all_capitals, all_populations, all_areas)
          elif command[0] == "//gen": 
            wsm.findSpecificInfoGENERAL(command[1], all_names, all_capitals, all_populations, all_areas)
          elif command[0] == "//co":
            wsm.findSpecificInfoNAMES(command[1], all_names, all_capitals, all_populations, all_areas)
          elif command[0] == "//ca":
            wsm.findSpecificInfoCAPITALS(command[1], all_names, all_capitals, all_populations, all_areas)
          elif command[0] == "//pop":
            wsm.findSpecificInfoPOPULATIONS(command[1], command[2], all_names, all_capitals, all_populations, all_areas)
          elif command[0] == "//ar":
            wsm.findSpecificInfoAREAS(command[1], command[2], all_names, all_capitals, all_populations, all_areas)
          elif command[0] == "//clear":
            wsm.clearScreen()
          elif command[0] == "//hlp":
            wsm.instructions()
          else:
            command = " ".join(command)
            print(f'"{command}" is not recognized as a valid command in this program.')
        except:
          print("Invalid entry.")
      else:
        print(f'"{command}" is not recognized as a valid command in this program.')
