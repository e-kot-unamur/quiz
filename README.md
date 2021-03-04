<h1 align="center">Quizz</h1>
<p align="center">
    <a>
        <img src="https://img.shields.io/website?down_color=red&down_message=down&up_color=brightgreen&style=flat-square&up_message=online&url=https%3A%2F%2Fquizz.e-kot.be" />
    </a>
    <a>
        <img src="https://img.shields.io/github/languages/code-size/e-kot-unamur/quizz.ekot?style=flat-square" />
    </a>
    <a>
        <img src="https://img.shields.io/github/v/tag/e-kot-unamur/quizz.ekot?style=flat-square" />
    </a>
    <a>
        <img src="https://img.shields.io/github/last-commit/e-kot-unamur/quizz.ekot?style=flat-square" />
    </a>
    <a>
        <img src="https://img.shields.io/github/contributors/e-kot-unamur/quizz.ekot?style=flat-square" />
    </a>
</p>

### Démo

Vous pouvez accéder à la dernière version du projet depuis [quizz.e-kot.be](https://quizz.e-kot.be/).

### But 

Proposer une plateforme de quizz pour les collectifs de l'UNamur parce que la licence coutait trop cher à l'AGE.

### Ajouter de nouveaux quizz

**TODO : AJOUT DE QUESTIONNAIRE DEPUIS LE SITE**

Rajouter une clé pour votre quizz dans le fichier *mainQuizz.json* (client/src/json)<br />Rajouter les routes dans *main.py* et dans App.svelte (client/src)<br />

-------

### Lancer l'appli en local :

```bash
py -m venv env #créé un environnement virtuel (pas obligatoire)
env/scripts/activate #entre dans l'environnement
pip install -r requirements.txt	#installe les dépendances
cd ./client
npm i #installe les dépendances
npm run build #permet de build svelte pr le backend
cd ../
py main.py #lance le serveur
```

-------

### Remerciements
Merci titi pour le template du readme. Je t'ai pas demandé, mais il est cool. Bisous
