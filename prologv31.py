# !/usr/bin/env/python3
from pathlib import Path
import tkinter
from tkinter import simpledialog
from datetime import datetime, timezone
import tkinter.font
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
# logdate defined at line 450
#
def to_uppercase(*args):
    callsign.set(callsign.get().upper())
    mode.set(mode.get().upper())
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
def stationID():
  pass

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
    id_timer.set('ID Timer started...')
    stid.config(state = 'disabled', relief = 'sunken')
    app = StationTimer()


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
                        logdata.config(state='normal')
                        logdata.delete(1.0, 'end')
                        try:
                            with open(logbook,'r') as UseFile:
                                logdata.insert('end', UseFile.read())
                        except:
                                print('No file exists')
                        logdata.config(state='disabled')
	# End of writing qso to log....
	#Clear the record; reset new_qso_record to empty.
	# clear fields for next qso... callsign, Name and City...leave other pre-entered fields.
	callsign.set('W5XYZ')
	#
	e4.delete(0, 'end')
	e4.insert('end', '')
	e5.delete(0, 'end')
	e5.insert('end', '')
	e7.delete(0, 'end') 
	e7.insert('end', '')
	# return focus back to Callsign field.
	e1.focus()
	# End of form clearing.
	# reset button text
	startq.set('Start QSO')
	endq.set('End QSO')
	qso_date_utc.set('UTC Date')
	#s_id.config(relief = 'sunken', fg ='green')
	#station_id.set('ID every ten minutes.')
	#
	##status.set('Saving contact to logbook...')
	time.sleep(2)
	##status.clear()
	b_close_log.config(state='normal')
	# Remember to use get(). to actually capture the values for the log
	# Capture all the values and then call a function to write the record to the logbook.
	
def get_time_begin():
	# get UTC date and time from datetime
    utc_date()
    ##status.set('Inital QSO date is set...')
    time.sleep(2)
    ##status.clear()
    b_close_log.config(state='disabled')
    get_utc_time = datetime.now(timezone.utc).strftime('%H:%M:%S')
    t = 0
    clock.config(fg = 'blue')
    ##status.set('Inital QSO time is set...')
    time.sleep(2)
    ##status.clear()
    startq.set(get_utc_time)
    global qtime_start; qtime_start = get_utc_time
    #station_id.set('ID Timer Started...')  Name may not be correct
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
    ##status.set('Ending QSO time is set...')
    time.sleep(2)
    ##status.clear()
    print (qtime_end)
#
def utc_date():
	get_utc_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
	qso_date_utc.set(get_utc_date)
	global qdate; qdate = get_utc_date
	##status.set('UTC Date retrieved...')
	time.sleep(2)
	##status.clear()
	print (qdate)
	
def close_log():
    ##status.set('Closes the current logbook...')
    messagebox.askyesno('Close', 'Close the current logbook?')
    logdata.config(state='normal')
    logdata.delete(1.0, 'end')
    #
# New log and open log buttons should become active!
    ##status.set('Logbook Closed.')
    b_open_log.config(state='normal')
    b_new_log.config(state='normal')
    b_close_log.config(state='disabled')
#
def create_log():
    #lets try to enter a filename or at least a callsign example(portable operation...)
    #creates and opens the new log.. let's try WA5CC.. (example)
    call = simpledialog.askstring("Input", "What is your Call Sign?",
                                    parent = root)
    if call is not None:
        print("Your Call Sign is ", call)
        newlog = call + "_logbook.txt"
    else:
       newlog  = "/home/pi/newlog.txt"
    try:
          open(newlog, 'x')
    except FileExistsError:
        b_new_log.config(state='disabled')
        b_open_log.config(state='disabled')
        b_close_log.config(state='normal')
        time.sleep(2)
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
    logdata.config(state='normal')
    logdata.delete(1.0, 'end')
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(logbook,'r') as UseFile:
            #print(UseFile.read())
            logdata.insert('end', UseFile.read())
    except:
        print('No file exists')
        
    logdata.config(state='disabled')
    b_open_log.config(state='disabled')
    b_new_log.config(state='disabled')
    b_close_log.config(state='normal')
    #
    ##status.set(logbook)
#
# Import raw csv data to create a new log.
def import_csv_data():
    #status.set('Imports raw CSV data ...')
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
        time.sleep(2)
    except:
        print('No file exists')
#
def import_log():
    name = askopenfilename(initialdir='/home/pi/',
                           filetypes =(('Log Files', '*.adif'),('Cabrillo Log Files', '*.cabr'),('All Files','*.*')),
                           title = 'Choose a file.'
                           )
    print (name)
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            print(UseFile.read())
            time.sleep(1)
    except:
        print('No file exists')
#
def export_log():
    messagebox.askyesno('Export', 'Export a logbook?')

#
def callback():
    messagebox.showinfo('Info', 'Called the Callback!')
    
# provide for exiting the program.
def on_closing():
    if messagebox.askokcancel('Quit', 'Do you want to quit?'):
        root.destroy()
    else:
       pass
# About box information
def About():
    messagebox.showinfo(
        'About',
'''Copyright by Kelly Mabry, 2019
Licensed under the Apache License, Version 2.0 (the 'License');
you may not use this file except in compliance with the License. You may obtain a copy of the
License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is
distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
express or implied. See the License for the specific language governing permissions and
limitations under the License.'''
        )


if __name__ == '__main__':
    # Set up the root frame window.
   root = Tk()
root.title('Prolog 3.1 - KD5AJ')
# Position the root frame on the screen; 800x600 is the size of the form; and 400+100 is
# the position on the screen
root.minsize(800,700)
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
#station_id = StringVar(root)
#station_id.set('ID every ten minutes.')
state = StringVar(root)
callsign = StringVar(root, 'W5XYZ')
power = StringVar(root, '100')
mode = StringVar(root, 'A3J')
qso_date_utc = StringVar(root, value = 'UTC Date') #  will be in Y-m-d format for log compatibility

startq = StringVar (root, value = 'Start QSO')
endq = StringVar (root, value = 'End QSO')
# create the menu bar
menu = Menu(root, font = 'Piboto 14')
root.config(menu=menu)
# create file menu
filemenu = Menu(menu, tearoff=0, font = 'Piboto 14')
menu.add_cascade(label='Logbook', menu=filemenu)
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
b_new_log = Button(toolbar, text='New Log', width=10, command=create_log, font = 'Piboto 14')
b_new_log.pack(side=LEFT, padx=2, pady=2)
#
b_open_log = Button(toolbar, text='Open Log', width=10, command=open_log, font = 'Piboto 14')
b_open_log.pack(side=LEFT, padx=2, pady=2)
#
b_close_log = Button(toolbar, text='Close Log', width=10, command=close_log, font = 'Piboto 14')
b_close_log.pack(side=LEFT, padx=2, pady=2)
b_close_log.config(state=DISABLED)
#
b_quit_program = Button(toolbar, text='Quit Program', width=10, command=on_closing, font = 'Piboto 14')
b_quit_program.pack(side=LEFT, padx=2, pady=2)
#
clock = Label(toolbar, font=('Piboto', 18, 'bold'), bg='light grey')
clock.pack(side = RIGHT, fill=X, expand=0)
#
toolbar.pack(side=TOP, fill=X)
#
tick()

# create #status bar       
##status = #statusBar(root)
##status.pack(side=BOTTOM, fill=X)
#root.update()
#
##status.set('Initializing, Please Wait...')
#root.after(500)
##status.set('Ready...')
#root.after(500)
##status.set('No Logbook is currently open.')
# Set the panes up here... the Logbook is placed and opened in the function 'open'
# m1 is the name of the paned window.
m1 = PanedWindow(relief = 'sunken', orient='horizontal', height = 50, width = 50)
m1.pack(fill='both', expand=1)
notes = Text(m1, font=('Piboto', 16, 'normal'), bg='light grey', fg = 'dark blue', selectbackground = 'blue', selectforeground ='yellow', height = 20, width =20,wrap=WORD)
m1.add(notes)
#
qso_data = Label(m1, text='', relief = 'sunken', height = 100, width = 10)
m1.add(qso_data)
#
logdata = Text(m1, font=('Piboto', 14, 'normal'), bg='light grey', height = 5, width =95, wrap=WORD)
m1.add(logdata)
#
bandplan = Label(m1, text ='bandplan', relief ='sunken', height = 10, width = 10)
m1.add(bandplan)
#
photo = PhotoImage(file="/home/pi/python_code/band_plan_color.gif")
w = Label(bandplan, height =1110, width =1040, image=photo)
#
w.photo = photo
bands_photo = photo
w.pack()
#
start_qso= Button(qso_data, textvariable = startq, command = get_time_begin, font = 'Piboto 16')
# use StringVar and pass the button text
start_qso.grid(row= 3, column = 2)
end_qso = Button(qso_data, textvariable = endq, command = get_time_end, font = 'Piboto 16')
end_qso.grid(row= 4, column = 2)
date_qso = Label(qso_data, textvariable = qso_date_utc, font = 'Piboto 16')
date_qso.grid(row= 2, column=2)
#
save_qso = Button(qso_data, text = 'Save QSO', command = save_qso, font = 'Piboto 16')
save_qso.grid(row= 5, column = 2)
save_qso.config(state = 'disabled')
# Provide Labels for entry fields
Label(qso_data, text= 'Station', font = 'Piboto 14', anchor= 'e', width = 12).grid(row=1)
Label(qso_data, text ='Frequency', font = 'Piboto 14', anchor= 'e', width = 12).grid(row=2)
Label(qso_data, text = 'Report Sent', font = 'Piboto 14', anchor= 'e', width = 12).grid(row =3)
Label(qso_data, text = 'Report Recvd', font = 'Piboto 14', anchor= 'e', width = 12).grid(row =4)
Label(qso_data, text='Name', font = 'Piboto 14', anchor= 'e', width = 12).grid(row=5)
#Label(qso_data, text='Last Name', font = 'Piboto 14').grid(row=9)
Label(qso_data, text = 'City', font = 'Piboto 14', anchor= 'e', width = 12).grid(row=6)
Label(qso_data, text = 'State', font = 'Piboto 14').grid(row=11, column =0)
Label(qso_data, text ='Pwr ', font = 'Piboto 14', anchor= 'w', width = 12).grid(row=6, column = 2)
Label(qso_data, text = 'M ', font = 'Piboto 14', anchor= 'w', width = 12).grid(row=7, column = 2)
#
# Provide entry fields for data
# setup callsign entry, auto capitalization and variable (get())
e1 = Entry(qso_data, textvariable = callsign, font = 'Piboto 14', bg = 'light grey', selectbackground = 'blue', selectforeground ='yellow')
e1.grid(row=1, column=1, padx =5, pady = 5) # Station callsign
e1.focus()
try:
    callsign.trace_add('write', to_uppercase)
except AttributeError:
    callsign.trace('w', to_uppercase)
#
e2 = Entry(qso_data, font = 'Piboto 14',background = 'light grey', selectbackground = 'blue', selectforeground ='yellow')
e2.grid(row=2, column=1) # frequency
e2.insert('end', '07.200')
e3 = Entry(qso_data, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') # report sent
e4 = Entry(qso_data, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') #report received 
e5 = Entry(qso_data, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') #Name
#e6 = Entry(qso_data, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') #
e7 = Entry(qso_data, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') # City
e8 = Entry(qso_data, font = 'Piboto 14', background = 'light grey', width = 4, selectbackground = 'blue', selectforeground ='yellow') # power
e8.insert('end', '100')
e9 = Entry(qso_data, font = 'Piboto 14', background = 'light grey', width = 4, selectbackground = 'blue', selectforeground ='yellow') # mode 
e9.insert('end', 'A3J')
state_listbox = Listbox(qso_data, background = 'light grey', selectbackground = 'blue', selectforeground ='yellow', font = 'Piboto 14', selectmode = SINGLE)
for item in state_list:
    state_listbox.insert('end', item)
    state_listbox.grid(row= 11, column =1)
#
e3.grid(row=3, column=1)
e3.insert('end', ' 59')
e4.grid(row=4, column=1)
e4.insert('end', ' 59')
e5.grid(row=5, column =1) # Name
e7.grid(row=6, column =1)# City
e8.grid(row = 6, column = 2)
e9.grid(row = 7, column = 2)
#
root.protocol(on_closing)
root.mainloop()
