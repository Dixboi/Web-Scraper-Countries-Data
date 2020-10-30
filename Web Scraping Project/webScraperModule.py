
import re

def allNames(countryNames):
  return [name.get_text().replace("  ", "").replace("\n", "") for name in countryNames]

def allCapitals(countryCapitals):
  return [capital.get_text() for capital in countryCapitals]

def allPopulations(countryPopulations):
  return [population.get_text() for population in countryPopulations]

def allAreas(countryAreas):
  return [area.get_text() for area in countryAreas]

def displayAllInfos(countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = allAreas(countryAreas)
  counter = 0
  for info in range(len(Names)):
    print(f'Name: {Names[counter]}')
    print(f'Capital: {Capitals[counter]}')
    print(f'Population: {Populations[counter]}')
    print(f'Area(km squared): {Areas[counter]}')
    print(f'<---{counter + 1}--->')
    counter += 1

def findSpecificInfoGENERAL(findName, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = allAreas(countryAreas)
  position = Names.index(findName)
  print(f'Name: {Names[position]}')
  print(f'Capital: {Capitals[position]}')
  print(f'Population: {Populations[position]}')
  print(f'Area(km squared): {Areas[position]}')

def findSpecificInfoNAMES(key, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = allAreas(countryAreas)
  pattern = "^{}".format(key)
  counter = 0
  for NAME in Names:
    searching = re.search(pattern, NAME)
    if searching:
      position = Names.index(NAME)
      print(f'Name: {Names[position]}')
      print(f'Capital: {Capitals[position]}')
      print(f'Population: {Populations[position]}')
      print(f'Area(km squared): {Areas[position]}')
      print(f'<---{counter + 1}--->')
      counter += 1
  
def findSpecificInfoCAPITALS(key, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = allAreas(countryAreas)
  pattern = "^{}".format(key)
  counter = 0
  for CAPITAL in Capitals:
    searching = re.search(pattern, CAPITAL)
    if searching:
      position = Capitals.index(CAPITAL)
      print(f'Name: {Names[position]}')
      print(f'Capital: {Capitals[position]}')
      print(f'Population: {Populations[position]}')
      print(f'Area(km squared): {Areas[position]}')
      print(f'<---{counter + 1}--->')
      counter += 1

def findSpecificInfoPOPULATIONS(startRange, endRange, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = list(map(lambda value: int(value), allPopulations(countryPopulations)))
  Areas = allAreas(countryAreas)
  counter = 0
  for POPULATION in Populations:
    if startRange <= POPULATION <= endRange:
      position = Populations.index(POPULATION)
      print(f'Name: {Names[position]}')
      print(f'Capital: {Capitals[position]}')
      print(f'Population: {Populations[position]}')
      print(f'Area(km squared): {Areas[position]}')
      print(f'<---{counter + 1}--->')
      counter += 1

def findSpecificInfoAREAS(startRange, endRange, countryNames, countryCapitals, countryPopulations, countryAreas):
  Names = allNames(countryNames)
  Capitals = allCapitals(countryCapitals)
  Populations = allPopulations(countryPopulations)
  Areas = list(map(lambda value: float(value), allAreas(countryAreas)))
  counter = 0
  for AREAS in Areas:
    if startRange <= AREAS <= endRange:
      position = Areas.index(AREAS)
      print(f'Name: {Names[position]}')
      print(f'Capital: {Capitals[position]}')
      print(f'Population: {Populations[position]}')
      print(f'Area(km squared): {Areas[position]}')
      print(f'<---{counter + 1}--->')
      counter += 1

  
