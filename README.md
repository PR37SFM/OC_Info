# OC_Info
Projet Kénan-Farouk


Ce projet consiste à créer un module Python permettant de faire de la stéganographie dans des images. Autrement dit, le programme demandera à l'utilisateur le message qu'il veut dissimué ainsi que l'image qu'il veut utilisé. Et ensuite, le programme rendra la même image (un peu differente de l'intitiale) avec le message à dissimuler à l'interieur.

Mode d'emploi:


méthode 1:

cacher:
1. Ouvrir fichier python nommé "Cacher.py"
2. Executer le code et suivre ordres.
3. Si l'utilisateur souhaite utiliser la fonction qui cache un message dans une image tout seul, utiliser la fonction nommée "cacher_messager" (lire sa docstring)

retrouver:
1. Ouvrir fichier python nommé "retrouver.py"
2. Executer et suivre ordres
3. Si l'utilisateur souhaite utiliser la fonction qui retrouver le message caché tout seul, utiliser la fonction nommée "decoder_message" (voir sa docstring)


méthode 2:

cacher:
1. Ouvrir fichier python nommé "Encrypt_03.py"
2. Entrer le path de l'image, ainsi que le message.
3. Entrer le nouveau nom de l'image avec le message à l'interieur (optionnel).
4. Ouvrir le fichier image qui est déposé au même endroit que l'image initiale.

retrouver:
1. Ouvrir fichier python nommé "Encrypt_03.py"
2. Entrer le path de l'image.
3. Si le terminal indique 'pas de message', la mauvaise image a été inseré, alors relancer le programme en indiquant la bonne image.




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

Encrypt_03:

1. Le programme demande le path de l'image et y accède. S'il ne l'a pas trouvé, il le redemande.
3. Le programme demande un message à dissimuler et le reçoit. S'il reçoit un message trop long ou trop court, il le redemande.
4. Le programme demande un nom à l'image dans lequel sera dissimuler le message. S'il ne recoit rien, il renomme lui-même l'image.
5. Le programme prépare le path où sera déposé le fichier image.
6. Le programme ajoute le caractère [NULL] en ASCII au message.
7. Le programme convertit le message, caractère par caractère, en valeur ASCII, puis en binnaire, ce qui va donner un octet pour chaque caractère.
8. Le programme prend la valeur Blue d'un pixel et, en fonction de chaque bit de l'octet, la rend/garde pair s'il s'agit de '0' ou la rend/garde impair s'il s'agit de '1'.
9. Le programme remplace le pixel traité par le même pixel avec la couleur bleu traité.
10. Le programme traite pixel par pixel, en commençant (0;0) et en progressant sur l'horizontale, puis s'il arrive au bout, passe à la ligne horizontale au-dessous.
11. Le programme arrête de progresser quand tout les caractères du message ont été traitées.
12. Le programme renvoie l'image avec le message dissimulé.

Decrypt_03:

1. Le programme demande le path de l'image et y accède. S'il ne l'a pas trouvé, il le redemande.
2. Le programme prend la valeur Blue d'un pixel et, en fonction de sa parité, determine le bit '0' ou '1', jusqu'à former un octet.
3. Le programme transforme l'octet en ASCII, puis en caractère, et recommence pour le prochaine octet, jusqu'à que celui-ci indique la valeur binaire du caractère [NULL] de ASCII.
4. Le programme traite pixel par pixel, en commençant (0;0) et en progressant sur l'horizontale, puis s'il arrive au bout, passe à la ligne horizontale au-dessous.
5. Le programme imprime le message qu'il a trouvé, sauf s'il n'a pas trouvé le caractère [NULL] de ASCII.

Journal de Bord:

Jeudi 14 décembre, Farouk + Kénan: Début du code. Ajout de fonction changeant la valeur Red de tout les pixels d'une images en valeur pair.

Vendredi 15 décembre, Kénan: Création de 5 fonctions (à remplir). Le code qui cache le message marche pour les cas qui lui ont été atribué (toujours pas d'input). Codage du programme qui retrouve le message. Il marche quand on le met dans le même fichier .py mais pas dans le nouveau, on reviendra la dessus.

Dimanche 17 décembre, Kénan: definition + ou - clair des docstrings de chaque fonction puis passage au cas général avec deux inputm pour le programme qui permet de caché le message. 

Jeudi 21 décembre, Kénan: changement de jpeg à png. Resolution du programme avec le fichier retrouvr.py -> le code qui permet de retrouver le message fonction.

Dimanche 25 décembre, Kénan: ajout de l'input qui permet à l'utilisateur de choisir le nom du fichier modifier (dans le code cacher.py) et ajout de l'input dans le code retrouver.py

Dimanche 31 décembre, Farouk + Kénan : discussion deuxième méthode
                      Farouk : début et documentation sur la méthode n°2

Lundi 1 janvier, Farouk : continuation du code avec création de 4 fonction pour cacher le message et le retrouver.

Mardi 2 janvier, Farouk : continuation du code avec création de la limite de lecture du programme et du message (caractère [NULL] de ASCII) + création des inputs pour l'encryptage
                          + plusieurs essais et test des cas limites.

Dimanche 7 janvier, Farouk : leger changement du code et revision du contenu.

Lundi 8 janvier, Farouk : mise-à-jour du Readme.md et ajout des docstrings et des fonctions tests.

## toto
