import tkinter
from tkinter import *
from datetime import datetime, timezone
import time
#
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

  
if __name__ == '__main__':
    # Set up the root frame window.
   root = Tk()
root.title('UTC Time & Date')
#
root.minsize(100,100)
root.geometry('200x200+400+100')
#
clock = Label(root, font=('Times', 30, 'bold'), bg='light grey', fg='blue')
clock.pack(side = 'left', fill=X, expand=0)
#
tick()
#
# Let 'er rip.
#
root.mainloop()   