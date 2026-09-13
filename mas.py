import utils.manejo_archivos as mar
import utils.manejo_audio as mau
import sys

# --- CÓDIGO PRINCIPAL DE TU APLICACIÓN ---
if __name__ == "__main__":
    # Los argumentos de la aplicación están en sys.argv.
    # sys.argv[0] es siempre el nombre del script ("app.py")
    # sys.argv[1] será el primer argumento que escribas después (la ruta)
    
    # Validamos si el usuario olvidó escribir la ruta en la consola
    if len(sys.argv) < 3:
        print("Error: Por favor, especifica al menos una ruta.")
        print('Uso correcto: python app.py "RUTA_DE_SALIDA" "LISTA_ARCHIVOS_ENTRADA"')
        sys.exit(1) # Cierra el programa con código de error
        
    # Capturamos la ruta que pasaste por consola
    ruta_salida = [sys.argv[1]]
    ruta_recibida = sys.argv[2:]
    
    # Invocamos tu función pasándole el argumento dinámico
    archivos_salida = mar.directorio_salida(ruta_salida)
    
    # Invocamos tu función pasándole el argumento dinámico
    archivos_entrada = mar.cargar_archivos(ruta_recibida)
    
    # Mostramos los resultados obtenidos
    print(f"\n--- Se encontraron {len(archivos_entrada)} archivos mp3 ---")
    for archivo in archivos_entrada:
        print(archivo)

    mau.segmentar_archivos_tiempo(archivos_entrada, ruta_salida)
    
