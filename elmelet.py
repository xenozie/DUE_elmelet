from tkinter import *

win = Tk()
win.title('Példa ablak')
win.geometry('600x400')
win.minsize(width=300, height=200)
cimke1 = Label(win, text='Szöveg', fg='blue')
cimke1.pack()
valtozo = StringVar()
valtozo.set('Ez egy masik szoveg')
cimke2 = Label(win, text=valtozo, fg='red')
cimke2.pack()

gomb = Button(win, text='Lezárás', command=win.destroy)
gomb.pack()
mainloop()
