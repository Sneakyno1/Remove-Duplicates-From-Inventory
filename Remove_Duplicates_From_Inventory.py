import csv

ITEM_NAME = 1
DEPARTMENT = 4
CATEGORY = 5

print("Starting")

#Open the input csv in a content manageer
with open('2022workingcsv.csv','r', encoding='utf8') as inputCSV:
     CSVContent = csv.reader(inputCSV, delimiter = ',')

     #Generate a list comprised of the rows in the csv 
     #except for the rows where the name of the item starts with the string 'zz'
     listWithNoZZ = [row for row in CSVContent if row[1][:2] != 'zz']

     print('Entries with \'zz\' removed')


     #initializing a dictionary that will have the category name as the key
     #the associated value will be a list of the items in that category
     categoryDictionary = dict()
     
     for line in listWithNoZZ:
         categoryDictionary[line[CATEGORY]]=list()

     for line in listWithNoZZ:
         categoryDictionary[line[CATEGORY]].append(line[ITEM_NAME])


     #open the output csv in another context manager
     with open('ZZClearedCSV.csv', 'w', newline='', encoding='utf8') as outputCSV:
          output=csv.writer(outputCSV, delimiter = ',')

          #We're doing this quick output.writereow() here so the headers will make it in 
          #withoutbeing affected by  the following for loop 
          output.writerow(listWithNoZZ[0])

          #any row where the category isn't 'general' gets changed to 'general'
          for line in listWithNoZZ[1:]:
               if line[5] != 'general':
                    line[5] = 'general'
               output.writerow(line)

               

print('done')