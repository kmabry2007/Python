from tkinter import *
from tkinter import messagebox

def on_close():
    root.destroy()

def fwl():
    f1 = e1.get()
   #get value from entrybox
    print(f1)
    freq = float(f1)
    length = 1005/freq
    # convert length from float to string.
    L = format(length, '.7g')  # give 12 significant digits
    print(L)
    # print result in a messagebox
    messagebox.showinfo('Length in feet', L)


def hwd():
    f1=e1.get()
    print(f1)
#get...
    freq = float(f1)
    length = 468/freq
    # convert length from float to string.
    L = format(length, '.7g')  # give 12 significant digits
    print(L)
    # print result in a messagebox
    messagebox.showinfo('Length in feet', L)

	

if __name__ == '__main__':
    # Set up the root frame window.
   root = Tk()
root.title('Antenna Calculator')
# Position the root frame on the screen; 800x600 is the size of the form; and 400+100 is
# the position on the screen
root.minsize(200,100)
root.geometry('200x200+400+100')
#
L1=Label(root, text = 'Enter frequency in MHZ')
L1.grid(row = 0, column = 0)
e1=Entry(root, bd=5)
e1.insert(END, '50.125')
e1.grid(row =1, column = 0)

b1=Button(root, text = 'FWLoop', command = fwl )
b2=Button(root, text= 'HWDipole', command= hwd)
b1.grid(row =2, column =0)
b2.grid(row =3, column = 0)
#
b3=Button(root, text= 'Quit', command= on_close)
b3.grid(row=5, column = 0)
root.mainloop()