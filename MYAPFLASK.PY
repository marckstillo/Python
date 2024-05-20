from flask import Flask 
app = Flask(__name__)
@app.route("/ver")
def saludar():
    return "<h1>HOLA MUNDO</h1>"
@app.route("/hora")
def hora():
    return "<h1>LA HORA ES</h1>"