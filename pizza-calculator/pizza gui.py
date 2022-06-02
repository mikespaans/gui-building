import tkinter as tk
from functools import partial
from tkinter.messagebox import showinfo


window = tk.Tk()
window.geometry("400x500")
window.title("pizza calculator")


def AantalPizzaVragen():
    SmallPizza_s = tk.Label(window, text="Hoeveel small pizza's wilt u? ")
    SmallPizza_s.place(x=10, y=10)

    AantalSmallPizza = tk.StringVar()
    HoeveelSmallPizza = tk.Entry(window, textvariable=AantalSmallPizza)
    HoeveelSmallPizza.place(x=14, y= 30)


    MediumPizza_s = tk.Label(window, text="Hoeveel medium pizza's wilt u? ")
    MediumPizza_s.place(x=10, y=60)

    AantalMediumPizza = tk.StringVar()
    HoeveelMediumPizza = tk.Entry(window, textvariable=AantalMediumPizza)
    HoeveelMediumPizza.place(x=14, y= 80)


    LargePizza_s = tk.Label(window, text="Hoeveel large pizza's wilt u? ")
    LargePizza_s.place(x=10, y=110)

    AantalLargePizza = tk.StringVar()
    HoeveelLargePizza = tk.Entry(window, textvariable=AantalLargePizza)
    HoeveelLargePizza.place(x=14, y= 130)

    TotaalKnop = tk.Button(window, command=partial(TotaalBereken, AantalSmallPizza, AantalMediumPizza, AantalLargePizza), text="Betalen")
    TotaalKnop.place(x = 200, y=300, width= 60)

def TotaalBereken(Small, Medium, Large):
    SmallHoeveelHeid = Small.get()
    MediumHoeveelHeid = Medium.get()
    LargeHoeveelHeid = Large.get()

    SmallPrijs = 0
    MediumPrijs = 0
    LargePrijs = 0

    if len(SmallHoeveelHeid) >= 1:
        SmallPrijs = int(SmallHoeveelHeid) * 4
    if len(MediumHoeveelHeid) >= 1:
        MediumPrijs = int(MediumHoeveelHeid) * 7.50
    if len(LargeHoeveelHeid) >= 1:
        LargePrijs = int(LargeHoeveelHeid) * 11.50

    TotaalPrijs = SmallPrijs + MediumPrijs + LargePrijs  

    showinfo("Totaal", "TotaalPrijs: "+str(TotaalPrijs))
    
AantalPizzaVragen()






window.mainloop()
