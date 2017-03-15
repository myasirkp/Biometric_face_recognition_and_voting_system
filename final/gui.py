#this is the main gui for the project
import Tkinter
import os
from picamera import PiCamera
from time import sleep
import sys
import csv

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent=parent
        self.initialize()

    #get training data
    def OnButtonClick_newId(self):
        self.labelVariable.set("Capturing training data")
        camera = PiCamera()
        camera.resolution=(320,240)
        arg=sys.argv[1]
        for i in range(1,11):
            path='/home/pi/Desktop/New/train/'
            path=path+arg+'.'+str(i)+'.jpg'
            camera.start_preview()
            sleep(3)
            camera.capture(path)
            camera.stop_preview()
        #check duplicate
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
                idnum= row[0]
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
            with open('table.csv','a') as f:
                writer=csv.writer(f)
                data=id_num,name_new,str(0)
                writer.writerow(data)
                f.close()
                print 'new voter added with:'
                print 'id ',id_num
                print 'name ',name_new

    #training
    def OnButtonClick_train(self):
        self.labelVariable.set("Training...")
        os.system('python new.py')

    #capture image for identification
    def OnButtonClick_image(self):
        self.labelVariable.set("Capturing image")
        camera = PiCamera()
        camera.resolution=(320,240)
        camera.start_preview()
        sleep(5)
        camera.capture('/home/pi/Desktop/gui/detect/test.jpg')
        camera.stop_preview()

    #find from file
    def OnButtonClick_detect(self):
        self.labelVariable.set("Recognizing voter")
        os.system('python newd.py')
    
    def initialize(self):
        
        self.grid()
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())
        
        button1=Tkinter.Button(self,text=u"Register new voter", command=self.OnButtonClick_newId)
        button1.grid(column=0,row=0)

        button2=Tkinter.Button(self,text=u"Train", command=self.OnButtonClick_train)
        button2.grid(column=0,row=1)

        button3=Tkinter.Button(self,text=u"Capture Image", command=self.OnButtonClick_image)
        button3.grid(column=0,row=2)

        button4=Tkinter.Button(self,text=u"Recognize", command=self.OnButtonClick_detect)
        button4.grid(column=0,row=3)
        

        self.labelVariable=Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,anchor="w", fg="white", bg="blue")
        label.grid(column=0,row=4,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Ready for next voter")


#main loop
if __name__=="__main__":
    app=simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
