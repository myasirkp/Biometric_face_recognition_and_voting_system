import sys
import csv
with open('table.csv','rb') as csvfile:
    read=csv.reader(csvfile)
    idnums=[]
    names=[]
    for row in read:
        idnum= row[0]
        name=row[1]
        idnums.append(idnum)
        names.append(name)
data=input('Enter the data to be found')
data=str(data)
find_id=idnums.index(data)
find_name=names[find_id]
print find_name


