"""
File    : pokemon.py
Author  : Hamzah Firman
Purpose : This program reads a Pokemon data from a file and arranges it
          according to its Pokemon type.Then, repeatedly reads in queries
          from the user and prints out solutions to those queries. 
Course  : CSC 120 / Spring 2019 / section 1A

"""

"""
Function       : This function executes other functions within this function. 
Parameters     : None.
Returns        : None.
Pre-condition  : None.
Post-condition : None.
"""
def main():
    
    pokeData = fileReading()
    print_poke(pokeData)
    
    
    
"""
Function       : This function reads an input file from the user and iterates
                 through its items as it organizes the data into a data
                 structure called a two-level dictionary (a dictionary
                 of dictionaries).
Parameters     : None
Returns        : A two-level dictionary consists of all of the information about
                 Pokemon belonging to a specific type. 
Pre-condition  : None.
Post-condition : The return value is a two-level dictionary which consists of
                 Pokemon types as the first key and Pokemon names as the
                 second key as its values are a list of integers.
"""

def fileReading():

    allPokeDict = {}

    file = open(input()).readlines() # Silent prompt

    for element in range(1,(len(file))):  # has no len(); not a list[] or set() or dict{}
        splitted    = file[element].strip('\n').split(',')
        pokeName    = splitted[1]      # Pokemon Names
        pokeType    = splitted[2]      # Pokemon Types
        pokeQueries = splitted[4:13]   # Pokemon Datas
        


        if pokeType not in allPokeDict.keys(): # Checks for a new Poke type
            allPokeDict[pokeType] = {}
    
        allPokeDict[pokeType][pokeName] = pokeQueries
                    
    return allPokeDict
    
"""
Function       : This function traverses a two-level dictionary consists of all
                 of the information about Pokemon belonging to a specific type
                 and calculates the average value for each query as it saves
                 the value into a new dictionary indexed by Pokemon type.
Parameters     : a.) pokeDict - A two-level dictionaries consists of all of
                 the information about Pokemon belonging to a specific type.
Returns        : A dictionary which consist of  Pokemon types as keys and a
                 list of integer values.
Pre-condition  : pokeDict is a two-level dictionaries and b.) num is an integer 
Post-condition : The return value is a dictionary. 
"""
def poke_avg(pokeDict,num):

    poke = {}
    
    for key1 in pokeDict.keys(): # Pokemon Types
        pokeList             = []
        pokeLen              = len(pokeDict[key1])
        totalSum             = 0
       

        for key2 in pokeDict[key1].values(): # Pokemon Datas
            totalSum          += int(key2[num])
    
        
        total_avg          = totalSum / pokeLen # Average Value
       

        pokeList.append(total_avg)
    
        poke[key1] = pokeList

    return poke
"""
Function       : This function iterates a two-level dictionary consists of all
                 of the information about Pokemon belonging to a specific type
                 and calculates the average value for each query as it saves
                 the value into a new dictionary indexed by Pokemon type.
Parameters     : a.) 'pokeDict' - A two-level dictionaries consists of average
                 values of Pokemon belonging to a specific type b.) 'num' - an
                 integer. 
Returns        : None.
Pre-condition  : pokeDict is a dictionary and num is an interger. 
Post-condition : Prints out a Pokemon type with an average value. 
"""
        
def max_grid(pokeDict,num):

    max = 0
    for poke in pokeDict:
        pokeValues = pokeDict[poke]
        if max < pokeValues[num]:
            maxList = [poke]
            max = pokeValues[num]
        elif max == pokeValues[num]:
            maxList.append(poke)

    maxList.sort()
    for maxVals in maxList:
        print ("{}: {}".format(maxVals, max))


"""
Function       : This function reads in queries from the user and prints out
                 solutions to those queries until the user enters an empty line. 
Parameters     : A two-level dictionary consists of average values of 
                 Pokemon belonging to a specific type.
Pre-condition  : pokeData is a two-level dictionary.
Post-condition : The return value is an empty line/ string.
"""


def print_poke(pokeData):

    userInput = input() # Silent Prompt

    querries = {'total': 0, 'hp': 1, 'attack': 2, 'defense' : 3, 'specialattack'
                : 4,'specialdefense': 5, 'speed' : 6}

    while userInput != '':
        userLower = userInput.lower()

        for item in querries:
            if userLower == item.lower():
                pokeDict = poke_avg(pokeData,querries[item])
                max_grid(pokeDict, 0)
        userInput = input()

    return ''
            
        
main()
