import sqlite3  

def crear_tabla():  
    conexion = sqlite3.connect("pinterest.db")  
    cursor = conexion.cursor()  
    cursor.execute("""  
        CREATE TABLE IF NOT EXISTS usuarios (  
            id INTEGER PRIMARY KEY AUTOINCREMENT,  
            nombre TEXT NOT NULL,  
            email TEXT UNIQUE  
        )  
    """)  
    conexion.commit()  
    conexion.close()