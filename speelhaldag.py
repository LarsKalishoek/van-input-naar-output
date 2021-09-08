#input

aantal_mensen = input('Hoeveel mensen  : ')
toegangsticket = 7.45
vip = 0.37
aantal_min = input('Hoeveel minuten x5  : ')
sum1 = int(aantal_min) * 5

#som
print(int(aantal_mensen) * toegangsticket + int(aantal_mensen) * (vip * int(aantal_min)))
prijs = int(aantal_mensen) * toegangsticket + int(aantal_mensen) * (vip * int(aantal_min))

#eindzin

factuurtekst = 'Dit geweldige dagje-uit met ' +str(aantal_mensen) + ' mensen in de Speelhal met ' + str(sum1) + ' minuten VR kost je maar ' + str(prijs)
print (factuurtekst)
