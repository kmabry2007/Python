import tkinter
from tkinter import *
from datetime import datetime, timezone
import time
#

class ExampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.label = Label(self, text='', width=20)
        self.label.pack()
        self.remaining = 0
        self.countdown(600)

    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining
            self.withdraw()

        if self.remaining <= 0:
            self.label.configure(text='')
            stid.config(state = 'active', relief = 'raised')
            id_timer.set('Please ID! [Press to Reset]')
            
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)
# Event function setup
def tick():
# get UTC date and time from datetime
    now_utc = datetime.now(timezone.utc).strftime('%A %m-%d-%Y %H:%M:%S')
# if time string has changed, update it
    clock.config(text=now_utc)
# calls itself every 200 milliseconds
# to update the time display as needed
# could use >200 ms, but display gets jerky
    clock.after(200, tick)

def st_id():
	# start 10 minute timer
	# get UTC date and time from datetime
    id_timer.set('10 minute timer started!')
    stid.config(state = 'disabled', relief = 'sunken')
    app = ExampleApp()

	
if __name__ == '__main__':
    # Set up the root frame window.
   root = Tk()
root.title('UTC Time & Date')
#
root.minsize(100,100)
root.geometry('200x200+400+100')
id_timer = StringVar(root, 'Press to Start')
#

####  Construct 3 pane window
m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left panel", height = 50, width=70, relief=RIDGE)
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="top panel", height=15, relief=RIDGE)
m2.add(top)

bottom = Label(m2, text="UTC Time & Station ID panel", relief = RIDGE)
m2.add(bottom)
# End of 3 paned window construction.
#
#!!!!!!  Construct entries which are contained in the m2 pane
# Can use grid within these sub-frames!!!

#!!!!!!!!!!! end of entries.
#
clock = Label(bottom, font=('Times', 12, 'normal'), bg='light grey', fg='blue')
clock.grid( row=0, column =1)
#
tick()
#
stid= Button(bottom, textvariable=id_timer, command=st_id)
stid.grid(row=1, column=1)
# Let 'er rip.
#
root.mainloop()
