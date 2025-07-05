# test-final-tekbot

## 1- Base de données
Exécuter le script schema.sql pour créer la base de données (de préférence MySQL). Si les identifiants de connection sont différents de root et '', modifier dans `__init__.py`.

## 2- Créer un environnement virtuel et l'activer
Se postionner a la racine du projet et exécuter les commandes suivantes
### - Windows
```sh
python -m venv env
./env/Scripts/activate
```
### - Linux
```sh
python3 -m venv env
./venv/bin/activate
```

## 3- Installer les dépendances
```sh
pip install -r requirements.txt
```

## 4- Lancer le projet
```sh
flask --app 'tekbot' run --debug
```

## 5- Routes :
- [localhost:5000](localhost:5000) : pour consulter la page (TekBot/templates/index.html)
- [localhost:5000/set?color={value}](localhost:5000/set?color={value}) : pour stocker la couleur de déchet trié. (value is in [green, yellow, red, blue])