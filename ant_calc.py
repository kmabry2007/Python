from tkinter import *
from tkinter import messagebox



def fwl():
	print('hello')
   #get value from entrybox

def hwd():
	print('hi')
	#get...

if __name__ == '__main__':
    # Set up the root frame window.
   root = Tk()
root.title('Program Name')
# Position the root frame on the screen; 800x600 is the size of the form; and 400+100 is
# the position on the screen
root.minsize(100,100)
root.geometry('200x200+400+100')
#
freq =StringVar()
L1=Label(root, textvariable =freq)
L1.pack(side= 'left''')
e1=Entry(root, bd=5)
e1.pack(side= 'left')
#
b1=Button(root, text = 'FWLoop', command = fwl )
b2=Button(root, text= 'HWDipole', command= hwd)
b1.pack(side = 'left')
b2.pack(side= 'left')
#
freq.set('Enter frequency in MHZ')
root.mainloop()
