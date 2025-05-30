from flask import Flask, request, jsonify  
import sqlite3  

app = Flask(__name__)  

@app.route('/usuarios', methods=['GET'])  
def obtener_usuarios():  
    conexion = sqlite3.connect("pinterest.db")  
    cursor = conexion.cursor()  
    cursor.execute("SELECT * FROM usuarios")  
    usuarios = cursor.fetchall()  
    conexion.close()  
    return jsonify(usuarios)