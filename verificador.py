from Archivo import Archivo


nombre = input("Ingrese nombre de archivo: ")
hash_del_sitio = input("Ingrese hash del sitio web: ")
carpeta = input("Carpeta donde está localizado: ")

archivo = Archivo(nombre, carpeta)

def comparar_hashes(hash1, hash2):
    try:
        if (hash1 == hash2):
            print("Hashfile correcto; el archivo es seguro.")
        else:
            print("Hashfile incorrecto; descargue de nuevo.")
    except:
        print("No se encuentra el archivo.")
        exit(0)

comparar_hashes(archivo.hash_de_archivo, hash_del_sitio)
print("Nombre de archivo: " + archivo.nombre)
print("Ruta: " + archivo.ruta)
print("Hash SHA256 calculado: " + archivo.hash_de_archivo)
print("Hash SHA256 de la web: " + hash_del_sitio)