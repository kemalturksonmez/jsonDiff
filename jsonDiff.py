#!/usr/bin/env python3
import json
import sys

# parses JSON structured files
# fileName - address of file being parsed
def readJson(fileName):
    try:
        with open(fileName, 'r') as file:
            data = file.read()
            jsonFormat = json.loads(data)
            return jsonFormat
    except:
        print('Please provide two JSON structured files')
    

# Compares two json structures by representing each object and array value
# as having the same value
# jsonStruct - a parsed json structure
# jsonSet - the set that stores the extracted json object and array values
def convertToSet(jsonStruct, jsonSet):
    for obj in jsonStruct:
        val = jsonStruct[obj]
        if type(val) == list:
            jsonSet.add(obj + ': []')
            for item in val:
                if type(item) == dict: 
                    convertToSet(item, jsonSet)
                else:
                    jsonSet.add(item)
        elif type(val) == dict:
            convertToSet(val, jsonSet)
        else:
            jsonSet.add(str(obj) + ': ' + str(val))

# Compares two JSON structures where array values are weighted
# by depth
# jsonStruct - a parsed json structure
# jsonSet - the set that stores the extracted json object and array values
# prevVal - reference to name of array
# def convertToSet(jsonStruct, jsonSet, prevVal=''):
#     for obj in jsonStruct:
#         val = jsonStruct[obj]
#         if type(val) == list:
#             for item in val:
#                 if type(item) == dict: 
#                     convertToSet(item, jsonSet, str(obj) + ': ')
#                 else:
#                     jsonSet.add(str(prevVal) 
#                     + str(val) + ': ' + item)
#         elif type(val) == dict:
#             convertToSet(val, jsonSet)
#         else:
#             jsonSet.add(str(prevVal)
#             + str(obj) + ': ' + str(val))

# Prints the jaccard coefficient of two provided sets
def getJaccardCoef(setOne, setTwo):
    setUnion = setOne.union(setTwo)
    setInter = setOne.intersection(setTwo)
    print(len(setInter)/len(setUnion))

# Check for length of arguments first
if len(sys.argv) != 3:
    print('Program Terminated: Please provide two JSON files')
else:
    # Ensure that you are provided with json file
    if sys.argv[1].lower().endswith('json') and sys.argv[1].lower().endswith('json'):
        file1 = readJson(sys.argv[1])
        file2 = readJson(sys.argv[2])
        # Create sets
        set1 = set()
        set2 = set()
        # Extract json structs to sets
        convertToSet(file1, set1)
        convertToSet(file2, set2)
        # Find Jaccard coefficient
        getJaccardCoef(set1,set2)
    else:
        print('Program Terminated: Please provide two JSON files')

