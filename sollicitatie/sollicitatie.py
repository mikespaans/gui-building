PraktijkErvaring = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
Jongleren = int(input("Hoeveel jaar jongleerervaring heeft u? "))
Acrobatiek = int(input("Hoeveel jaar praktijkervarung heeft u met acrobatiek? "))
MboDilpoma = str(input("Bent u in bezit van een MBO-4 Diploma ondernemen? "))
VrachtwagenBewijs = str(input("Bent u in bezit van een geldig Vrachtwagen rijbewijs? "))
HogeHoed = str(input("Bent u in bezit van een hoge hoed? "))
Man = str(input("Bent u een man? "))
if Man == "ja":
    Snor = str(input("Heeft u een snor? "))
    if Snor == "ja": 
        SnorBreedte = int(input("Hoe breed is uw snor? "))
else:
     HaarKleur = str(input("Heeft u rood krulhaar? "))
     if HaarKleur == "ja":
         HaarLengte = int(input("Hoelang is uw haar in centimeters? "))
Lengte = float(input("Hoelang bent u in centimeters? "))
LichaamsGewicht = int(input("Wat is uw lichaamsgewicht in hele kilo's? "))
Certificaat = str(input("Heeft u een certificaat voor overleven met gevaarlijk personeel? "))
Fietsen = str(input("Kunt u fietsen? "))
Skelter = str(input("Heeft u wel eens op een skelter gereden? "))
Zandbak = str(input("Heeft u thuis een zandbak? "))
BalletjesPistool = str(input("Heeft u wel eens met een balletjespistool geschoten? "))

gezakt = 'Helaas u bent niet in aanmerking gekomen voor de sollicitatie'

if (PraktijkErvaring > 4 or Jongleren > 5 or Acrobatiek > 3) and MboDilpoma == "ja" and VrachtwagenBewijs == "ja" and HogeHoed == "ja" and (SnorBreedte > 10 or HaarLengte > 20 ) and Lengte > 150 and LichaamsGewicht > 90 and Certificaat == "ja":
    print ("Gefeliciteerd u mag solliciteren")
else:
    print (gezakt)