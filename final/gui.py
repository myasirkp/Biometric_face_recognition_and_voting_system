#this is the main gui for the project
import RPi.GPIO as GPIO
import Tkinter
import os
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
        arg=sys.argv[1]
        name_new=sys.argv[2]
        data=arg+' '+name_new
        os.system('python cap.py '+str(data))
    #training
    def OnButtonClick_train(self):
        self.labelVariable.set("Training...")
        os.system('python new.py')

    #capture image for identification
    def OnButtonClick_image(self):
        os.system('python capd.py')
        self.labelVariable.set(u"Voter image captured")

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
    
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(5,GPIO.OUT)
    GPIO.output(5,0)

    app=simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
