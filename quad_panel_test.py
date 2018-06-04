from tkinter import *

root = Tk()
root.title('Program Name')

root.minsize(400,300)
root.geometry('800x600+400+100')

m1 = PanedWindow(relief = 'ridge', orient=HORIZONTAL, height = 100, width = 100)
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text='left panel', relief = 'ridge', height = 50, width = 50)
m1.add(left)

right = Label(m1, text='right panel', relief = 'ridge')
m1.add(right)

m2 = PanedWindow(relief = 'ridge', orient = VERTICAL, height = 100, width = 100)
m2.pack(fill = BOTH, expand =1)

top = Label(m2, text = 'top panel', relief = 'ridge', height = 10)
m2.add(top)

bottom = Label(m2, text = 'bottom panel', relief = 'ridge', height = 25)
m2.add(bottom)

root.mainloop()