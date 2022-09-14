import tkinter as tk

window = tk.Tk()
window.geometry("600x400")
window.title("sollicitatie")

def DierenDressuurVragen():
    PraktijkErvaring = tk.Label(window, text="Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? ")
    PraktijkErvaring.place(x = 10, y= 10)

    DierenDressuur = tk.StringVar()

    PraktijkErvaringAntwoord = tk.Entry(window, textvariable=DierenDressuur)
    PraktijkErvaringAntwoord.place(x = 14, y= 30)
    return DierenDressuur

DierenDressuurVragen()

def JonglerenVragen():
    JongLeren = tk.Label


window.mainloop()