from picamera import PiCamera
from time import sleep
import sys
import csv

camera = PiCamera()
camera.resolution=(320,240)
    
arg=sys.argv[1]
find_id=0;
arg_new=arg.split('subject')
id_num=arg_new[1]
name_new=sys.argv[2]

with open('table.csv','rb') as csvfile:
    read=csv.reader(csvfile)
    idnums=[]
    names=[]
    statuses=[]
    row_num=0
    for row in read:
        idnum=row[0]
        name=row[1]
        status=row[2]
        idnums.append(idnum)
        names.append(name)
        statuses.append(status)
        row_num=row_num+1
        
data=id_num
data=str(data)
try:
    find_id=idnums.index(data)
    print 'Voter already registered'
except:
    for i in range(1,11):
        path='/home/pi/Desktop/gui/train/'
        path=path+arg+'.'+str(i)+'.jpg'
        camera.start_preview()
        sleep(3)
        camera.capture(path)
        camera.stop_preview()

    with open('table.csv','a') as f:
        writer=csv.writer(f)
        data=id_num,name_new,str(0)
        writer.writerow(data)
        f.close()
        print 'new voter added with:'
        print 'id ',id_num
        print 'name ',name_new
