import csv


# these variables represent the corresponding index into the csv row
ITEM_NAME = 1
DEPARTMENT = 4
CATEGORY = 5


def main():
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
    seasonalDictionary = dict()
    
    #load dictionary with empty lists where the key is the category name
    #but only adds the category if it starts with the string seasonal
    for line in listWithNoZZ[1:]:
        if line[CATEGORY][:8].lower()=='seasonal':
            seasonalDictionary[line[CATEGORY]] = list()
    
    #add items to appropriate list based on category
    for line in listWithNoZZ[1:]:
        if line[CATEGORY][:8].lower()=='seasonal':
           seasonalDictionary[line[CATEGORY]].append(line[ITEM_NAME])
    
    #Initializing a dictionary that will hold lists like seasonalDicitonary
    departmentDictionary = dict()
    
    #adds entry into dictionary only if the category doesnt start with 'seasonal'
    for line in listWithNoZZ[1:]:
        if line[CATEGORY][:8].lower()=='seasonal':
            continue
        departmentDictionary[line[DEPARTMENT]] = list()
    
    for line in listWithNoZZ[1:]:
        if line[CATEGORY][:8].lower()=='seasonal':
            continue
        departmentDictionary[line[DEPARTMENT]].append(line[ITEM_NAME])
    
    
    #Makes one csv per category
    for key in seasonalDictionary:
        print('Working on category: '+ key)
        with open( key+'.csv', 'w', newline='', encoding='utf8') as categoryCSV:
            output=csv.writer(categoryCSV, delimiter = ',')
            output.writerow(listWithNoZZ[0])
            for item in seasonalDictionary[key]:
                for line in listWithNoZZ[1:]:
                    if line[ITEM_NAME]==item:
                        output.writerow(line)
    
    #Makes one csv per department
    for key in departmentDictionary:
        print('Working on department: '+ key)
        with open( key+'.csv', 'w', newline='', encoding='utf8') as departmentCSV:
            output=csv.writer(departmentCSV, delimiter = ',')
            output.writerow(listWithNoZZ[0])
            for item in departmentDictionary[key]:
                for line in listWithNoZZ[1:]:
                    if line[ITEM_NAME]==item:
                        output.writerow(line)
    
    
    #write the total csv without 'zz' including all departments and categories
    with open('ZZClearedCSV.csv', 'w', newline='', encoding='utf8') as outputCSV:
         output=csv.writer(outputCSV, delimiter = ',')
    
         for line in listWithNoZZ:
              output.writerow(line)
    
              
    
    print('done')

if __name__ == 'main':
    main()