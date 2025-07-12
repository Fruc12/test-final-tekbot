import sqlite3
from flask import Blueprint, redirect, render_template, request, url_for
bp = Blueprint('controller', __name__)

# Fonction de connection a la base de données SQLite
def connect():
    return sqlite3.connect("db.sqlite3")

# Fonction pour insérer une couleur dans la base de données
# Cette fonction est appelée par les routes pour enregistrer la couleur choisie
def set_value(color):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO `colors`(`color`) VALUES ('{color}')")
    connection.commit()
    connection.close()

# Fonction pour récupérer les valeurs des couleurs depuis la base de données
# Elle retourne le nombre d'occurrences de chaque couleur spécifiée
def get_values():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT color, COUNT(*) AS total
        FROM colors
        WHERE color IN ('green', 'yellow', 'red', 'blue')
        GROUP BY color
    """)
    colors = cursor.fetchall()
    connection.close()
    
    green = yellow = red = blue = 0
    for color, count in colors:
        if color == "green": green = count
        if color == "yellow": yellow = count
        if color == "red": red = count
        if color == "blue": blue = count
        
    return green, yellow, red, blue

# Routes pour afficher la page principale et gérer les requêtes de changement de couleur
@bp.get("/")
def render_page():
    green, yellow, red, blue = get_values()            
    return render_template("index.html", green=green, yellow=yellow, red=red, blue=blue)


@bp.get("/set")
def save_color_web():
    color = request.args.get("color")
    if color in ['green', 'yellow', 'red', 'blue'] :
        set_value(color)
    return redirect(url_for("render_page"))

# 
@bp.get("/api/set")
def save_color_api():
    color = request.args.get("color")
    headers = {
        "Content-Type": 'application/json',
    }
    if color in ['green', 'yellow', 'red', 'blue'] :
        set_value(color)
        response = {
            'success':True,
        }
        return (response, 201, headers)
    elif color != None:
        response = {
            'success':False,
            'message': "Couleur non valide. Utilisez 'green', 'yellow', 'red' ou 'blue'."
        }
        return (response, 422, headers)
    else:
        green, yellow, red, blue = get_values()
        response = {
            'success':True,
            'message': 'Donées récupérées avec succès.',
            'data': {
                'green': green,
                'yellow': yellow,
                'red': red,
                'blue': blue
            }
        }
        return (response, 200, headers)

# Initialisation de la base de données
# Cette partie crée la base de données et la table si elles n'existent pas déjà
connection = connect()
cursor = connection.cursor()
with open('schema.sql') as f:
    cursor.executescript(f.read())  
connection.close()