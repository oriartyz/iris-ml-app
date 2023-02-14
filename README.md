# iris-ml-app

![Alt text](/iris_img.png)

<br>

## But

Cette application est conçue pour prédire le type de fleur d'Iris en fonction des entrées de l'utilisateur. L'utilisateur peut entrer les longueurs et les largeurs des pétales et des sépales d'Iris et l'application retournera le type de fleur prédit avec une probabilité associée.

## Outils

- Streamlit: une bibliothèque Python pour construire des applications web interactives pour les scientifiques de données et les ingénieurs.
- Pandas: une bibliothèque open source de Python pour manipuler et analyse de données.
- Sklearn: une bibliothèque open source de Python pour les algorithmes d'apprentissage automatique.
- Iris dataset: un jeu de données populaire en apprentissage automatique qui comprend les mesures des pétales et des sépales pour 150 iris différents.
- RandomForestClassifier: un algorithme d'apprentissage automatique supervisé de la bibliothèque scikit-learn pour la classification.

## Étapes

1. Chargement des bibliothèques Streamlit, Pandas et Sklearn.
2. Affichage du titre de l'application et de sa description.
3. Définition de la barre latérale pour les entrées de l'utilisateur.
4. Définition de la fonction `user_input_features` pour prendre en compte les entrées de l'utilisateur sous forme de curseurs pour les longueurs et les largeurs des pétales et des sépales.
5. Chargement du jeu de données Iris et division en données d'entraînement (X) et cibles (Y).
6. Entraînement du modèle RandomForestClassifier en utilisant les données d'entraînement.
7. Prédiction du type de fleur en utilisant les entrées de l'utilisateur.
8. Affichage des étiquettes de classe et de leur numéro d'index correspondant.
9. Affichage de la prédiction et de la probabilité associée.

## Améliorations à venir

1. Ajout d'autres algorithmes d'apprentissage automatique pour comparer les performances.
2. Affichage de graphiques pour visualiser les entrées de l'utilisateur et les résultats de la prédiction.
3. Ajout de fonctionnalités pour charger d'autres jeux de données.
4. Possibilité de sauvegarder les entrées de l'utilisateur et les résultats de la prédiction pour une analyse ultérieure.
