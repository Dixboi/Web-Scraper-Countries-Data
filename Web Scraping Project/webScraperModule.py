import re
import os
import sys

def instructions():
  print('''

  Data of countries from https://scrapethissite.com/pages/simple/
  
  I N S T R U C T I O N S
  
  //a --> to display all information
  //gen + (country name) --> to display a country's information
                         Example: "//gen Philippines"
                         Will display information about Philippines
  //co + (starting letter/s) --> to display a country's name information starting with that letter/s
                         Exaple: "//co P"
                         Will display information about all countries starting with letter 'P'
  //ca + (starting letter/s) --> to display a country's capital information starting with that letter/s
                         Example: "//ca P"
                         Will display information about all capitals starting with letter 'P'
  //pop + (starting number) + (ending number) --> to display a country's population information
                                                  based on that range
                                            Example: "//pop 1000 2000"
                                            Will display information about all population within that range
  //ar + (starting number) + (ending number) --> to display a country's area information
                                                 based on that range
                                            Example: "//ar 1000 2000"
                                            Will display information about all area within that range
  //clear --> to clear screen
  //term --> to exit program
  //hlp --> to display instructions
  ''')

def allNames(countryNames):
  return [name.get_text().replace("  ", "").replace("\n", "") for name in countryNames]

def allCapitals(countryCapitals):
  return [capital.get_text() for capital in countryCapitals]

def allPopulations(countryPopulations):
  return [population.get_text() for population in countryPopulations]

def allAreas(countryAreas):
  return [area.get_text() for area in countryAreas]

def HEADER():
  print("#################################################################################################################################")
  print("# NAME                          # CAPITAL                       # POPULATION                              # AREA (km^2)         #")
  print("#################################################################################################################################")

def FOOTER():
  print("#################################################################################################################################")

def DISPLAY(country_name, country_capital, country_population, country_area):
  length = 30
  name = "# " + country_name + (" " * (length - len(country_name)) + "#")
  capital = country_capital + (" " * (length - len(country_capital)) + "#")
  population = str(country_population) + (" " * (length - len(str(country_population))) + "#")
  area = str(country_area) + (" " * (length - len(str(country_area))) + "#")
  print(name, capital, population, area)
  

def displayAllInfos(countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = allAreas(countryAreas)
  counter = 0
  HEADER()
  for info in range(len(Names)):
    DISPLAY(Names[counter], Capitals[counter], Populations[counter], Areas[counter])
    counter += 1
  FOOTER()

def findSpecificInfoGENERAL(findName, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = allAreas(countryAreas)
  position = Names.index(findName)
  HEADER()
  DISPLAY(Names[position], Capitals[position], Populations[position], Areas[position])
  FOOTER()

def findSpecificInfoNAMES(key, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = allAreas(countryAreas)
  pattern = "^{}".format(key)
  HEADER()
  for NAME in Names:
    searching = re.search(pattern, NAME)
    if searching:
      position = Names.index(NAME)
      DISPLAY(Names[position], Capitals[position], Populations[position], Areas[position])
  FOOTER()
     
  
def findSpecificInfoCAPITALS(key, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = allAreas(countryAreas)
  pattern = "^{}".format(key)
  HEADER()
  for CAPITAL in Capitals:
    searching = re.search(pattern, CAPITAL)
    if searching:
      position = Capitals.index(CAPITAL)
      DISPLAY(Names[position], Capitals[position], Populations[position], Areas[position])
  FOOTER()

def findSpecificInfoPOPULATIONS(startRange, endRange, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = list(map(lambda value: int(value), allPopulations(countryPopulations)))
  Areas = allAreas(countryAreas)
  HEADER()
  startRange = int(startRange)
  endRange = int(endRange)
  length = 30
  for POPULATION in Populations:
    if startRange <= POPULATION <= endRange:
      position = Populations.index(POPULATION)
      DISPLAY(Names[position], Capitals[position], Populations[position], Areas[position])
  FOOTER()
      
def findSpecificInfoAREAS(startRange, endRange, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = list(map(lambda value: float(value), allAreas(countryAreas)))
  HEADER()
  startRange = int(startRange)
  endRange = int(endRange)
  for AREAS in Areas:
    if startRange <= AREAS <= endRange:
      position = Areas.index(AREAS)
      DISPLAY(Names[position], Capitals[position], Populations[position], Areas[position])
  FOOTER()

def clearScreen():
  print("\n" * 40)
  os.system('cls')
  instructions()

def exitProgram():
  print("Are you sure you want to exit the program?")
  print("Type 'y' for yes, Press 'Enter' for no")
  isQuit = input()
  if isQuit == "y":
    sys.exit("Quitting program")
