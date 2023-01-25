import csv


print("Starting")

with open('2022workingcsv.csv','r', encoding='utf8') as inputCSV:
     CSVContent = csv.reader(inputCSV, delimiter = ',')

     with open('ZZClearedCSV.csv', 'w', newline='', encoding='utf8') as outputCSV:
          output=csv.writer(outputCSV, delimiter = ',')

          for row in CSVContent:
               if row[1][:2]=='zz':
                    continue
               else:
                    output.writerow(row)

print('done')