import subprocess
from os import getlogin

usuario = getlogin()

class Archivo:
    def __init__(self, nombre, carpeta):
        self.nombre = nombre
        self.carpeta = carpeta
        self.ruta = "C:\\Users\\" + usuario + "\\" + carpeta + "\\" + nombre
        self.hash_de_archivo = self.funcion_hash()


    def funcion_hash(self):
        calculo_de_hash = subprocess.run(
            ["certutil", "-hashfile", self.ruta, "SHA256"],
            capture_output=True,
            text=True
        )
        lineas = calculo_de_hash.stdout.splitlines()
        hashSHA256 = lineas[1]
        return hashSHA256