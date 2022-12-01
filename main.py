# jelszogenerator

'''from fuggvenyek import *


print(jelszogenerator(15, True, True))
'''
from tkinter import *
import fuggvenyek
import objektumok

def rogzites_lap():
        pass

def parameter_lap():
    def jelszokiiras():
        try:
            p.jelszohossz = int(hossz.get())
        except:
            jelszo_ertek['state'] = NORMAL
            jelszo_ertek.delete(1.0, END)
            jelszo_ertek.insert(END, p.jelszo)
            jelszo_ertek.grid(row=1, column=2)
            jelszo_ertek['state'] = DISABLED
            hibaablak = Toplevel(ablak)
            hibaablak.geometry('200x200')
            hibaablak.title('Hibajelzés')
            hibauzenet = Label(hibaablak, text='Számjegyet adjon meg', fg='red', pady=15)
            hibauzenet.grid(row=0)
            ok = Button(hibaablak, text='Bezár', command=hibaablak.destroy, width=10, height=3)
            ok.grid(row=1, sticky=E)
            hibaablak.mainloop()
        else:
            p.van_szamjegy = szamjegy.get()
            p.van_irasjel = irasjel.get()
            p.jelszogenerator()
            jelszo_ertek['state'] = NORMAL
            jelszo_ertek.delete(1.0, END)
            jelszo_ertek.insert(END, p.jelszo)
            jelszo_ertek.grid(row=1, column=2)
            jelszo_ertek['state'] = DISABLED

    cim_cimke = Label(ablak, text='Paraméterek')
    cim_cimke.grid(row=0, column=1)
    jelszo_cimke = Label(ablak, text='A jelszó: ', fg='red')
    jelszo_cimke.grid(row=1, column=0, sticky=E)

    jelszo_ertek = Text(ablak, height=1, width=15, state=DISABLED)
    jelszo_ertek.grid(row=1, column=2)

    jelszo_hossza = Label(ablak, text='A jelszó hossza:')
    jelszo_hossza.grid(row=2, column=0)

    hossz = Entry(ablak, width=3)
    hossz.insert(0, '8')
    hossz.grid(row=2, column=2, sticky=W)

    szamjegy = BooleanVar()
    hossz_pipa = Checkbutton(ablak, text="Kell számjegy?", variable=szamjegy)
    hossz_pipa.grid(row=3, column=0)

    irasjel = BooleanVar()
    irasjel_pipa = Checkbutton(ablak, text="Kell irasjel?", variable=irasjel)
    irasjel_pipa.grid(row=3, column=1)

    lezaro_gomb = Button(ablak, text='Lezárás', command=ablak.destroy)
    lezaro_gomb.grid(row=5, column=2)

    jelszo_gomb = Button(ablak, text='Alkalmazás', command=jelszokiiras)
    jelszo_gomb.grid(row=5, column=0, columnspan=2)

def nevjegy_lap():
    nevjegy_ablak = Toplevel(ablak)
    nevjegy_ablak.title('Programnévjegy')
    programnev = label(nevjegy_ablak, text='Dolgozo Nyilvantartas\n2022 - ver 1.0')
    programnev.pack()
    ok_gomb = Button(nevjegy_ablak, text='OK', command=nevjegy_ablak_destroy)
    ok_gomb.pack()
    nevjegy_ablak.mainloop()

p = objektumok.Dolgozo()

ablak = Tk()
ablak.title('Jelszó generálás')
ablak.minsize(width=200, height=100)

menusor = Menu(ablak)

felvetel = Menu(menusor)

felvetel.add_command(label='Rögzítés', command=rogzites_lap)
felvetel.add_command(label='Parameterek', command=parameter_lap)
felvetel.add_command(label='Kilépés', command=ablak.destroy)

menusor.add_cascade(label='Felvétel', menu=felvetel)

dolgozok = Menu(menusor)

dolgozok.add_command(label='Keresés')
dolgozok.add_command(label='Listázás')
dolgozok.add_command(label='Névjegy', command=nevjegy_lap)

menusor.add_cascade(label='Dolgozok', menu=dolgozok)

ablak.config(menu=menusor)
ablak.mainloop()


