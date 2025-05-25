import sqlite3
from sqlite3 import Error

class baseDatos:
    def __init__(self, ruta = "./", bd = "miBD.sqlite3"):
        self.bd = ruta + '/' + bd
        self.conexionSQL()
        
    def conexionSQL(self): #Se crea objeto para inicializar la conexion
        try:
            self.con = sqlite3.connect(self.bd)
            self.cursor = self.con.cursor()
        except Error:
            print(Error)
            
    def crearDB(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS general(
                            alumno TEXT PRIMARY KEY,
                            espanol REAL,
                            matematicas REAL,
                            historia REAL)""")
        
    def agregarAlumno(self, alumno):
        self.cursor.execute("""INSERT INTO general (alumno) VALUES(?)""", (alumno,))
        self.con.commit()
        
    def eliminarAlumno(self, alumno):
        self.cursor.execute("""DELETE FROM general WHERE alumno = ?""", (alumno,))
        self.con.commit()
        
    def actualizarEspanol(self, calif, alumno):
        self.cursor.execute("""UPDATE general SET espanol = ? WHERE alumno = ?""", (calif, alumno))
        self.con.commit()
        self.cursor.execute("""SELECT * FROM general WHERE alumno = ?""", (alumno,))
        lista = self.cursor.fetchall()
        return lista
    
    def actualizarMatematicas (self, calif, alumno):
        self.cursor.execute("""UPDATE general SET matematicas = ? WHERE alumno = ?""", (calif, alumno))
        self.con.commit()
        self.cursor.execute("""SELECT * FROM general WHERE alumno = ?""", (alumno,))
        lista = self.cursor.fetchall()
        return lista
    
    def actualizarHistoria(self, calif, alumno):
        self.cursor.execute("""UPDATE general SET historia = ? WHERE alumno = ?""", (calif, alumno))
        self.con.commit()
        self.cursor.execute("""SELECT * FROM general WHERE alumno = ?""", (alumno,))
        lista = self.cursor.fetchall()
        return lista
    
    def listarGeneral(self):
        self.cursor.execute("""SELECT * FROM general""")
        lista = self.cursor.fetchall()
        return lista
    