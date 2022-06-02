# Mike Spaans
# opdracht Pizza Calculator
PrijsSmallPizza = 4
PrijsMediumPizza = 7.50
PrijsLargePizza = 11.50
# Hier wordt er gevraagd hoeveel pizza's van elk formaat de klant wilt hebben
SmallPizza = int(input("Hoeveel small pizza's wilt u? "))
MediumPizza = int(input("Hoeveel medium pizza's wilt u? "))
LargePizza = int(input("Hoeveel large pizza's wilt u? "))
# Hier wordt de hoeveelheid pizza's en de prijs van de pizza's naar de terminal geprint
print (SmallPizza , "Small pizza's : " , SmallPizza * PrijsSmallPizza , "euro" )
print (MediumPizza , "Medium pizza's : " , MediumPizza * PrijsMediumPizza , "euro")
print (LargePizza , "Large pizza's : " , LargePizza * PrijsLargePizza , "euro")
# Hier wordt uitgerekend wat de totaal prijzen van elk formaat is 
TotaalSmallPizza = SmallPizza * PrijsSmallPizza
TotaalMediumPizza = MediumPizza * PrijsMediumPizza
TotaalLargePizza = LargePizza * PrijsLargePizza
# Hier wordt naar de terminal geprint hoeveel de totaalprijs kost
print ("Totaal : " , TotaalSmallPizza + TotaalMediumPizza + TotaalLargePizza , "euro")