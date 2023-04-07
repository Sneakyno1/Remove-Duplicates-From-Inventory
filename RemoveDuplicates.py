#!/usr/bin/env python
import csv
import os

# these variables represent the corresponding index into the csv row
ITEM_NAME = 1
DEPARTMENT = 4
CATEGORY = 5

inputPath = input("Please type in, or copy-paste, the full file path for where the excel file is located and then press enter: \n")
outputPath = input("Please type in, or copy-paste, the full file path for where the finished excel files will be located \nand then press enter: \n")

for root, dirs, files in os.walk(inputPath):
    for file in files:
        if str.lower(file[-3:]) == "csv":
            inputPath += '\\' + file

print("Grabbing file from: " + inputPath)
print("Outputting files to: " + outputPath)
print("Starting")

#Open the input csv in a content manageer and read it into a list
with open(inputPath,'r', encoding='utf8') as inputCSV:
     CSVContent = csv.reader(inputCSV, delimiter = ',')

     #Generate a list comprised of the rows in the csv 
     #except for the rows where the name of the item starts with the string 'zz'
     listWithNoZZ = [row for row in CSVContent if row[1][:2] != 'zz']

     print('Entries with \'zz\' removed')


#initializing a dictionary that will have the category name as the key
#the associated value will be a list of the items in that category
seasonalDictionary = dict()

#Initializing a dictionary that will hold lists like seasonalDicitonary
departmentDictionary = dict()

#initialize dictionaries with their lists
for line in listWithNoZZ[1:]:
    if line[CATEGORY][:8].lower()=='seasonal':
        seasonalDictionary[line[CATEGORY]] = list()
    else:
        departmentDictionary[line[DEPARTMENT]] = list()

#add items to appropriate list based on category and department
for line in listWithNoZZ[1:]:
    if line[CATEGORY][:8].lower()=='seasonal':
       seasonalDictionary[line[CATEGORY]].append(line[ITEM_NAME])
    else:
        departmentDictionary[line[DEPARTMENT]].append(line[ITEM_NAME])



#Makes one csv per category
for key in seasonalDictionary:
    print('Working on category: '+ key)
    with open( outputPath+'\\'+key+'.csv', 'w', newline='', encoding='utf8') as categoryCSV:
        output=csv.writer(categoryCSV, delimiter = ',')
        output.writerow(listWithNoZZ[0])
        for item in seasonalDictionary[key]:
            for line in listWithNoZZ[1:]:
                if line[ITEM_NAME]==item:
                    output.writerow(line)

#Makes one csv per department
for key in departmentDictionary:
    print('Working on department: '+ key)
    with open( outputPath+'\\'+key+'.csv', 'w', newline='', encoding='utf8') as departmentCSV:
        output=csv.writer(departmentCSV, delimiter = ',')
        output.writerow(listWithNoZZ[0])
        for item in departmentDictionary[key]:
            for line in listWithNoZZ[1:]:
                if line[ITEM_NAME]==item:
                    output.writerow(line)


#write the total csv without 'zz' including all departments and categories
with open(outputPath+'\\'+'ZZClearedCSV.csv', 'w', newline='', encoding='utf8') as outputCSV:
     output=csv.writer(outputCSV, delimiter = ',')

     for line in listWithNoZZ:
          output.writerow(line)

          

print('done')

