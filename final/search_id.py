import sys
import csv
with open('table.csv','rb') as csvfile:
    read=csv.reader(csvfile)
    idnums=[]
    names=[]
    statuses=[]
    row_num=0
    for row in read:
        idnum= row[0]
        name=row[1]
        status=row[2]
        idnums.append(idnum)
        names.append(name)
        statuses.append(status)
        row_num=row_num+1
data=input('Enter the data to be found')
data=str(data)
find_id=idnums.index(data)
find_name=names[find_id]
print find_name
if int(statuses[find_id])==0:
    print 'Ready to vote'
    with open('table.csv','wb') as csvfile:
        write=csv.writer(csvfile)
        statuses[find_id]=1
        for i in range(0,row_num):
            row[i]=idnums[i],names[i],statuses[i]
            write.writerow(row[i])


