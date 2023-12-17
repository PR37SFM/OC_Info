# OC_Info
Projet Kénan-Farouk


Ce projet consiste à créer un module Python permettant de faire de la stéganographie dans des images. Autrement dit, le programme deamndera à l'utilisateur le message qu'il veut dissimué ainsi que l'image qu'il veut utilisé. Et ensuite, le programme rendra la même image avec le message à dissimuler à l'interieur.

Mode d'emploi:
dire comment utiliser:
- le script (entiereté du code)
- comment utiliser fonction qui cache le message
- comment utiliser fonction qui retrouve message

(
1. L'utilisateur doit écrire une chaine caractère représentant le message qu'il veut cacher.
2. L'utilisateur doit donner accès au programme à l'image qu'il souhait utiliser.
3. L'utilisateur doit écrire le nouveau fichier que le programme va créé avec le message dissimulé.
4. Le programme va renvoyer un nouveau fichier (avec le nom choisi par l'utilisateur) avec le message dissimulé à l'interieur.
)


méthode 1:

caché:

1. programme reçoit image
2. programme recolte toutes les valeurs RGB de chaque pixel
3. programme modifie valeur RGB pour qu'elles soient toutes pair
4. porgramme reçoit message
5. programme représente chaque lettre du message en valeur numérique (modulo 26)
6. PS: chaque colonne de l'image représente la n-ième lettre
7. Pour la lettre X de valeur numérique n, on modifiera n pixel en leur donnant des coordonnées impair
8. Fait ça pour chaque lettre (par exemple, si espace, on change rien)
9. renvoie image (message a été caché)

recupéré:

1. programme reçoit image avec message dissimulé
2. programme compte combien de pixel avec coordonnées impair par colonne
3. pour chaque colonne, programme transforme le nombre de coordonnées impair n en lettre X.
4. fait ça pour chaque colonne
5. renvoie l'ensemble des lettres (et donc le message)

(
pixel -> (x,y,z)
(x+1,y,z)
)


méthode 2:




Le module devra contenir toutes les fonctions nécessaires pour dissimuler un message et le retrouver.
De plus, le module devra être exécutable en tant que script, et dans ce cas devra demander à l'utilisateur :

le message à dissimuler
le fichier image dans lequel dissimuler le message
le nom du fichier image à utiliser pour sauvegarder l'image contenant le message

Journal de Bord:

Jeudi 14 décembre, Farouk + Kénan: Début du code. Ajout de fonction changeant la valeur Red de tout les pixels d'une images en valeur pair.

Vendredi 15 décembre, Kénan: Création de 5 fonctions (). Le code qui cache le message marche pour cas particulier

Dimanche 17 décembre, Kénan: definition + ou - clair des docstring de chaque fonction puis passage au cas général avec deux input.

## toto
