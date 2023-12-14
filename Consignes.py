"""
Projet Stéganographie
Objectif
Ce projet consiste à créer un module Python permettant de faire de la stéganographie dans des images. Le module devra contenir toutes les fonctions nécessaires pour dissimuler un message et le retrouver.
De plus, le module devra être exécutable en tant que script, et dans ce cas devra demander à l'utilisateur :

le message à dissimuler
le fichier image dans lequel dissimuler le message
le nom du fichier image à utiliser pour sauvegarder l'image contenant le message
Exigences et contraintes générales
Le message a dissimuler sera écrit en utilisant uniquement les caractères du code ASCII.
Les images utilisées seront au format PNG, avec une taille minimum de 500 x 500 pixels et pas de taille maximum.
Le nom de l'image contenant le message devra pouvoir être choisi par l'utilisateur mais s'il ne le fait pas un nom par défaut devra être généré en lien avec le nom de l'image d'origine.
Le projet devra être hébergé sur github et l'enseignant devra être ajouté comme collaborateur (chamblandes-dds).
Le projet contiendra, en plus des fichiers python, un fichier README.md dont la structure est décrite ci-dessous.
Le module devra proposer au moins 2 méthodes originales (i.e. imaginées par vous) pour dissimuler un message dans une image.
Structure du README.md
Bref descriptif du projet en termes d'objectifs et de contenu.
Un mode d'emploi détaillé. Sa lecture doit permettre l'utilisation du module en tant que script ainsi que l'utilisation des fonctions principales permettant de dissimuler et retrouver un message.
Un descriptif des méthodes de stéganographie imaginées (i.e. les algorithmes).
Un descriptif technique de l'implémentation de ces algorithmes. Ce descriptif devra détailler les choix qui auront été faits aussi bien en ce qui concerne les structures de données, leur utilisation, la granularité des fonctions définies et leur organisation.
Un journal de bord concis qui indiquera ce qui a été fait et par qui pour chaque date à laquelle vous avez travaillé sur le projet. Attention le journal de bord est différent des commit, en effet lors d'un cycle de développement classique il devrait y avoir de multiples commit pour chaque avancée ou ajout de fonctionnalité.
Organisation du code
Votre code ne doit comporter que des fonctions sans utilisation de variables globales. Toutes les informations passent par les paramètres et les return.
Chaque fonction contient une docstring qui explique le rôle de la fonction, ses paramètres et leurs types ainsi que ce les éléments retournés et leurs type.
Chaque fonction doit être associée à une fonction de test (cf. Test Driven Development). Si des ressources externes sont nécessaires pour les tests, elles doivent être inclues dans le projet.
Il n'y a aucune interaction avec l'utilisateur hors de l'exécution du module en tant que script.
Deadline, Rendu et Évaluation
Il n'y a pas de rendu, je ferai une copie de votre projet le Lundi 08.01.2024 @20h24 et l'évaluation de votre travail se fera sur la base de cette copie.
L'évaluation se fera en 2 parties ayant la même pondération :

Module fonctionnel et respect des consignes.
Démonstration de votre module, explications d'une des méthode originale et réponse aux questions (10 minutes de présentations + 10 minutes de questions).
"""