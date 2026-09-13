import os
import subprocess

def segmentar_archivos_tiempo(archivos, salida):
    """
    Une una lista de audios re-codificándolos en un archivo maestro
    y luego los segmenta estrictamente en bloques de 1 hora (3600s).
    """
    # 1. CORREGIDO: Forzar a extraer el string si 'salida' es una lista
    dir_salida = salida[0] if isinstance(salida, list) else salida
    
    # 2. VALIDACIÓN: Si no es un directorio o no existe, lanzar un error estricto
    if not os.path.isdir(dir_salida):
        raise ValueError(
            f"Error crítico: La ruta de salida {dir_salida} no es un directorio válido o no existe."
        )
        
    # 3. Definir rutas de archivos temporales y patrón final
    extension = ".mp3"
    lista_txt = os.path.join(dir_salida, "lista_archivos_ffmpeg.txt")
    maestro_mp3 = os.path.join(dir_salida, "maestro_temporal_continuo.mp3")
    nombre_salida_patron = os.path.join(dir_salida, f"salida_%03d{extension}")
    
    try:
        # 4. Escribir la lista de reproducción virtual para FFmpeg
        with open(lista_txt, "w", encoding="utf-8") as f:
            for archivo in archivos:
                ruta_absoluta = os.path.abspath(archivo)
                ruta_normalizada = ruta_absoluta.replace("\\", "/")
                f.write(f"file '{ruta_normalizada}'\n")
        
        # PASO 1: Concatenar y re-codificar todo a un único archivo MP3 continuo
        print(f"Paso 1/2: Uniendo y re-codificando {len(archivos)} archivos...")
        comando_unir = [
            "ffmpeg", "-y",
            "-f", "concat",
            "-safe", "0",
            "-i", lista_txt,
            "-c:a", "libmp3lame",
            "-q:a", "4",  # Excelente calidad VBR
            maestro_mp3
        ]
        subprocess.run(comando_unir, capture_output=True, text=True, check=True)
        
        # PASO 2: Segmentar el archivo maestro generado
        print("Paso 2/2: Segmentando el flujo continuo en bloques estrictos de 1 hora...")
        comando_segmentar = [
            "ffmpeg", "-y",
            "-i", maestro_mp3,
            "-c", "copy",  # Copia directa instantánea ya que el archivo ya fue procesado
            "-f", "segment",
            "-segment_time", "3600",
            "-reset_timestamps", "1",
            nombre_salida_patron
        ]
        subprocess.run(comando_segmentar, capture_output=True, text=True, check=True)
        
        print("¡Proceso completado con éxito! Se han generado los archivos numerados.")
        
    except subprocess.CalledProcessError as e:
        print(f"Error crítico en FFmpeg: {e.stderr}")
        raise
    finally:
        # 5. Limpieza absoluta de archivos temporales
        if os.path.exists(lista_txt):
            os.remove(lista_txt)
        if os.path.exists(maestro_mp3):
            os.remove(maestro_mp3)
