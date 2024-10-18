# Verificador de Hash SHA256

Este script de Python permite calcular el hash SHA256 de un archivo local y compararlo con el hash proporcionado por un sitio web o una fuente externa, asegurando así que el archivo descargado no ha sido alterado y es seguro.

## Descripción

El script utiliza la herramienta `certutil` de Windows para calcular el hash SHA256 de un archivo ubicado en el equipo del usuario. Posteriormente, compara el hash calculado con el hash proporcionado por una fuente externa (como el sitio web del proveedor del archivo) para verificar la integridad del archivo.

### Características:
- Calcula el hash SHA256 de un archivo local.
- Compara el hash calculado con el hash proporcionado por el sitio web.
- Informa si el archivo es seguro o si debe ser descargado de nuevo.

## Requisitos

Este script está diseñado para sistemas operativos Windows, ya que utiliza el comando `certutil`, que está disponible en este entorno. No es compatible con otros sistemas operativos sin modificaciones adicionales.

### Dependencias:
- Python 3.x
- Herramienta `certutil` (preinstalada en sistemas Windows)

## Instalación

1. Clona este repositorio o descarga el script manualmente.
   
   ```bash
   git clone https://github.com/tu-usuario/verificador-hash.git
   ```
   
2. Asegúrate de tener Python 3.x instalado en tu sistema.

## Uso

1. Ejecuta el script en la consola:

    ```bash
    python verificador.py
    ```

2. Proporciona la siguiente información cuando se te solicite:

    - Nombre del archivo: El nombre del archivo que deseas verificar.
    - Carpeta: La carpeta donde se encuentra el archivo en tu sistema.
    - Hash del sitio web: El hash SHA256 proporcionado por el sitio web o la fuente confiable.

3. El script calculará el hash del archivo y lo comparará con el hash proporcionado. Si los hashes coinciden, se indicará que el archivo es seguro; de lo contrario, se recomienda volver a descargarlo.

## Ejemplo de uso

   ```bash
   Ingrese nombre de archivo: ejemplo.txt
   Ingrese hash del sitio web: 2c3a40993a450dc9a059563d07664fc0fb85ae398a57d22b1b4bf0e602417bf7
   Carpeta donde está localizado: Downloads
   Hashfile correcto; el archivo es seguro.
   Nombre de archivo: ejemplo.txt
   Ruta: C:\Users\tu-usuario\Downloads\ejemplo.txt
   Hash SHA256 calculado: 2c3a40993a450dc9a059563d07664fc0fb85ae398a57d22b1b4bf0e602417bf7
   Hash SHA256 de la web: 2c3a40993a450dc9a059563d07664fc0fb85ae398a57d22b1b4bf0e602417bf7
   ```

## Advertencia

Este script funciona únicamente en entornos Windows. Si se utiliza en otro sistema operativo, se deben modificar los comandos que calculan el hash del archivo.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún error o deseas mejorar el script, siéntete libre de enviar un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Puedes consultar los detalles en el archivo LICENSE.
