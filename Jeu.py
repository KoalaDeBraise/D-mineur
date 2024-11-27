from Système import système
from Grille import grille
from Case import case
from Titre import titre

Titre = titre()
Titre.Bienvenue()

a = 0
b = input('Veuillez choisir la difficulté (numéro): ')
if b == '1':
    a = 9
else:
    if b == '2':
        a = 16
    else:
        if b == '3':
            a = 50
        else:
            print('Désolé, veuillez relancer le programme!')
            quit()

taille = (a, a)
proba = 0.1
Grille = grille(taille, proba)
écranT = (800,800)
jouer = système(Grille, écranT)
jouer.jouer()

