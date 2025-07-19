import sqlite3
from flask import Blueprint, render_template, request
bp = Blueprint('controller', __name__)

# Fonction de connection a la base de données SQLite
def connect() :
    return sqlite3.connect("db.sqlite3")

# Fonction pour insérer une nouvelle couleur et le niveau de batterie dans la base de données
def set_value(color, battery=0) :
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO `colors`(`color`, `battery`) VALUES ('{color}', {battery})")
    connection.commit()
    connection.close()

# Fonction pour récupérer les nombres de couleurs et le niveau de batterie
def get_values() :
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT color, COUNT(*) AS total
        FROM colors
        WHERE color IN ('green', 'yellow', 'red', 'blue')
        GROUP BY color
    """)
    colors = cursor.fetchall()
    cursor.execute("SELECT battery FROM colors ORDER BY id DESC LIMIT 1")
    battery = cursor.fetchone()
    battery = battery[0] if battery else 0
    connection.close()
    
    green = yellow = red = blue = 0
    for color, count in colors:
        if color == "green": green = count
        if color == "yellow": yellow = count
        if color == "red": red = count
        if color == "blue": blue = count
        
    return green, yellow, red, blue, battery

# Routes pour afficher la page principale
@bp.get("/")
def render_page() :
    green, yellow, red, blue, battery = get_values()            
    return render_template("index.html", green=green, yellow=yellow, red=red, blue=blue, battery=battery)

# Route pour l'actualisation des données sur la page principale
@bp.get("/api/get")
def get_data() :
    green, yellow, red, blue, battery = get_values()
    headers = {
        "Content-Type": 'application/json',
    }
    response = {
        'success': True,
        'message': 'Données récupérées avec succès.',
        'data': {
            'green': green,
            'yellow': yellow,
            'red': red,
            'blue': blue,
            'battery': battery
        }
    }
    return (response, 200, headers)

# Route pour enregistrer les données de couleur et de niveau de batterie
@bp.get("/api/set")
def save_data() :
    color = request.args.get("color")
    battery = request.args.get("battery", type=int)
    headers = {
        "Content-Type": 'application/json',
    }
    if color in ['green', 'yellow', 'red', 'blue'] and battery != None and 0 <= battery <= 100 :
        set_value(color, battery)
        response = {
            'success' : True,
        }
        return (response, 201, headers)
    else :
        response = {
            'success' : False,
            'message' : {
                "color": "Couleur recquise et doit etre l'une des suivantes : 'green', 'yellow', 'red', 'blue'.",
                "battery" : "Niveau de batterie recquis et doit etre compris entre 0 et 100."
            }
        }
        return (response, 400, headers)


# Initialisation de la base de données
connection = connect()
cursor = connection.cursor()
with open('schema.sql') as f:
    cursor.executescript(f.read())  
connection.close()