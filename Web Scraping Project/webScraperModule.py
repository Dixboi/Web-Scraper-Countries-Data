import re
import os
import sys

def instructions():
  print('''
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
  //help --> to display instructions
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
  print("#########################################################################################")
  print("# NAME                # CAPITAL             # POPULATION          # AREA (km^2)         #")
  print("#########################################################################################")

def FOOTER():
  print("#########################################################################################")

def displayAllInfos(countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = allAreas(countryAreas)
  counter = 0
  HEADER()
  length = 20
  for info in range(len(Names)):
    if len(Names[counter]) < length:
      Names[counter] = "# " + Names[counter] + (" " * (length - len(Names[counter])) + "#")
      Capitals[counter] = Capitals[counter] + (" " * (length - len(Capitals[counter])) + "#")
      Populations[counter] = Populations[counter] + (" " * (length - len(Populations[counter])) + "#")
      Areas[counter] = Areas[counter] + (" " * (length - len(Areas[counter])))
      print(Names[counter], Capitals[counter], Populations[counter], Areas[counter] + "#")
    counter += 1
  FOOTER()

def findSpecificInfoGENERAL(findName, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = allAreas(countryAreas)
  position = Names.index(findName)
  HEADER()
  length = 20
  for info in range(len(Names)):
    if len(Names[position]) < length:
      Names[position] = "# " + Names[position] + (" " * (length - len(Names[position])) + "#")
      Capitals[position] = Capitals[position] + (" " * (length - len(Capitals[position])) + "#")
      Populations[position] = Populations[position] + (" " * (length - len(Populations[position])) + "#")
      Areas[position] = Areas[position] + (" " * (length - len(Areas[position])))
      print(Names[position], Capitals[position], Populations[position], Areas[position] + "#")
  FOOTER()

def findSpecificInfoNAMES(key, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = allAreas(countryAreas)
  pattern = "^{}".format(key)
  HEADER()
  length = 20
  for NAME in Names:
    searching = re.search(pattern, NAME)
    if searching:
      position = Names.index(NAME)
      Names[position] = "# " + Names[position] + (" " * (length - len(Names[position])) + "#")
      Capitals[position] = Capitals[position] + (" " * (length - len(Capitals[position])) + "#")
      Populations[position] = Populations[position] + (" " * (length - len(Populations[position])) + "#")
      Areas[position] = Areas[position] + (" " * (length - len(Areas[position])))
      print(Names[position], Capitals[position], Populations[position], Areas[position] + "#")
  FOOTER()
     
  
def findSpecificInfoCAPITALS(key, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = allAreas(countryAreas)
  pattern = "^{}".format(key)
  HEADER()
  length = 20
  for CAPITAL in Capitals:
    searching = re.search(pattern, CAPITAL)
    if searching:
      position = Capitals.index(CAPITAL)
      Names[position] = "# " + Names[position] + (" " * (length - len(Names[position])) + "#")
      Capitals[position] = Capitals[position] + (" " * (length - len(Capitals[position])) + "#")
      Populations[position] = Populations[position] + (" " * (length - len(Populations[position])) + "#")
      Areas[position] = Areas[position] + (" " * (length - len(Areas[position])))
      print(Names[position], Capitals[position], Populations[position], Areas[position] + "#")
  FOOTER()
      
def findSpecificInfoPOPULATIONS(startRange, endRange, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = list(map(lambda value: int(value), allPopulations(countryPopulations)))
  Areas = allAreas(countryAreas)
  HEADER()
  length = 20
  for POPULATION in Populations:
    if startRange <= POPULATION <= endRange:
      position = Populations.index(POPULATION)
      Names[position] = "# " + Names[position] + (" " * (length - len(Names[position])) + "#")
      Capitals[position] = Capitals[position] + (" " * (length - len(Capitals[position])) + "#")
      Populations[position] = str(Populations[position]) + (" " * (length - len(str(Populations[position]))) + "#")
      Areas[position] = Areas[position] + (" " * (length - len(Areas[position])))
      print(Names[position], Capitals[position], Populations[position], Areas[position] + "#")
  FOOTER()
      
def findSpecificInfoAREAS(startRange, endRange, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = list(map(lambda value: float(value), allAreas(countryAreas)))
  HEADER()
  length = 20
  for AREAS in Areas:
    if startRange <= AREAS <= endRange:
      position = Areas.index(AREAS)
      Names[position] = "# " + Names[position] + (" " * (length - len(Names[position])) + "#")
      Capitals[position] = Capitals[position] + (" " * (length - len(Capitals[position])) + "#")
      Populations[position] = Populations[position] + (" " * (length - len(Populations[position])) + "#")
      Areas[position] = str(Areas[position]) + (" " * (length - len(str(Areas[position]))))
      print(Names[position], Capitals[position], Populations[position], Areas[position] + "#")
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
