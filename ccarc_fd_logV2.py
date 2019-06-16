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
def tick():
# get UTC date and time from datetime
    now_utc = datetime.now(timezone.utc).strftime('%A %m-%d-%Y %H:%M:%S')
    clock.config(text=now_utc)
    clock.after(200, tick)
#
def resetform():
    date_qso.config(state = 'normal', relief = 'flat')
    start_qso.config(state = 'normal', relief = 'raised')
    end_qso.config(state = 'normal',  relief = 'raised')
    save_qso.config(state = 'disabled')
    clock.config(fg = 'black')
    callsign.set('W1AW')
    e3.delete(0, 'end')
    e3.insert('end', '4A AR')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e5.insert('end', '')
    e4.insert('end', '12E')
    e1.focus()
    startq.set('Start QSO')
    endq.set('End QSO')
    qso_date_utc.set('UTC Date')
    b_close_log.config(state='normal')
#
def save_qso():
	date_qso.config(state = 'normal', relief = 'flat')
	start_qso.config(state = 'normal', relief = 'raised')
	end_qso.config(state = 'normal',  relief = 'raised')
	save_qso.config(state = 'disabled')
	clock.config(fg = 'black')
	new_qso_record.append(qdate)
	new_qso_record.append(qtime_start)
	new_qso_record.append(qtime_end)
	station= e1.get()
	new_qso_record.append(station)
	frq = e2.get()
	new_qso_record.append(frq)
	qrst = e3.get()
	new_qso_record.append(qrst)
	mrst = e4.get()
	new_qso_record.append(mrst)
	state = state_listbox.get(state_listbox.curselection())
	new_qso_record.append(state)
	p = e8.get()
	new_qso_record.append(p)
	m=e9.get()
	new_qso_record.append(m)
	print (new_qso_record)
	with open(logbook, 'a') as filehandle:  
                        for list_item in new_qso_record:
                            filehandle.write('%s ' % list_item)
                        filehandle.write('\n')
                        filehandle.close()
                        new_qso_record.clear()
                        logdata.config(state='normal')
                        logdata.delete(1.0, 'end')
                        try:
                            with open(logbook,'r') as UseFile:
                                logdata.insert('end', UseFile.read())
                        except:
                                print('No file exists')
                        logdata.config(state='disabled')
	callsign.set('W1AW')
	e4.delete(0, 'end')
	e4.insert('end', '12E')
#	e5.delete(0, 'end')
#	e5.insert('end', ' 59')
#	e7.delete(0, 'end') 
#	e7.insert('end', '')
	e1.focus()
	startq.set('Start QSO')
	endq.set('End QSO')
	qso_date_utc.set('UTC Date')
	b_close_log.config(state='normal')
	
def get_time_begin():
    utc_date()
    b_close_log.config(state='disabled')
    get_utc_time = datetime.now(timezone.utc).strftime('%H:%M:%S')
    t = 0
    clock.config(fg = 'blue')
    startq.set(get_utc_time)
    global qtime_start; qtime_start = get_utc_time
    print (qtime_start)
    date_qso.config(state = 'disabled', relief = SUNKEN, disabledforeground= 'green')
    start_qso.config(state = 'disabled', relief = SUNKEN, disabledforeground= 'green')
    
def get_time_end():
    get_utc_time = datetime.now(timezone.utc).strftime('%H:%M:%S')
    t=0
    endq.set(get_utc_time)
    global qtime_end; qtime_end = get_utc_time
    end_qso.config(state = 'disabled', relief = SUNKEN, disabledforeground = 'green')
    save_qso.config(state = 'active')
    clock.config(fg = 'green')
    print (qtime_end)
#
def utc_date():
	get_utc_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
	qso_date_utc.set(get_utc_date)
	global qdate; qdate = get_utc_date
	print (qdate)
	
def close_log():
    if messagebox.askyesno('Close', 'Close the current logbook?'):
        logdata.config(state='normal')
        logdata.delete(1.0, 'end')
        b_open_log.config(state='normal')
        b_new_log.config(state='normal')
        b_close_log.config(state='disabled')
    else:
        pass
#
def create_log():
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
#
def open_log():
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
            logdata.insert('end', UseFile.read())
    except:
        print('No file exists')
        
    logdata.config(state='disabled')
    b_open_log.config(state='disabled')
    b_new_log.config(state='disabled')
    b_close_log.config(state='normal')
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
    try:
        with open(name,'r') as UseFile:
            reader = csv.reader(UseFile, delimiter=',')
            data_csv= list(reader)
            for row in data_csv:
              w.insert('end', row[0:1])
              
        UseFile.close()
    except:
        print('No file exists')
#
def import_log():
    name = askopenfilename(initialdir='/home/pi/',
                           filetypes =(('Log Files', '*.adif'),('Cabrillo Log Files', '*.cabr'),('All Files','*.*')),
                           title = 'Choose a file.'
                           )
    print (name)
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
    
def on_closing():
    if messagebox.askokcancel('Quit', 'Do you want to quit?'):
        root.destroy()
    else:
       pass
#
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
#
#
if __name__ == '__main__':
    # Set up the root frame window.
   root = Tk()
root.title('CCARC WA5CC FD LOG')
# Position the root frame on the screen; 800x600 is the size of the form; and 400+100 is
# the position on the screen
root.minsize(800,700)
root.geometry('800x700+350+0')
#
# Initialize all StringVar(root, value = 'some text')
state_list = ['DX - Non US', 'AK - Alaska', 'AL - Alabama', 'AR - Arkansas', 'AS - American Samoa', 'AZ - Arizona',
                     'EB - East Bay CA', 'LAX - Los Angeles CA', 'ORG - Orange CA', 'SB - Santa Barbara CA',
                     'SCV - Santa Clara Valley CA', 'SDG - San Diego CA', 'SF - San Fransisco CA',
                     'SJV - San Juaquin Valley CA', 'SV - Sacromento Valley CA', 'PAC - Pacific Region California', 'CO - Colorado',
                     'CT - Connecticut', 'DE - Delaware', 'NFL - Florida', 'SFL - Florida', 'FM - Micronesia',
                     'GA - Georgia', 'GU - Guam', 'HI - Hawaii', 'ID - Idaho', 'IL - Illinois','IN - Indiana', 'IA - Iowa', 'KS - Kansas', 'KY - Kentucky',
                     'LA - Louisiana', 'ME - Maine', 'MDC - Maryland DC', 'E. Massachusetts', 'W. Massachusetts',
                     'MH - Marshall Islands', 'MI - Michigan', 'MN - Minnesota', 'MS - Missippi', 'MO - Missouri', 'MT - Montana', 'MP - Northern Marianas',
                     'NE - Nebraska', 'NV - Nevada', 'NH - New Hampshire', 'NNJ - New Jersey', 'SNJ - New Jersey', 'NM - New Mexico',
                     'ENY - New York', 'WNY - New York', 'NLI - New York', 'NNY - New York', 'NC - North Carolina', 'ND - North Dakota', 
                     'OH - Ohio', 'OK - Oklahoma', 'OR - Oregon', 'EPA - Pennsylvania', 'WPA - Pennsylvania', 'PR - Puerto Rico', 'RI - Rhode Island',
                     'SC - South Carolina', 'SD - South Dakota', 'TN - Tennessee', 'NTX - Texas', 'STX - Texas', 'WTX - Texas', 'UT - Utah',
                     'VT - Vermont', 'VA - Virginia',  'VI - Virgin Islands', 'EWA - Washington', 'WWA - Washington', 'WV - West Virginia', 'WI - Wisconson', 'WY - Wyoming',
                     'MAR - Maritime Newfoundland Canada', 'QC - Quebec Canada', 'ON - Ontario Canada', 'MB - Manitoba Canada', 'SK - Saskatchewan Canada',
                     'AB - Alberta Canada', 'BC - British Columbia Canada', 'NWT - Northwest Territories Yukon Canada']
#
state = StringVar(root)
callsign = StringVar(root, 'W1AW')
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
#
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
#
m1 = PanedWindow(relief = 'sunken', orient='horizontal', height = 500, width = 100)
m1.pack(fill='both', expand=1)
m2= PanedWindow(relief ='sunken', orient ='horizontal', height =5, width = 5)
m2.pack(fill='both', expand=1)
#
notes = Text(m2, font=('Piboto', 16, 'normal'), bg='light grey', fg = 'dark blue', selectbackground = 'blue', selectforeground ='yellow', height = 20, width =20,wrap=WORD)
m2.add(notes)
#
logdata = Text(m2, font=('Piboto', 14, 'normal'), bg='light grey', height = 5, width =95, wrap=WORD)
m2.add(logdata)
#
qso_data = Label(m1, text='', relief = 'sunken', height = 450, width = 10)
m1.add(qso_data)
#
bandplan = Label(m1, text ='bandplan', relief ='sunken', height = 450, width = 10)
m1.add(bandplan)
#
usamap = Label(m1, text ='usa map', relief ='sunken', height = 450, width = 10)
m1.add(usamap)
#
photo1 = PhotoImage(file="/home/pi/python_code/band_plan_color.gif")
w1= Label(bandplan, height =765, width =1004, image=photo1)
#
photo2 = PhotoImage(file="/home/pi/python_code/north_america.gif")
w2= Label(usamap, height =765, width =1004, image=photo2)
#
w1.photo = photo1
bands_photo = photo1
w1.pack()
#
w2.photo = photo2
usa_photo = photo2
w2.pack()
#
start_qso= Button(qso_data, textvariable = startq, command = get_time_begin, font = 'Piboto 16')
# use StringVar and pass the button text
start_qso.grid(row= 3, column = 2)
end_qso = Button(qso_data, textvariable = endq, command = get_time_end, font = 'Piboto 16')
end_qso.grid(row= 4, column = 2)
date_qso = Label(qso_data, textvariable = qso_date_utc, font = 'Piboto 16')
date_qso.grid(row= 1, column=2)
#
save_qso = Button(qso_data, text = 'Save QSO', command = save_qso, font = 'Piboto 16')
save_qso.grid(row= 5, column = 2)
save_qso.config(state = 'disabled')
formreset = Button(qso_data, text ='Reset Form', command = resetform, font = 'Piboto 16')
formreset.grid(row= 11, column =2)
# Provide Labels for entry fields
Label(qso_data, text= 'Station', font = 'Piboto 14', anchor= 'e', width = 12).grid(row=1, column =0)
Label(qso_data, text ='Band', font = 'Piboto 14', anchor= 'e', width = 12).grid(row=2, column =0)
Label(qso_data, text = 'Report Sent', font = 'Piboto 14', anchor= 'e', width = 12).grid(row =3, column =0)
Label(qso_data, text = 'Report Recvd', font = 'Piboto 14', anchor= 'e', width = 12).grid(row =4, column =0)
#
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
e2.insert('end', '40M')
e3 = Entry(qso_data, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') # report sent
e4 = Entry(qso_data, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') #report received 
e5 = Entry(qso_data, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') #Name
#e6 = Entry(qso_data, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') #
#e7 = Entry(qso_data, font = 'Piboto 14', background = 'light grey', selectbackground = 'blue', selectforeground ='yellow') # City
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
e3.insert('end', '4A AR')
e4.grid(row=4, column=1)
e4.insert('end', '12E')
e8.grid(row = 6, column = 2)
e9.grid(row = 7, column = 2)
#
root.protocol(on_closing)
root.mainloop()