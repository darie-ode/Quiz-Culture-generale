# 📚   Quiz-Culture-generale

Ce projet est une **application interactive de quiz à choix multiples** développée en Python avec l'interface graphique Tkinter. Elle permet à un joueur de tester ses connaissances en répondant à une série de questions dans un temps limité.


## 📦 À propos du projet

Langage : Python

Interface : Tkinter

Type : Application locale

Objectif : Apprentissage du développement d’interfaces graphiques et de la logique de jeu éducatif.


## 🗃️ Structure du projet (fichiers importants)

- `main.py` : code principal de l'application
- `json_utils.py` : fonctions pour gérer les fichiers JSON
- `questions.json` : liste des questions du quiz
- `results.json` : généré automatiquement pour stocker les résultats
- `README.md` : documentation



## 🎮 Comment ça marche ?

### Déroulement du quiz
- L'utilisateur entre son nom pour démarrer une session.
- Chaque question est affichée avec plusieurs réponses possibles.
- L'utilisateur doit choisir la bonne réponse dans un temps limité (20 secondes).
- À la fin du quiz, le score est affiché avec un message personnalisé selon la performance.

### Fonctionnalités principales
- Interface graphique via Tkinter.
- Gestion d’un **compte à rebours** par question.
- Validation de la réponse et passage automatique à la question suivante.
- Sauvegarde des résultats dans un fichier local.
- Affichage de l’historique des résultats.


## 🚀 Lancer l’application
**Pré-requis**

Python 3 installé sur la machine.

Module tkinter (souvent inclus de base).

**Commande pour lancer l'application**

python3 main.py


## 🧪 Exemple de partie

1. L'utilisateur clique sur **"Jouer au quiz"**.
2. Il saisit son **prénom**.
3. Il répond aux **10 questions** proposées, chaque question étant chronométrée.
4. À la fin, il voit son **score** accompagné d’un message :
   - 🎉 "Félicitations" pour un bon score
   - 👍 "Bien joué"
   - 😕 "Peut mieux faire" si le score est faible
5. Il peut aussi **consulter l’historique des scores** enregistrés automatiquement.



⚠️ Ce projet ne contient pas de version web. Pour une version utilisable dans un navigateur, voir le projet quiz-html.

