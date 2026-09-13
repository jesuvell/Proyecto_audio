import os
import sys

def directorio_salida(ruta):
    # Valida si existe directorio de salida, si no, lo crea.

    # 1. Validamos que la lista no venga vacía
    if not ruta:
        print("Error: No se proporcionó ninguna ruta de salida.")
        return None

    # 2. Extraemos el primer elemento de la lista (la ruta de la carpeta)
    directorio_final = ruta[0]

    # 3. Determinamos si el directorio existe; si no, lo creamos
    if not os.path.exists(directorio_final):
        # os.makedirs crea la carpeta y subcarpetas necesarias de forma segura
        os.makedirs(directorio_final, exist_ok=True)
        
    return directorio_final

def cargar_archivos(ruta):
    #   Carga una lista de archivos con la extensión indicada, validando de forma segura cada elemento 
    #   dentro de la lista recibida (sea carpeta o archivo), devolviendo rutas absolutas completas.

    archivos_validos = []

    # Iteramos sobre CADA elemento que el usuario pasó en la terminal
    for elemento in ruta:
        
        # Caso A: El elemento es una carpeta física
        if os.path.isdir(elemento):
            # Buscamos los mp3, creamos la ruta absoluta completa para cada uno
            for f in os.listdir(elemento):
                if f.endswith(".mp3"):
                    ruta_completa = os.path.abspath(os.path.join(elemento, f))
                    archivos_validos.append(ruta_completa)
            
        # Caso B: El elemento es un archivo individual
        elif os.path.isfile(elemento):
            if elemento.endswith(".mp3"):
                ruta_completa = os.path.abspath(elemento)
                archivos_validos.append(ruta_completa)

    return archivos_validos
