from tkinter import *
import tkinter
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

def save_qso():
	startq.set('Start QSO')
	endq.set('End QSO')
	qso_date_utc.set('YYYY-mm-dd')
	
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

qso_date_utc = StringVar(root, value = 'YYYY-mm-dd') #  will be in Y m d format for log compatibility

startq = StringVar (root, value = 'Start QSO')
#
endq = StringVar (root, value = 'End QSO')
#

####  Construct 3 pane window
m1 = PanedWindow()
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="left panel", height = 50, width=70, relief=RIDGE)
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Label(m2, text="UTC time & Date", height=15, relief=RIDGE)
m2.add(top)

bottom = Label(m2, text="bottom panel", relief = RIDGE)
m2.add(bottom)
# End of 3 paned window construction.
#
#!!!!!!  Construct entries which are contained in the m2 pane
# Can use grid within these sub-frames!!!
##
clock = Label(m2, justify='center', font=('Times', 10, 'bold'), bg='light grey', fg='black')
clock.grid(row= 0, column = 1, columnspan=2)
#
tick()
#
start_qso= Button(m2, textvariable = startq, command = get_time_begin) # use StringVar and pass the button text
start_qso.grid(row= 2, column = 1)
end_qso = Button(m2, textvariable = endq, command = get_time_end)
end_qso.grid(row= 2, column = 2)
date_qso = Label(m2, textvariable = qso_date_utc)
date_qso.grid(row=2, column=3)

save_qso = Button(m2, text = 'Save QSO', command = save_qso)
save_qso.grid(row= 3, column = 3)
#

#!!!!!!!!!!! end of entries.
mainloop()
