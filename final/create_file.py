import sys
import csv
table= '1,subject01\n100,Yasir\n101,Jibin'
#data= tabulate(table,headers=['id','Name'])
f=open('table.csv','w')
f.write(table)
f.close()
