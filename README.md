# test-final-tekbot

## 1- Créer un environnement virtuel et l'activer
Se postionner a la racine du projet et exécuter les commandes suivantes
### - Windows
```sh
python -m venv env
./env/Scripts/activate
```
### - Linux
```sh
python3 -m venv env
. ./env/bin/activate
```

## 2- Installer les dépendances
### Windows
```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```
### Linux
```sh
pip install --upgrade pip
pip install -r requirements.txt
```
## 3- Lancer le projet
### En local
```sh
flask --app 'TekBot' run --debug --with-threads
```
### En réseau
```sh
flask --app 'TekBot' run --debug --with-threads --host=0.0.0.0
```

## 4- Routes :
- [localhost:5000](localhost:5000) : pour consulter la page (TekBot/templates/index.html)
- [localhost:5000/api/set?color={value}](localhost:5000/api/set?color={value}) : pour tester le stockage de la couleur de déchet trié. (value is in [green, yellow, red, blue])
- [{ip_address}:5000/api/set?color={value}](ip_address:5000/set?color={value}) : pour stocker de la couleur de déchet trié. A utiliser par le module wifi