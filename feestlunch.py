#user input
croissantjes = input('Hoeveel croissants  :')
prijsC = 0.39
stokbrood = input('Hoeveel stokbroden  :')
prijsS = 2.78 
kortingsbonnen = input('Hoeveel kortingsbonnen  :')
korting = 0.50

#prijs berekenen

print(int(croissantjes) * prijsC + int(stokbrood) * prijsS - int(kortingsbonnen) * korting)
prijs = int(croissantjes) * prijsC + int(stokbrood) * prijsS - int(kortingsbonnen) * korting

#eind zin

factuurtekst = 'De feestlunch kost je bij de bakker ' + str(prijs) + ' euro' 'voor de ' + str(croissantjes) + ' croissantjes en de ' + str(stokbrood) + ' stokbroden als de ' + str(kortingsbonnen) + ' kortingsbonnen nog geldig zijn!'
print(factuurtekst)