import os
from flaskext.mysql import MySQL
from flask import Flask, redirect, render_template, request, url_for

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        MYSQL_DATABASE_USER='root',
        MYSQL_DATABASE_PASSWORD='',
        MYSQL_DATABASE_DB='tekbot',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
        
    mysql = MySQL()
    mysql.init_app(app)
    connection = mysql.connect()
    cursor = connection.cursor()
    cursor.execute(" TRUNCATE TABLE colors")

    @app.get("/")
    def render_page():
        cursor.execute("""
            SELECT color, COUNT(*) AS total
            FROM colors
            WHERE color IN ('green', 'yellow', 'red', 'blue')
            GROUP BY color
        """)
        colors = cursor.fetchall()
        
        green = yellow = red = blue = 0
        context = {}
        for color, count in colors :
            if color == "green" : green = count
            if color == "yellow" : yellow = count
            if color == "red" : red = count
            if color == "blue" : blue = count
            
        return render_template("index.html", green=green, yellow=yellow, red=red, blue=blue)

    @app.get("/set")
    def save_color_web():
        color = request.args.get("color")
        if color in ['green', 'yellow', 'red', 'blue'] :
            cursor.execute(f"INSERT INTO `colors`(`color`) VALUES ('{color}')")
            connection.commit()
        return redirect(url_for("render_page"))
    
    @app.get("/api/set")
    def save_color_api():
        color = request.args.get("color")
        if color in ['green', 'yellow', 'red', 'blue'] :
            cursor.execute(f"INSERT INTO `colors`(`color`) VALUES ('{color}')")
            connection.commit()
            headers = {
                "Accept": 'application/json'
            }
            response = {
                'success':True,
            }
            return (response, 201, headers)
        else :
            headers = {
                "Accept": 'application/json'
            }
            response = {
                'success':False,
            }
            return (response, 422, headers)

    return app