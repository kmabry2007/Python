# !/usr/bin/python3
# python 3.x
import datetime
from datetime import datetime, timezone
import tkinter.font
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import time
from time import strftime
#
import sys
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



def close_log():
    status.set('Closes the current logbook...')
    messagebox.askyesno('Close', 'Close the current logbook?')
    #kill child for logbook...
    status.set('Logbook Closed.')
#
#
def save_log():
    status.set('Saves the current logbook...')
    messagebox.askyesno('Save', 'Save the current logbook?')
    #
    # do something here with the log book
    #
    status.clear()
#
def open_log():
    status.set('Selected Logbook open')
# create a listbox which would format the log records in a listbox
# this is a simple list example. Note!! Multiple copies can open,
# so it is best to grey out.. or make menu selection inactive once opened.


def import_log():
    status.set('Imports a new logbook...')
    messagebox.askyesno('Import', 'Import a new logbook?')
    status.clear()  
#
#
def export_log():
    status.set('Exports a new logbook...')
    messagebox.askyesno('Import', 'Export a new logbook?')
    status.clear()
    #
def utc_date_time():
    now_utc = datetime.now(timezone.utc).strftime('%A %m-%d-%Y %H:%M:%S')
    status.set('This is the current UTC Date and Time...')
    messagebox.showinfo('UTC Date -Time', now_utc)
    status.clear()
#
def callback():
    status.set('This is a callback...')
    messagebox.showinfo('Info', 'Called the Callback!')
    status.clear()
#
# provide for exiting the program.
def on_closing():
    status.set('This closes the program.')
    if messagebox.askokcancel('Quit', 'Do you want to quit?'):
        root.destroy()
    else:
       status.clear()
#
# About box information
def About():
    status.set('Program information.')
    messagebox.showinfo(
        'About',
'''Copyright by Kelly Mabry K5AID, 2018 Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License. You may obtain a copy of the
License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is
distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
express or implied. See the License for the specific language governing permissions and
limitations under the License.'''
        )
    status.clear()
# set up classes
class StatusBar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.label.pack(fill=X)

    def set(self, format, *args):
        self.label.config(text=format % args)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text='')
        self.label.update_idletasks()
        

if __name__ == '__main__':
    # Set up the root frame window.
   root = Tk()
root.title('ProLog')
# Position the root frame on the screen; 800x600 is the size of the form; and 400+100 is
# the position on the screen
root.minsize(300,300)
root.geometry('800x600+400+100')
# create the menu bar
menu = Menu(root)
root.config(menu=menu)
# create file menu
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Logbook', menu=filemenu)
filemenu.add_command(label='New Log', command=callback) # here do a button function
filemenu.add_command(label='Open Log', command=open_log)
filemenu.add_command(label='Save Log', command=save_log)
filemenu.add_command(label='Close Log', command=close_log)
filemenu.add_separator()
filemenu.add_command(label='Import Log...', command=import_log)
filemenu.add_command(label='Export Log...', command=export_log)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=on_closing) # call exit window and quit
# create help menu
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About...', command=About)
# create time menu
timemenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Time', menu=timemenu)
timemenu.add_command(label='UTC Time & Date',command=utc_date_time)
# create a toolbar
#
# create a toolbar
toolbar = Frame(root)

b = Button(toolbar, text='new', width=4, command=callback)
b.pack(side=LEFT, padx=2, pady=2)

b = Button(toolbar, text='open', width=4, command=callback)
b.pack(side=LEFT, padx=2, pady=2)

clock = Label(toolbar, font=('Piboto', 12, 'bold'), bg='light grey')
clock.pack(side = RIGHT, fill=X, expand=0)

tick()

toolbar.pack(side=TOP, fill=X)
#
# create status bar       
status = StatusBar(root)
status.pack(side=BOTTOM, fill=X)
root.update()
#
status.set('Initializing, Please Wait...')
root.after(1000)
status.set('Ready...')
root.after(750)
status.set('No Logbook is currently open.')
# Set the panes up here... the listbox is placed and opened in the function 'open'
# m1 is the name of the paned window.
m1 = PanedWindow()
m1.pack(fill='both', expand=1)
#
logbook = Label(m1, text='logbook here', relief = SUNKEN, height=20, width = 55)
m1.add(logbook)
#
m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)
#
util_panel = Label(m2, text='utility panel', relief = SUNKEN, height = 30, width = 30)
m2.add(util_panel)
#
task_panel = Label(m2, text='task panel',relief = SUNKEN)
m2.add(task_panel)
#
#

#Make a log entry grid with in the sub panel, m2
# grid method used WITHIN this pane, m2 
Header_fields = ['recno','UTC_date','UTC_time_begin','UTC_time_end','Station_Worked','Report_Sent','Report_Rec','Frequency','Mode','Power','State','Country','Name']
r = 0
for c in Header_fields:
    Label(m2, text=c, relief=RIDGE,width=15).grid(row=r,column=0)
    Entry(m2, bg= 'lightgrey',relief=SUNKEN,width=20).grid(row=r,column=1)
    r = r + 1
# ***completed***
# Make a couple of check boxes for QSL Sent and QSL Rec.
#
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(m2, text = "QSL Sent", variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 10, state=DISABLED).grid(row=25,column=0)
C2 = Checkbutton(m2, text = "QSL Received", variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 10, state=DISABLED).grid(row=25,column=1)
# ***completed***
# Make an entry box for Grid Square
#
#
# ***completed***
# Make an entry box for Remarks
#
#
# ***completed***
#
# Make buttons for adding entries and clearing the form.
#
# End of Panel (subframes) construction.
#
# Let 'er rip.
#
root.protocol(on_closing)
root.mainloop()
