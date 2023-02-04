import csv

# these variables represent the corresponding index into the csv row
ITEM_NAME = 1
DEPARTMENT = 4
CATEGORY = 5

print("Starting")

#Open the input csv in a content manageer and read it into a list
with open('2022workingcsv.csv','r', encoding='utf8') as inputCSV:
     CSVContent = csv.reader(inputCSV, delimiter = ',')

     #Generate a list comprised of the rows in the csv 
     #except for the rows where the name of the item starts with the string 'zz'
     listWithNoZZ = [row for row in CSVContent if row[1][:2] != 'zz']

     print('Entries with \'zz\' removed')


#initializing a dictionary that will have the category name as the key
#the associated value will be a list of the items in that category
categoryDictionary = dict()

for line in listWithNoZZ[1:]:
    categoryDictionary[line[CATEGORY]]=list()

for line in listWithNoZZ[1:]:
    categoryDictionary[line[CATEGORY]].append(line[ITEM_NAME])
    
for key in categoryDictionary:
    if key == 'general':
        continue;
    for item in categoryDictionary[key]:
        if categoryDictionary['general'].count(item)>0:
            print("found a duplicate item")
            categoryDictionary['general'].remove(item)
            

for key in categoryDictionary:
    print('Working on category: '+ key)
    with open( key+'.csv', 'w', newline='', encoding='utf8') as categoryCSV:
        output=csv.writer(categoryCSV, delimiter = ',')
        output.writerow(listWithNoZZ[0])
        for item in categoryDictionary[key]:
            for line in listWithNoZZ[1:]:
                if line[ITEM_NAME]==item:
                    output.writerow(line)


#open the output csv in another context manager
with open('ZZClearedCSV.csv', 'w', newline='', encoding='utf8') as outputCSV:
     output=csv.writer(outputCSV, delimiter = ',')

     for line in listWithNoZZ:
          output.writerow(line)

          

print('done')