from tkinter import *
import tkinter
from datetime import datetime, timezone
import time
#
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

def save_qso():
	startq.set('Start QSO')
	endq.set('End QSO')
	qso_date_utc.set('UTC Date')
	
	date_qso.config(state = 'normal')
	start_qso.config(state = 'normal')
	end_qso.config(state = 'normal')
	save_qso.config(state = 'disabled')
	
# Remember to use get(). to actually capture the values for the log
# all i have done is to set the labels.
def get_time_begin():
	# get UTC date and time from datetime
    get_utc_time = datetime.now(timezone.utc).strftime('%H:%M:%S')
    #
    # strftime('%A %m-%d-%Y %H:%M:%S')
    startq.set(get_utc_time)
    get_utc_date()
    date_qso.config(state = 'disabled')
    start_qso.config(state = 'disabled')
    

def get_time_end():
	# get UTC date and time from datetime
    get_utc_time = datetime.now(timezone.utc).strftime('%H:%M:%S')
    endq.set(get_utc_time)
    end_qso.config(state = 'disabled')
    save_qso.config(state = 'active')
    C1.config(state = 'active')
    C2.config(state = 'active')

def get_utc_date():
	get_utc_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
	qso_date_utc.set(get_utc_date)

if __name__ == '__main__':
    # Set up the root frame window.
   root = Tk()
root.title('UTC Time & Date')
#
root.minsize(100,100)
root.geometry('200x200+400+100')

# Initialize all StringVar(root, value = 'some text')
state = StringVar(root)
power = StringVar(root)
qso_date_utc = StringVar(root, value = 'UTC Date') #  will be in Y m d format for log compatibility

startq = StringVar (root, value = 'Start QSO')
#
endq = StringVar (root, value = 'End QSO')
#

####  Construct 3 pane window
m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text='Display log', height = 50, width=70, relief=RIDGE)
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Label(m2, text='', height=15, relief=RIDGE)
m2.add(top)

bottom = Label(m2, text='Clock', relief = RIDGE)
m2.add(bottom)
# End of 3 paned window construction.
#
#!!!!!!  Construct entries which are contained in the m2 pane
# Can use grid within these sub-frames!!!
##
clock = Label(bottom, justify='right', font=('Arial', 10, 'bold'), bg='light grey', fg='black')
clock.grid(row= 1, column = 1, columnspan=2)

#
tick()
#
start_qso= Button(top, textvariable = startq, command = get_time_begin) # use StringVar and pass the button text
start_qso.grid(row= 2, column = 0)
end_qso = Button(top, textvariable = endq, command = get_time_end)
end_qso.grid(row= 2, column = 1)
date_qso = Label(top, textvariable = qso_date_utc)
date_qso.grid(row= 2, column=2)
#
save_qso = Button(top, text = 'Save QSO', command = save_qso)
save_qso.grid(row= 15, column = 1)
# Provide Labels for entry fields
Label(top, text= 'Station').grid(row=4)
Label(top, text ='Frequency').grid(row=5)
Label(top, text = 'Report Sent').grid(row =6)
Label(top, text = 'Report Recvd').grid(row =7)
Label(top, text='First Name').grid(row=8)
Label(top, text='Last Name').grid(row=9)
Label(top, text = 'City').grid(row=10)
Label(top, text = 'State').grid(row=4, column =2)
Label(top, text ='Power').grid(row=12)

# Make a couple of check boxes for QSL Sent and QSL Rec.
# Utilize StringVar() to toggle checbox state!!!!
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text = 'QSL Sent', variable = CheckVar1, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 10, state='normal').grid(row=13, column= 0)
C2 = Checkbutton(top, text = 'QSL Recvd', variable = CheckVar2, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 10, state='normal').grid(row=13, column=1)
                 
             
# ***completed***
# Provide entry fields for data
e1 = Entry(top)
e2 = Entry(top)
e3 = Entry(top)
e4 = Entry(top)
e5 = Entry(top)
e6 = Entry(top)
e7 = Entry(top)
#e8 = Entry(top)


state_id= OptionMenu(top, state, 'AK - Alaska', 'AL - Ala', 'AR - Ark', 'AS - A. Samoa','AZ - Ariz', 'CA - Calif.', 'CO - Colo', 'CT', 'DC', 'DE',' FL',
).grid(row= 5, column =2)
pwr = OptionMenu(top, power, '100', '50', '25', '5').grid(row=12, column=1)

# Place entry boxes in grid format
e1.grid(row=4, column=1)
e2.grid(row=5, column=1)
e2.insert(END, '50.125')
e3.grid(row=6, column=1)
e3.insert(END, '59')
e4.grid(row=7, column=1)
e4.insert(END, '59')
e5.grid(row=8, column =1)
e6.grid(row=9, column =1)
e7.grid(row=10, column =1)
#e8.grid(row=11, column =1)

mainloop()
