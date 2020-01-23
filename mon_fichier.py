largeur, hauteur  = [int(i) for i in input().split()]

grille = []
for _ in range(hauteur):
	ligne = [int(i) for i in input().split()]
	grille.append(ligne)

#La variable grille contient le terrain la
#Vous en faites ce que vous voulez pour trouver la solution


#Une fois ceci fait vous affichez votre liste de coups
#Voici la solution pour le premier niveau
print("7 4 L +")
print("3 0 D -")
print("6 4 L -")
