# OC_Info
Projet Kénan-Farouk


Ce projet consiste à créer un module Python permettant de faire de la stéganographie dans des images. Autrement dit, le programme demandera à l'utilisateur le message qu'il veut dissimué ainsi que l'image qu'il veut utilisé. Et ensuite, le programme rendra la même image (un peu differente de l'intitiale) avec le message à dissimuler à l'interieur.

Mode d'emploi:

Méthode 1 :


Avec script :

Cacher :
1.	Ouvrez le fichier python Cacher.py
2.	Faite run le code.
3.	Vous devez d’abord écrire le message que vous voulez cacher. Attention, chaque charactère de votre message doit être compris dans le petit tableau ascii (jusqu’à 127). Au-delà, il se peut que le message ne puisse pas être caché. Entrezvotre réponse.
4.	Ensuite, on vous demande le nom du fichier de votre image. Ce fichier doit être un fichier png et vous devez bien écrire le nom entier (avec .png). Si vous avec des problèmes, glissez l’image dans le dossier de VisualStudoCode. Entrez votre réponse.
5.	Finalement, écrivez le nom du nouveau fichier png qui enregistrera l’image avec le message caché (avec à nouveau .png à la fin).
6.	Votre message a bien été caché.

Retrouver :
1.	Ouvrez le fichier python retrouver.py
2.	Faite run le code.
3.	Écrivez le nom du fichier png de l’image dont vous voulez retrouver un message caché (avec .png à la fin).
4.	Vous devez normalement recevoir le message caché.


Sans script :

Cacher :

1.	Ouvrez le fichier python Cacher.py
2.	Allez en bas du code et utilisez la fonction cacher_message(image_to_change,message,image_changed) 
3.	Le premier argument est le nom du fichier png de l’image dans laquelle vous voulez cacher un message (avec .png à la fin).
4.	Le deuxième argument est le message que vous voulez caché (avec chaque charactère devant se trouver dans la petite table ascii).
5.	Le troisième argument est le nom que vous voulez attribué au nouveau fichier png dans lequel vous voulez enregistrer l’image avec le message caché.

Retrouver : 
1.	Ouvrez le fichier python retrouver.py
2.	Allez en bas du code et utilisez la fonction decoder_message(image_to_solve)
3.	L’argument image_to_solve est le nom du fichier png de l’image dont vous voulez retrouver un message caché (avec .png à la fin).
4.	Vous êtes sensé recevoir le message qui était caché.



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


Idée : 

Méthode 1:

Cacher, Cacher.py :

1.	Le programme reçoit une image de x pixels de longueur et y pixels de hauteur.
2.	Le programme reçoit un message à cacher sur l’image
3.	Le programme change la valeur R de chaque pixel de l’image en paire.
4.	Chaque caractère du message est assigné à une colonne de pixel de l’image (le premier caractère va être caché sur la premier colonne, le deuxième caractère sur la deuxième colonne, etc.)
5.	Ces caractères vont être converti en valeur numérique x grâce au tableau ascii.
6.	Cette valeur x liée au i-ème caractère du message représente le nombre de pixels de la colonne i de l’image qui auront leur valeur R changée en impair
7.	Donc si le message est ”a“, la première colonne aura x pixels avec une valeur R impaire (avec x la valeur numérique en ascii de a).

Retrouver, retrouver.py : 

1.	Le programme reçoit l’image avec un message caché.
2.	Il va compter le nombre de pixels avec une valeur R impair pour chaque colonne.
3.	Il transformera chacun des résultats trouvés en caractère (string) en utilisant le tableau ascii.
4.	En mettant chacun de ces caractères dans une chaine de caractère, il retrouvera le message caché.





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



Explication de méthodes et algorithmes :

Méthode 1:

Cacher, Cacher.py :

ChangeRGB:
1.	On veut que tout les pixels aient une valeur R pair.
2.	Pour changer toutes le valeurs R en paires, il suffit de prendre les coordonnées (x,y) avec l’ensemble des x possible et l’ensemble des y possible et du parcourir tous ces points.
3.	On va ensuite prendre la valeur R de chaque point.
4.	On vérifie si R est déjà pair en utilisant les modulos, si ce n’est pas le cas, on ajoute 1 à R (pour R = 255, on fait -1).
5.	Et on intègre cette nouvelle valeur R au point (x,y) pour tous les pixels de l’image.
6.	Tout les pixels ont une valeur R pair.

Numerisermessage:
1.	On veut créer une liste avec comme éléments la valeur en ascii de chaque caractère du message dans l’ordre.
2.	Le message en string, on va créer une liste vide.
3.	On parcourt chaque caractère du message et on ajoute à droite de la liste (append) la valeur numérique du ce caractère.
4.	On return cette liste et voilà.

liste_coordonnées_alea:
1.	On veut créer une liste avec x coordonnées aléatoire de y tq : x est la valeur numérique d’un caractère du message et les valeurs de y doivent être compris dans la hauteur de l’image. On répétera ce processus pour chaque caractère du message en obtenant à chaque fois, pour le i-ème caractère du message, une liste avec x élément (x étant la valeur num. en ascii du i-ème élément du message) et chacun de ces élément des valeurs possibles de y différentes.
2.	Il suffit d’utiliser random.sample en créant une liste avec l’ensemble des y possible (donc les entier de l’intervalle [0,hauteur de l’image]) et en donnant le nombre d’éléments à prendre (dans ce cas, x).
3.	Il return cette liste et on peut maintenant cacher le message

cache_nombre_sur_une_colonne:
1.	On veut cacher le message sur une colonne.
2.	Pour la colonne i de l’image, il suffit de prendre la liste des coordonnées y en choisissant comme nombre d’élément la valeur num. en ascii du i-ème caractère du message.
3.	On va ensuite prendre comme coordonnée (i,y) (avec plusieurs y possibles) et à chaque point, ajouter 1 à la valeur R du pixel (donc rendant R pair).
4.	On a donc, pour la i-ème colonne, x valeurs R impair (avec x la valeur num. en ascii du i-ème caractère du message)

cacher_message:
1.	On veut cacher tout le message
2.	Il suffit de répéter l’algorithme d’avant sur toute la longueur du message (i varie donc de 0 à len(message) – 1).
3.	On enregistre ensuite l’image modifiée (avec le message caché) sur un nouveau fichier png.


Retrouver, retrouver.py :

compter_impair_colonne:
1.	On veut compter le nombre d’impair par colonne.
2.	Le programme créer une variable k de valeur 0.
3.	Pour (x,y), on fixe x et on fait varier y sur toute la hauteur de l’image.
4.	Pour chaque point (x,y), on regarde si la valeur R du pixel est pair ou impair avec les modulos.
5.	Si c’est impair, on ajoute 1 à la variable k.
6.	On répète pour tout les y et on trouve le nombre de pixels avec un R impair.

decoder_message:
1.	On veut retrouver le message.
2.	Le programme répète l’algo d’avant pour chaque colonne.
3.	Pour chaque nombre de R impair par colonne, il transforme ce nombre en lettres avec le tableau ascii.
4.	Il suffit d’ajouter chacun de ces caractères sur une nouvelle chaines de caractères.
5.	Lorsque le programme aura parcouru toutes les colonnes, la chaine de caractères sera le message caché.






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

Dimanche 7 janvier, Kénan: début du code des fonctions de test

Lundi 8 janvier, Farouk : mise-à-jour du Readme.md et ajout des docstrings et des fonctions tests.

## toto
