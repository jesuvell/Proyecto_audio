# Proyecto_Audio

MAS (Muliple Audio Splitter) is a **Python 3.6+** ETL framework

## Installation:
---
shell script
pip3 install MAS
---

## Descripci車n

Aplicaci車n en **Python** que recibe un conjunto de archivos MP3, individuales u organizados en carpetas,
y genera uno o m芍s archivos de salida de 1 hora de duraci車n cada uno.
Ideal para dividir grabaciones largas en bloques manejables y continuos, y mas livianos para dispositivos m車viles.

El proceso se realiza en dos partas:
1 fase: se crea un archivo con la mezcla de todos los mp3 encontrados en la entrada, y los recodifica, generando
etiquetas de tiempo
2 fase: generacion de los archivos de salida de 1 hora cada uno. Toma el archivo recodificado, y aprovecha las
etiquetas de piempo para identificar los segmentos de 1 hora. Cada archivo se va generando con un consecutivo
de 3 d赤gitos.

---

## Caracter赤sticas
- Procesa uno o m芍s archivos MP3 de larga duraci車n, desde una carpeta o lista de archivos.
- Genera archivos de salida de 1 hora.
- Si el conjunto dura menos de una hora, se exporta un 迆nico archivo concatenado.
- Manejo de archivos con codificaci車n corrupta: se recodifican los archivos fuente, de forma que se puedan 
  particionar sin problema.
- Manejo optimizado de memoria: procesa archivo por archivo sin cargar todo en RAM.
- Compatible con cualquier duraci車n de entrada (horas o incluso decenas de horas).

---

## Estructura del proyecto
MAS/
 MAS.py                # Script principal
 utils/                # Directorio con los los procesos que hacel la l車gica del proceso
   manejo_archivos.py  # Prepara los archivos de entrada, y administra el directorio de salida
   manejo_audio.py     # Realiza el particionamiento de los archivos
 requirements.txt      # Dependencias
 README.md             # Documentaci車n
 salida/               # Carpeta de salida (se genera autom芍ticamente)


---

## Instalaci車n

1. Clona el repositorio:
   ```bash
   git clone https://github.com/jesuvell/Proyecto_audio.git
   cd MAS

# Instalaci車n de dependencias
pip install -r requirements.txt

# Instala ffmpeg (requerido por pydub):
Windows: descarga desde ffmpeg.org (ffmpeg.org in Bing) y agrega la carpeta bin al PATH.

Linux (Debian/Ubuntu):

bash
sudo apt install ffmpeg
macOS (Homebrew):

bash
brew install ffmpeg

