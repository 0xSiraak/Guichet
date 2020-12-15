import sys

age = input("[*] - Quel âge avez-vous ? ")
depart = input("[*] - À quelle heure souhaitez-vous partir ? ")
kilometre = input("[*] - Quelle distance allez-vous parcourir ? ")

print()

if (int(kilometre) < 10):
    print("[*] - Le tarif de votre billet est de 1.20€")
    x = 1.20
    prix_kilometre = float(x)
elif (int(kilometre) > 10 and int(kilometre) < 25):
    print("[*] - Le tarif de votre billet est de 2.00€")
    x = 2.00
    prix_kilometre = float(x)
elif (int(kilometre) > 25):
    print("[*] - Le tarif de votre billet est de 2.50€")
    x = 2.50
    prix_kilometre = float(x)
elif (int(kilometre) > 50):
    print("[*] - Limit de déplacement suite au confinement, merci de ne pas dépasser les 50 kilomètres")
    sys.exit(0)

if (int(depart) < 7):
    print("[*] - Vous bénéficiez d'une réduction de -5% grâce à votre heure de départ")
    x = -5
    reduction_depart = int(x)
elif (int(depart) > 7 and int(depart) < 10):
    print("[*] - Vous bénéficiez d'une augmentation de +10% à cause votre heure de départ")
    x = +10
    reduction_depart = int(x)
elif (int(depart) > 10 and int(depart) < 16):
    print("[*] - Vous bénéficiez d'aucune réduction grâce à votre heure de départ")
    x = 0
    reduction_depart = int(x)
elif (int(depart) > 16 and int(depart) < 19):
    print("[*] - Vous bénéficiez d'une augmentation de +10% à cause votre heure de départ")
    x = +10
    reduction_depart = int(x)
elif (int(depart) > 19 and int(depart) < 24):
    print("[*] - Vous bénéficiez d'une réduction de -5% grâce à votre heure de départ")
    x = -5
    reduction_depart = int(x)
elif (int(depart) > 24):
    print("[*] - Valeure incorrect, rentrez une heure de départ valide")
    sys.exit(0)

if (int(age) < 10):
    print("[*] - Vous bénéficiez d'une réduction de -15% grâce à votre âge")
    x = -15
    reduction_age = int(x)
elif (int(age) > 64):
    print("[*] - Vous bénéficiez d'une réduction de -10% grâce à votre âge")
    x = -10
    reduction_age = int(x)
else:
    print("[*] - Vous bénéficiez d'aucune réduction grâce à votre âge")
    x = 0
    reduction_age = int(x)
if (int(age) > 90):
    print("[*] - Vous êtes une personne à risque, merci de faire attention à votre santé")
    sys.exit(0)

print("[*] - L'utilisateur bénéficie de {}% avec son heure de départ et de {}% avec son âge sur son ticket d'une valeur de {}€".format(reduction_depart, reduction_age, prix_kilometre))

pourcentage = reduction_age+reduction_depart
pourcentage_total = pourcentage

prix_total = (1+pourcentage_total/100)*prix_kilometre
print("[*] - Une remise de {}% a été effectué, le voyageur payera donc {}".format(pourcentage_total, prix_total))
