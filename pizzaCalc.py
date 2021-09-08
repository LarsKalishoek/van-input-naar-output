#Lars Kalishoek pizzacalc
#pizza sizes

small = input('Hoeveel small pizzas wilt u,  twv $6  :')
medium = input('Hoeveel medium pizzas wilt u, twv $12  :')
large = input('Hoeveel large pizzas wilt u, twv $16  :')

#prijs berekenen
prijs1 = int(small) * 6
prijs2 = int(medium) * 12
prijs3 = int(large) * 16

prijs = prijs1 + prijs2 + prijs3

#eindzin

factuurtekst = 'U heeft ' + str(small) + ' small pizzas ' + str(medium) + ' medium pizzas ' + str(large) + ' large pizzas het totale bedrag dat u moet betalen is : $' + str(prijs)
print (factuurtekst)