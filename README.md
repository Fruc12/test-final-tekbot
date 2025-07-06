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
### En local
```sh
flask --app 'tekbot' run --debug --with-threads
```
### En réseau
```sh
flask --app 'tekbot' run --debug --with-threads --host=0.0.0.0
```

## 5- Routes :
- [localhost:5000](localhost:5000) : pour consulter la page (TekBot/templates/index.html)
- [localhost:5000/set?color={value}](localhost:5000/set?color={value}) : pour tester le stockage de la couleur de déchet trié. (value is in [green, yellow, red, blue])
- [{ip_address}:5000/api/set?color={value}](ip_address:5000/set?color={value}) : pour stocker de la couleur de déchet trié. A utiliser par le module wifi