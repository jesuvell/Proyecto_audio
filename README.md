# Proyecto_Aerolineas

MAS (Muliple Audio Splitter) is a **Python 3.6+** ETL framework

## Installation:
```shell script
pip3 install MAS
```

# 馃幍 Segmentador de Multiples Audios en Python

Aplicaci贸n en **Python** que recibe un conjunto de archivos MP3, individuales o en una carpeta, y genera 
uno o m谩s archivos de salida de 1 hora de duraci贸n cada uno, optimizando el uso de memoria.
Ideal para dividir grabaciones largas en bloques manejables y continuos, y mas livianos para dispositivos m贸viles.

---

## 馃殌 Caracter铆sticas
- Procesa uno o m谩s archivos MP3 de larga duraci贸n, desde una carpeta o lista de archivos.
- Genera archivos de salida de 1 hora.
- Si el conjunto dura menos de una hora, se exporta un 煤nico archivo concatenado.
- Manejo optimizado de memoria: procesa archivo por archivo sin cargar todo en RAM.
- Compatible con cualquier duraci贸n de entrada (horas o incluso decenas de horas).

---

## Estructura del proyecto
MAS/
 MAS.py        # Script principal
 requirements.txt      # Dependencias
 README.md             # Documentación
 salida/               # Carpeta de salida (se genera automáticamente)


---

## 鈿欙笍 Instalaci贸n

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tuusuario/MAS.git
   cd MAS

# 鈿欙笍 Instalaci贸n de dependencias
pip install -r requirements.txt

# Instala ffmpeg (requerido por pydub):
Windows: descarga desde ffmpeg.org (ffmpeg.org in Bing) y agrega la carpeta bin al PATH.

Linux (Debian/Ubuntu):

bash
sudo apt install ffmpeg
macOS (Homebrew):

bash
brew install ffmpeg

