from tkinter import *

root = Tk()
root.title('Program Name')

root.minsize(400,300)
root.geometry('800x600+400+100')
#create first pane; then add left and right sections...
m1 = PanedWindow(relief = 'ridge', orient='horizontal', height = 400, width = 100)
m1.pack(fill=BOTH, expand=1)

qso_data = Label(m1, text='QSO Panel', relief = 'ridge', height = 50, width = 50)
m1.add(qso_data)

log_area = Label(m1, text='Log Panel', relief = 'ridge')
m1.add(log_area)
# create the second panel; add the top and bottom sections....
m2 = PanedWindow(relief = 'ridge', orient = 'horizontal', height = 100, width = 100)
m2.pack(fill = BOTH, expand =1)

notes_area = Label(m2, text = 'Notes Panel', relief = 'ridge', height = 10)
m2.add(notes_area)

bandplan_area = Label(m2, text = 'Band Plan Panel', relief = 'ridge', height = 20)
m2.add(bandplan_area)

root.mainloop()