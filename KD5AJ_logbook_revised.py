# !/usr/bin/python3
from pathlib import Path
import tkinter
from datetime import datetime, timezone
import tkinter.font
#from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import time, csv, os, sys
from time import strftime
os.chdir('/home/pi')
#
global logbook; logbook = ''
new_qso_record = []
#
def to_uppercase(*args):
    callsign.set(callsign.get().upper())
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
#
def StationID():
    pass

def save_qso():
    date_qso.config(state = 'normal', relief = 'flat')
    start_qso.config(state = 'normal', relief = 'raised')
    end_qso.config(state = 'normal',  relief = 'raised')
    save_qso.config(state = 'disabled')
    clock.config(fg = 'black')
    # here is where we construct and write to a file.
    #qso start date
    new_qso_record.append(qdate)
    #qso start time
    new_qso_record.append(qtime_start)
    #qso end time
    new_qso_record.append(qtime_end)
    #
    station= e1.get()
    new_qso_record.append(station)
    frq = e2.get()
    new_qso_record.append(frq)
    qrst = e3.get()
    new_qso_record.append(qrst)
    mrst = e4.get()
    new_qso_record.append(mrst)
    p = e8.get()
    new_qso_record.append(p)
    m=e9.get()
    new_qso_record.append(m)
    name = e5.get()
    new_qso_record.append(name)
    # removed e6, which was last name.. unnecessary
    city =e7.get()
    new_qso_record.append(city)
    state = state_listbox.get(state_listbox.curselection())
    new_qso_record.append(state)
    #
    print (new_qso_record)
    # define list of places
    with open(logbook, 'a') as filehandle:  
                        for list_item in new_qso_record:
                            filehandle.write('%s ' % list_item)
                        filehandle.write('\n')
                        filehandle.close()
                        new_qso_record.clear()
                           #this is where we update our display of our records. for the log.
                        logdata.config(state=NORMAL)
                        logdata.delete(1.0, END)
                        try:
                            with open(logbook,'r') as UseFile:
                                logdata.insert(END, UseFile.read())
                        except:
                                print('No file exists')
                        logdata.config(state=DISABLED)
    # End of writing qso to log....
    #Clear the record; reset new_qso_record to empty.
    # clear fields for next qso... callsign, Name and City...leave other pre-entered fields.
    callsign.set('W5XYZ')
    e4.delete(0, 'end')
    e4.insert(END, '')
    e5.delete(0, 'end')
    e5.insert(END, '')
    e7.delete(0, 'end') 
    e7.insert(END, '')
    # return focus back to Callsign field.
    e1.focus()
    #set e1 bg and fg attrib.
    
    # End of form clearing.
    # reset button text
    startq.set('Start QSO')
    endq.set('End QSO')
    qso_date_utc.set('UTC Date')
    s_id.config(relief = 'sunken', fg ='green')
    station_id.set('ID every ten minutes.')
    #
    status.set('Saving contact to logbook...')
    time.sleep(1)
    status.clear()
    # Remember to use get(). to actually capture the values for the log
    # Capture all the values and then call a function to write the record to the logbook.
    
def get_time_begin():
    # get UTC date and time from datetime
    utc_date()
    status.set('Inital QSO date is set...')
    time.sleep(1)
    status.clear()
    get_utc_time = datetime.now(timezone.utc).strftime('%H:%M:%S')
    t = 0
    clock.config(fg = 'blue')
    status.set('Inital QSO time is set...')
    time.sleep(1)
    status.clear()
    startq.set(get_utc_time)
    global qtime_start; qtime_start = get_utc_time
    station_id.set('ID Timer Started...')
    print (qtime_start)
    date_qso.config(state = 'disabled', relief = SUNKEN, disabledforeground= 'green')
    start_qso.config(state = 'disabled', relief = SUNKEN, disabledforeground= 'green')
    
def get_time_end():
    # get UTC date and time from datetime
    get_utc_time = datetime.now(timezone.utc).strftime('%H:%M:%S')
    t=0
    endq.set(get_utc_time)
    global qtime_end; qtime_end = get_utc_time
    end_qso.config(state = 'disabled', relief = SUNKEN, disabledforeground = 'green')
    save_qso.config(state = 'active')
    clock.config(fg = 'green')
    status.set('Ending QSO time is set...')
    time.sleep(1)
    status.clear()
    print (qtime_end)
    s_id.config(relief = 'sunken', fg ='green')
    station_id.set('Timer reset')
    
    
    # changed function from get_utc_date(): to utc_date():
def utc_date():
    get_utc_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    qso_date_utc.set(get_utc_date)
    global qdate; qdate = get_utc_date
    status.set('UTC Date retrieved...')
    time.sleep(1)
    status.clear()
    print (qdate)
    
def close_log():
    status.set('Closes the current logbook...')
    messagebox.askyesno('Close', 'Close the current logbook?')
    logdata.config(state=NORMAL)
    logdata.delete(1.0, END)
    #
#
    status.set('Logbook Closed.')  
#
def save_log():
    status.set('Saves the current logbook...')
    messagebox.askyesno('Save', 'Save the current logbook?')
    #
    # do something here with the log book
    status.set('Logbook Saved.')
    time.sleep(2)
    status.clear()
#
def create_log():
    pass
#
def open_log():
    #This is where we lauch the file manager bar.
    global logbook
    #
    logbook = askopenfilename(initialdir='/home/pi/',
                           filetypes =(('Text Files', ' *.txt'),('adif Log Files', '*.adif'),('cabr Log Files', '*.cabr')),
                           title = 'Choose a file.'
                           )
    #    
    #print (logbook)
    
    logdata.config(state=NORMAL)
    logdata.delete(1.0, END)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(logbook,'r') as UseFile:
            #print(UseFile.read())
            logdata.insert(END, UseFile.read())
    except:
        print('No file exists')
        
    logdata.config(state=DISABLED)
    status.set('Selected Logbook open')
    time.sleep(2)
    status.clear()
    
#
#This is where we lauch the file manager bar.
#
#
# Import raw csv data to create a new log.
def import_csv_data():
    status.set('Imports raw CSV data ...')
    name = askopenfilename(initialdir='/home/pi/',
                           filetypes =(('CSV Files', '*.csv'),('All Files','*.*')),
                           title = 'Choose a file.'
                           )
    print (name)
    # 
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            reader = csv.reader(UseFile, delimiter=',')
            data_csv= list(reader)
            for row in data_csv:
              w.insert('end', row[0:1])
              
        UseFile.close()
        status.set('csv data imported...')
        time.sleep(1)
        status.clear()
    except:
        print('No file exists')
        status.set('No Log exists...')  
#
def import_log():
    status.set('Imports a new logbook...')
    name = askopenfilename(initialdir='/home/pi/',
                           filetypes =(('Log Files', '*.adif'),('Cabrillo Log Files', '*.cabr'),('All Files','*.*')),
                           title = 'Choose a file.'
                           )
    print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
            status.set('Logbook imported.')
            time.sleep(1)
            status.clear()
    except:
        print('No file exists')
        status.set('No Log exists...')  
#
def export_log():
    status.set('Exports a new logbook...')
    messagebox.askyesno('Import', 'Export a new logbook?')
    status.clear()
#
def callback():
    status.set('This is a callback...')
    messagebox.showinfo('Info', 'Called the Callback!')
    status.clear()
    
# provide for exiting the program.
def on_closing():
    status.set('This closes the program.')
    if messagebox.askokcancel('Quit', 'Do you want to quit?'):
        root.destroy()
    else:
       status.clear()
# About box information
def About():
    status.set('Program information.')
    messagebox.showinfo(
        'About',
'''Copyright by Kelly Mabry, 2018
Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License. You may obtain a copy of the
License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is
distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
express or implied. See the License for the specific language governing permissions and
limitations under the License.'''
        )
    status.clear()
# set up classes
class StationID():
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
#
class StatusBar(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, bd=1, relief=SUNKEN, anchor=W, font = 'Piboto 12')
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
root.title('KD5AJ logbook')
# Position the root frame on the screen; 800x600 is the size of the form; and 400+100 is
# the position on the screen
root.minsize(1000,750)
root.geometry('800x700+350+0')
#
# Initialize all StringVar(root, value = 'some text')
state_list = ['DX - Non US', 'AK - Alaska', 'AL - Alabama', 'AS - American Samoa', 'AR - Arkansas', 'AZ - Arizona',
                     'CA - California', 'CO - Colorado', 'CT - connecticut', 'DC - District of Columbia', 'DE - Delaware', 'FL - Florida',
                     'FM - Micronesia', 'GA - Georgia', 'GU - Guam', 'HI - Hawaii',  'IA - Iowa', 'ID - Idaho', 'IL - Illinois', 'IN - Indiana',
                     'KS - Kansas', 'KY - Kentucky','LA - Louisiana',  'MA - Massachusetts', 'MD - Maryland','ME - Maine',
                     'MH - Marshall Islands', 'MI - Michigan', 'MN - Minnesota',  'MO - Missouri', 'MS - Missippi', 'MT - Montana',
                     'MP - Northern Marianas',  'NC - North Carolina', 'ND - North Dakota', 'NE - Nebraska', 'NH - New Hampshire',
                     'NJ - New Jersey', 'NM - New Mexico',  'NV - Nevada', 'NY - New York','OH - Ohio', 'OK - Oklahoma', 'OR - Oregon',
                     'PA - Pennsylvania',  'PR - Puerto Rico', 'RI - Rhode Island', 'SC - South Carolina', 'SD - South Dakota', 'TN - Tennessee',
                     'TX - Texas', 'UT - Utah', 'VA - Virginia',  'VI - Virgin Islands', 'VT - Vermont', 'WA - Washington', 'WV - West Virginia',
                     'WI - Wisconson', 'WY - Wyoming']
#
station_id = StringVar(root)
station_id.set('ID every ten minutes.')
state = StringVar(root)
callsign = StringVar(root)
callsign.set('W5XYZ')
power = StringVar(root)
power.set('100')
mode = StringVar(root)
mode.set('A3J')
qso_date_utc = StringVar(root, value = 'UTC Date') #  will be in Y-m-d format for log compatibility

startq = StringVar (root, value = 'Start QSO')
endq = StringVar (root, value = 'End QSO')
# create the menu bar
menu = Menu(root, font = 'Piboto 14')
root.config(menu=menu)
# create file menu
filemenu = Menu(menu, tearoff=0, font = 'Piboto 14')
menu.add_cascade(label='Logbook', menu=filemenu)
#filemenu.add_command(label='New Log', command=callback) # here do a button function
filemenu.add_command(label='Open Log', command=open_log)
#filemenu.add_command(label='Save Log', command=save_log)
filemenu.add_command(label='Close Log', command=close_log)
filemenu.add_separator()
filemenu.add_command(label='Import Log...', command=import_log)
filemenu.add_command(label='Export Log...', command=export_log)
filemenu.add_separator()
filemenu.add_command(label='Import CSV data...', command=import_csv_data)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=on_closing) # call exit window and quit
# create help menu
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About...', command=About, font = 'Piboto 14')

# create a toolbar
toolbar = Frame(root)
#
b_new_log = Button(toolbar, text='New Log', width=10, command=callback, font = 'Piboto 14')
b_new_log.pack(side=LEFT, padx=2, pady=2)
#
b_open_log = Button(toolbar, text='Open Log', width=10, command=open_log, font = 'Piboto 14')
b_open_log.pack(side=LEFT, padx=2, pady=2)
#
b_close_log = Button(toolbar, text='Close Log', width=10, command=close_log, font = 'Piboto 14')
b_close_log.pack(side=LEFT, padx=2, pady=2)
#
b_quit_program = Button(toolbar, text='Quit Program', width=10, command=on_closing, font = 'Piboto 14')
b_quit_program.pack(side=LEFT, padx=2, pady=2)
#
clock = Label(toolbar, font=('Piboto', 18, 'bold'), bg='light grey')
clock.pack(side = RIGHT, fill=X, expand=0)
#
tick()
#
toolbar.pack(side=TOP, fill=X)
#
# create status bar       
status = StatusBar(root)
status.pack(side=BOTTOM, fill=X)
root.update()
#
status.set('Initializing, Please Wait...')
root.after(500)
status.set('Ready...')
root.after(500)
status.set('No Logbook is currently open.')
# Set the panes up here... the listbox is placed and opened in the function 'open'
# m1 is the name of the paned window.
m1 = PanedWindow()
m1.pack(fill='both', expand=1)
#
m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)
#
top = Label(m2, text='', relief = SUNKEN, height = 30, width = 30)
m2.add(top)
#
logdata = Text(m2, font=('Piboto', 14, 'normal'), bg='light grey', height = 5, width =10)
m2.add(logdata)
logdata.config(state='disabled')
#
#Make a log entry grid with in the sub panel, m2
#
start_qso= Button(top, textvariable = startq, command = get_time_begin, font = 'Piboto 16') # use StringVar and pass the button text
start_qso.grid(row= 2, column = 0)
end_qso = Button(top, textvariable = endq, command = get_time_end, font = 'Piboto 16')
end_qso.grid(row= 2, column = 1)
date_qso = Label(top, textvariable = qso_date_utc, font = 'Piboto 16')
date_qso.grid(row= 2, column=2)
#
save_qso = Button(top, text = 'Save QSO', command = save_qso, font = 'Piboto 16')
save_qso.grid(row= 15, column = 1)
save_qso.config(state = 'disabled')
# Provide Labels for entry fields
Label(top, text= 'Station', font = 'Piboto 14', anchor= 'e', width = 12).grid(row=4)
Label(top, text ='Frequency', font = 'Piboto 14', anchor= 'e', width = 12).grid(row=5)
Label(top, text = 'Report Sent', font = 'Piboto 14', anchor= 'e', width = 12).grid(row =6)
Label(top, text = 'Report Recvd', font = 'Piboto 14', anchor= 'e', width = 12).grid(row =7)
Label(top, text='Name', font = 'Piboto 14', anchor= 'e', width = 12).grid(row=8)
#Label(top, text='Last Name', font = 'Piboto 14').grid(row=9)
Label(top, text = 'City', font = 'Piboto 14', anchor= 'e', width = 12).grid(row=10)
Label(top, text = 'State', font = 'Piboto 14').grid(row=12, column =0)
Label(top, text ='Power ', font = 'Piboto 14', anchor= 'e', width = 12).grid(row=4, column = 2)
Label(top, text = 'Mode ', font = 'Piboto 14', anchor= 'e', width = 12).grid(row=5, column = 2)

# Make a couple of check boxes for QSL Sent and QSL Rec.
# Utilize StringVar() to toggle checbox state!!!!
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = 'QSL Sent', font = 'Piboto 14', variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 10, state='normal').grid(row=13, column= 0)
C2 = Checkbutton(top, text = 'QSL Recvd', font = 'Piboto 14',variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 10, state='normal').grid(row=13, column=1)

s_id = Button(top, textvariable = station_id, command = StationID, font = 'Piboto 16') # use StringVar and pass the button text
s_id.grid(row= 13, column = 2)
s_id.config(relief = 'sunken', fg ='green')
#
# Provide entry fields for data
# setup callsign entry, auto capitalization and variable (get())
e1 = Entry(top, textvariable = callsign, font = 'Piboto 14', bg = 'light grey', selectbackground = 'blue', selectforeground ='yellow')
e1.grid(row=4, column=1, padx =5, pady = 5) # Station callsign
e1.focus()
#
#
try:
    # python 3.6
    callsign.trace_add('write', to_uppercase)
except AttributeError:
    # python < 3.6
    callsign.trace('w', to_uppercase)
#
e2 = Entry(top, font = 'Piboto 14',background = 'light grey', selectbackground = 'blue', selectforeground ='yellow')
e2.grid(row=5, column=1) # frequency
#
e2.insert(END, '07.000')
e3 = Entry(top, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') # report sent
e4 = Entry(top, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') #report received 
e5 = Entry(top, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') #Name
#e6 = Entry(top, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') #
e7 = Entry(top, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') # City
e8 = Entry(top, font = 'Piboto 14', background = 'light grey', width = 4, selectbackground = 'blue', selectforeground ='yellow') # power
e8.insert(END, '100')
e9 = Entry(top, font = 'Piboto 14', background = 'light grey', width = 4, selectbackground = 'blue', selectforeground ='yellow') # mode 
e9.insert(END, 'A3J')


state_listbox = Listbox(top, background = 'light grey', selectbackground = 'blue', selectforeground ='yellow', font = 'Piboto 14', selectmode = SINGLE)
for item in state_list:
    state_listbox.insert(END, item)
    state_listbox.grid(row= 12, column =1)
#
#need to find a way to select from a listbox
#
#
e3.grid(row=6, column=1)
e3.insert(END, ' 59')
e4.grid(row=7, column=1)
e4.insert(END, ' 59')
e5.grid(row=8, column =1) # Name
#e6.grid(row=9, column =1)
e7.grid(row=10, column =1)
e8.grid(row = 4, column = 3)
e9.grid(row = 5, column = 3)
#
# Make an entry box for Grid Square

#
# ***completed***
#StationID()
#
root.protocol(on_closing)
root.mainloop()
