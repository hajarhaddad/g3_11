

Maximisation des Prospects via Programmation Linéaire (Python)

Ce projet a été réalisé dans le cadre du cursus de 3ème année Ingénierie
Informatique et Réseaux à l'EMSI (École Marocaine des Sciences de l'Ingénieur)
pour l'année universitaire 2025-2026.

📋 Description du Projet

L'objectif est d'optimiser la stratégie de communication d'une université pour
ses Journées Portes Ouvertes (JPO). Nous utilisons la programmation linéaire
pour maximiser le nombre de prospects (étudiants potentiels) en respectant des
contraintes de budget, de temps et de volume d'actions.

Le projet traite deux scénarios :

1.  Modèle à 2 variables (Instagram & Radio) résolu par la méthode graphique.
2.  Modèle à 3 variables (Instagram, Radio & Panneaux publicitaires) résolu par
    l'algorithme du Simplexe.

🚀 Fonctionnalités

  - Modélisation mathématique d'un problème d'optimisation.
  - Résolution automatisée avec la bibliothèque Python PuLP.
  - Comparaison des résultats avec le solveur Excel et la méthode manuelle du
    Simplexe.

🛠️ Installation

1.  Assurez-vous d'avoir Python installé sur votre machine.
2.  Installez la bibliothèque de programmation linéaire PuLP via votre terminal
    :

pip install pulp

📈 Modélisation Mathématique (Scénario 2)

Variables de décision :

  - x : Nombre de publications Instagram
  - y : Nombre de spots Radio
  - w : Nombre de Panneaux publicitaires

Fonction Objectif :

Maximiser Z = 40x + 80y + 60w (Nombre total de prospects générés)

Contraintes :

  - Budget : 200x + 1000y + 500w \le 10000 Dh
  - Temps : 1x + 2y + 3w \le 40 heures
  - Volume : x + y + w \le 30 actions
  - Positivité : x, y, w \ge 0

💻 Utilisation

Pour exécuter l'optimisation, lancez le script Python :

# Exemple de résultat attendu dans la console :
--- RÉSULTATS DE L'OPTIMISATION ---
Statut : Optimal
Instagram (x) : 21.875
Radio (y) : 3.846
Panneaux (w) : 3.077
Nombre maximal de prospects : 1415.38

📂 Structure du Projet

  - chapitre1.py : Script Python contenant la résolution avec PuLP de 3 variables.
  - chapitre2.py : Script Python contenant la résolution avec PuLP de 4 variables.
  - README.md : Guide d'utilisation du projet.

👥 Équipe Projet

  - Réalisé par : Haddad Hajar, Ouchen Houda, El Ablaoui Hamza, Maalagh Ayoub.
  - Encadré par : Abdelati REHA & Yassine SAFSOUF.

