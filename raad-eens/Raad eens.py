import random
Getal = random.randint(0,1000)
Vraag = 'ja'
AantalKansen = 1
Score = 0
Ronde = 1
Doorgaan = 'nee'


while Vraag == "ja" and AantalKansen <=10 and Ronde <= 20:
    VraagGetal = int(input("Raad het getal "))
    AantalKansen = AantalKansen + 1
    WarmKoud = Getal - VraagGetal
    Warm = VraagGetal - Getal
    if VraagGetal > Getal:
        print ("lager")
    elif VraagGetal < Getal:
        print ("Hoger")

        if WarmKoud <= 50 and WarmKoud > 20 and Ronde <= 20:
            print ("Je bent warm")
        elif WarmKoud <= 20 and WarmKoud > 0:
            print ("Je bent heel warm")

    if Warm <= 50 and Warm > 20:
        print ("Je bent warm")
    elif Warm <= 20 and Warm > 0:
        print ("Je bent heel warm")

    if VraagGetal == Getal:
        print ("Je hebt het getal geraden")
        Score = Score + 1
        print ("Je score is" , Score)
        Doorgaan = 'ja'
    elif AantalKansen >= 11:
        print ("Je kansen zijn op en je hebt het getal niet geraden")
        print ("Je score is" , Score)
        Doorgaan = 'ja'

    if Doorgaan == 'ja':
        Opnieuw = input("Wil je opnieuw ja of nee? ")
        if Opnieuw == "ja": 
            AantalKansen = 1
            Ronde = Ronde + 1
            print ("Ronde" , Ronde)
            Getal = random.randint(0,1000)
        elif Opnieuw == "nee":
            Vraag = 'nee'
            print ("Je bent gestopt in Ronde" , Ronde ,"je score was", Score)