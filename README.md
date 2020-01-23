# Ressource-pour-numbershifting-ALGOSEC

Voici le lien du concours: https://www.codingame.com/multiplayer/optimization/number-shifting

Des rôles sur le discord seront attribués selon votre score. Venez donc prouver que vous saviez manier mieux que personne la programmation ^-^

Si un truc n'est pas clair posez la question sur le discord. Vous pouvez aussi parler du problème entre vous et le faire ensemble. Ou alors juste en parler. Comme vous voulez.

### Explication du problème en français

Le but est de résoudre le plus de puzzle possible. Vous utilisez le langage que vous voulez puisque les codes vont tourner **sur votre machine**. (C'est pas le cas des autres jeux de codingame, et lisp est pas un langage proposé par le site, alors que la vous pourrez utiliser lisp).

Un puzzle est une grille de nombres où il faut rendre tous les nombres de la grille nuls.  
La seule opération disponible consiste à faire glisser (verticalement ou horizontalement) un nombre d'exactement **n** cases si le nombre présent sur la case vaut **n**. Ce nombre doit être glissé vers un autre nombre non nul, et la vous devez choisir si les nombres s'ajoutent ou si ils se soustraient (et dans ce cas la valeur absolue de la soustraction est choisie). Quelque soit l'opération choisie l'endroit d'où part le nombre qui glisse vaut maintenant 0, et l'endroit d'arrivé (comme vu précédement) vaut soit l'addition soit la valeur absolue de la soustraction.

Pour avoir les règles en anglais et avoir une interface graphique qui permets de bien comprendre: https://www.codingame.com/ide/puzzle/number-shifting

Par exemple si vous avez le plateau suivant:
```
0 0 0 1 0
0 0 0 2 1
```
Alors votre seul coup possible est de faire glisser un des deux nombres 1 donc le nombre 2. Vous ne pouvez **pas** faire glisser le nobre 2.

Par exemple faisons glisser celui du haut. Alors je peux me retrouver sur l'un de ces deux plateaux suivant que je choisis d'ajouter ou de soustraire les nombres:
Si je choisis de les additionner j'obtiens le plateau suivant :
```
0 0 0 0 0
0 0 0 3 1
```
Et enfin j'obtiens ce plateau la si je les soustrait :
```
0 0 0 0 0
0 0 0 1 1
```
Enfin si j'avais choisis de les soustraire et que je fait glisser un des 1 contre le deuxième, en choississant encore une fois de soustraire j'obtiens un plateau avec que des 0 et j'ai gagné !

Par contre si j'avais choisi pour mon premier coup de les additionner alors j'ai aucun moyen de gagner.

Encore une fois les règles sont écrites aussi en anglais avec une interface graphique qui permets de bien comprendre comment ça fonctionne: https://www.codingame.com/ide/puzzle/number-shifting

### Pour pouvoir participer au concours

Il faut exécuter ce script puis copier coller la solution du puzzle le plus difficile que vous avez résolu

En gros chaque niveau vous avez un puzzle à résoudre, de plus en plus difficile, et ce script permets de tester votre code sur tous les niveaux. Tant qu'il donne la bonne solution il continue. Et enfin, vous en tant qu'humain pour valider voter score sur codingame vous devez poster la solution du dernier niveau que vous avez résolu sur le site.

Je suis pas l'auteur du script.

Donc pour exécuter le script:

+ D'abord récupérer ce répo:
**git clone https://github.com/symfunc/Number-shift.git**

+ Se placer dans le dossier Number shift: **cd Number-shift**

+ Rentrer ensuite votre email et votre mot de passe de votre compte codingame dans l'entête du fichier submit.py

+ Remplir dans ce même fichier comment lancer votre code. Si par exemple vous avez écrit du python pour répondre au problème et que votre fichier python se nomme mon_fichier.py alors il faudra mettre "python3 mon_fichier.py" dans la variable   *program_execute*. Si par exemple vous créez un executable qui se lance en faisant ./main alors il faudra mettre "./main" dans la variable *program_execute*

+ Lancer votre code: **python3 submit.py**. Ca affiche des liens pour visualiser vos parties et vous indique quand votre solution est incorrecte.

+ Récupérer dans _log.txt_ la solution donnée par votre programme. Ce fichier contient la solution qu'a donné votre programme sur chaque puzzle. Vous devez donc récupérer sa solution pour le dernier puzzle réussi.  
Par exemple le fichier peut ressembler à ça:
```
solution:
first_level
7 4 L +
3 0 D -
6 4 L -
replay: -------------------------

Level 2:
pmkhklcgypoivqgfzyyuvmtsywegacwu
8 5
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 2 0 0 0
0 0 0 0 0 0 0 0
11 0 0 0 6 0 0 7

solution:
pmkhklcgypoivqgfzyyuvmtsywegacwu
7 4 L +
3 0 D -
6 4 L -
```

+ Vous devez maintenant copier coller puis soumettre en PHP sur https://www.codingame.com/ide/puzzle/number-shifting ce qui permets de résoudre le dernier puzzle que vous avez réussit à résoudre. Dans ce tutoriel on a échoué sur le niveau 2 donc il faut copier coller la solution du premier niveau, c'est ce qui suit immédiatement la ligne **solution:**. Il faut donc copier coller (puis soumettre en php) le code suivant :
```
first_level
7 4 L +
3 0 D -
6 4 L -
```

+ Résultat on apparait sur le classement ! On a un score de 1 puisqu'on a résolu seulement le premier puzzle.  
Le but est de résoudre le plus de puzzle possible et d'avoir un score le plus haut possible.  
Mettez devant votre pseudo la chaine de caracètere [symfunc] comme ça on peut facilement trouver tout le monde du serveur sur le classement global.

### Comment faire pour soumettre dans un langage différent ?

Il faut soumettre un code qui affiche la code disponible plus haut. De base PHP affiche le texte qu'on lui donne si on lui dit rien d'autre donc il n'y a rien faire d'autre.

Si on veut soumettre en python ça devient par exemple:
```python
print("""first_level
7 4 L +
3 0 D -
6 4 L -""")
```

### Comment voir le classement de tout le monde du serveur ?

Si tout le monde mets symfunc dans son pseudo on peut voir le classmeent de tout ceux du serveur sur ce lien: https://www.codingame.com/multiplayer/optimization/number-shifting/leaderboard?column=keyword&value=symfunc
