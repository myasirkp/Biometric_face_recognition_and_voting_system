import Tkinter

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.output(11,0)
GPIO.output(3,0)
GPIO.output(5,0)
GPIO.output(7,0)
GPIO.output(13,0)
GPIO.output(15,0)
GPIO.output(16,0)

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent=parent
        self.initialize()
        
    def initialize(self):
        
        self.grid()
        self.num=1
        self.num1=1
        self.num2=1
        self.num3=1
        
        self.entryVariable = Tkinter.StringVar()
        self.entry=Tkinter.Entry(self,textvariable=self.entryVariable)
        self.entry.grid()
        
        self.entry.bind("<Right>", self.OnPressRight)
        self.entry.bind("<Up>", self.OnPressUp)
        self.entry.bind("<Down>", self.OnPressDown)
        self.entry.bind("<Left>", self.OnPressLeft)
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entry.bind("z", self.OnpressS)
        self.entry.bind("x", self.OnpressA)
        #self.entryVariable.set(u"Enter text here :")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

       
       # button=Tkinter.Button(self,text=u"Click me !", command=self.OnButtonClick)
        #button.grid(column=1,row=0)
        

        self.labelVariable=Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,anchor="w", fg="white", bg="blue")
        label.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.labelVariable.set(u"Ready")

        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())

    def OnButtonClick(self):
        self.labelVariable.set(self.entryVariable.get()+" (You clicked the button !)")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressRight(self,event):
        self.labelVariable.set(" Right")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        GPIO.output(11,1)
        GPIO.output(3,0)
        GPIO.output(5,0)
        GPIO.output(7,0)
        sleep(.1)
        GPIO.output(11,0)
        GPIO.output(3,0)
        GPIO.output(5,0)
        GPIO.output(7,0)

    def OnPressLeft(self,event):
        self.labelVariable.set("Left")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        GPIO.output(11,0)
        GPIO.output(3,0)
        GPIO.output(5,1)
        GPIO.output(7,0)
        sleep(.1)
        GPIO.output(11,0)
        GPIO.output(3,0)
        GPIO.output(5,0)
        GPIO.output(7,0)

    def OnPressUp(self,event):
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        self.num2=self.num2+1
        if self.num2%2==0:
            self.labelVariable.set("Forward")
            GPIO.output(11,1)
            GPIO.output(3,0)
            GPIO.output(5,1)
            GPIO.output(7,0)
        else:
            self.labelVariable.set("Stopped")
            GPIO.output(11,0)
            GPIO.output(3,0)
            GPIO.output(5,0)
            GPIO.output(7,0)


    def OnPressDown(self,event):
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        self.num3=self.num3+1
        if self.num3%2==0:
            self.labelVariable.set("Back")
            GPIO.output(11,0)
            GPIO.output(3,1)
            GPIO.output(5,0)
            GPIO.output(7,1)
        else:
            self.labelVariable.set("Stopped")
            GPIO.output(11,0)
            GPIO.output(3,0)
            GPIO.output(5,0)
            GPIO.output(7,0)

    def OnPressEnter(self,event):
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        self.num=self.num+1
        if self.num%2==0:
            self.labelVariable.set(" Water pump on")
            GPIO.output(13,1)
        else:
            self.labelVariable.set(" Water pump off")
            GPIO.output(13,0)
            
    def OnpressS(self,event):
        self.labelVariable.set("Nozzle rotating")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        GPIO.output(15,1)
        sleep(0.5)
        GPIO.output(15,0)

    def OnpressA(self,event):
        self.labelVariable.set("Direction changed")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)
        self.num1=self.num1+1
        if self.num1%2==0:
            GPIO.output(16,1)
        else:
            GPIO.output(16,0)
        

if __name__=="__main__":
    app=simpleapp_tk(None)
    app.title('my application')
    app.mainloop()
    GPIO.cleanup()
