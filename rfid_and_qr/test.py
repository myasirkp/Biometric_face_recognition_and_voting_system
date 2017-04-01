import serial
import threading
import Queue
import Tkinter as tk
global sum_total
import pyqrcode
from PIL import Image, ImageTk

class SerialThread(threading.Thread):
    def __init__(self, queue):
        self.sum=0
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        global sum_total
        sum_total=0
        s = serial.Serial('/dev/ttyS0',9600)
        
        while True:
            if s.inWaiting():
                text = s.read(12)
                if (text=="090073C805B7"):
                    self.sum=self.sum+30
                    self.queue.put("Soap : LUX-200g \t Price : 30 Rs \t Total:"+str(self.sum)+" Rs\n")
                    
                    
                    sum_total=self.sum
                elif (text=="3B005063F4FC"):
                    self.sum=self.sum+40
                    self.queue.put("Notebook : Classmate-100pgs \t Price : 40 Rs \t Total:"+str(self.sum)+" Rs\n")
            
                    sum_total=self.sum

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry("1360x750")

        
        
        frameLabel= tk.Frame(self, padx=40, pady =40,)
        self.text = tk.Text(frameLabel, wrap='word', font='TimesNewRoman 37',
                            bg=self.cget('bg'), relief='flat')

        
        self.labelVariable=tk.StringVar()
        label = tk.Label(frameLabel,textvariable=self.labelVariable,font='TimesNewRoman 37',anchor="w", fg="white", bg="blue")
        button=tk.Button(frameLabel,text=u"Done Shopping !", font='TimesNewRoman 37',command=self.OnButtonClick)
        button.pack()
        label.pack()
        frameLabel.pack()
        self.text.pack()
    
        
        self.queue = Queue.Queue()
        
        thread = SerialThread(self.queue)
        thread.start()
        self.process_serial()
        
    def OnButtonClick(self):
        self.labelVariable.set("Pay "+str(sum_total)+" Rs")
        img=pyqrcode.create(str(sum_total))
        img.png('total.png',scale=8)
        image=Image.open('total.png')
        image.show()
 

    def process_serial(self):
         #self.text.delete(1.0, 'end')
         while self.queue.qsize():
            try:
                self.text.insert('end', self.queue.get())
            except Queue.Empty:
                pass
         self.after(1000, self.process_serial)

app = App()
app.mainloop()
