import tkinter as tk
import random
from functools import partial
from tkinter.messagebox import showinfo
from tkinter.messagebox import askretrycancel

window = tk.Tk()
window.geometry("400x300")
window.title("Getal Raden")
window.configure(background="lightgrey")

Rondes = 1
KansenRonden = 0

def GetalGeneren():
    

    RandomGetal = random.randint(0,1000)
    return RandomGetal

Getal = GetalGeneren()

def GetalInvoeren(RandomGetal):
    RaadHetGetal = tk.Label(window, text="Raad het getal", background="lightgrey")
    RaadHetGetal.place(x=150, y=50)

    IngevoerdeGetal = tk.StringVar()
    GetalInvullen = tk.Entry(window, textvariable=IngevoerdeGetal)
    GetalInvullen.place(x=154, y=70, width=75)

    GetalCheck = tk.Button(window, text="Getal Checken", command=partial(GetalControleren, IngevoerdeGetal, RandomGetal))
    GetalCheck.place(x=150, y=130)


def GetalControleren(IngevuldeGetal, randomGetal):
    global KansenRonden
    global Rondes
    Getal = IngevuldeGetal.get()
    print (randomGetal)
    KansenRonden += 1
    if KansenRonden <= 10 and Rondes <= 20:
        if int(Getal) > randomGetal:
            Warm = int(Getal) - randomGetal
            if Warm >= 20 and Warm <= 50:
                showinfo("", "je bent warm, Lager")
            elif Warm > 0 and Warm <= 20:
                showinfo("", "je bent heel warm, Lager")
            else:
                showinfo("", "Lager")

        elif int(Getal) < randomGetal:
            Warm = randomGetal - int(Getal)
            if Warm >= 20 and Warm <= 50:
                showinfo("", "je bent warm, Hoger")
            elif Warm > 0 and Warm <= 20:
                showinfo("", "je bent heel warm, Hoger")
            else:
                showinfo("", "Hoger")
        else:
            OpnieuwSpelen = askretrycancel("Opnieuw", "Je hebt het getal geraden! Wil je Opnieuw Spelen?")
            Rondes += 1
            if OpnieuwSpelen == True:
                KansenRonden = 0
                Getal = GetalGeneren()
                GetalInvoeren(Getal)
    else:
        showinfo("", "je kansen zijn op het spel stopt.")
        window.destroy()


GetalInvoeren(Getal)

window.mainloop()