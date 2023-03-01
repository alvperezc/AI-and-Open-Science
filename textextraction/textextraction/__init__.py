import requests
import re
import os
from bs4 import BeautifulSoup
from textblob import TextBlob
import nltk
import xml.etree.ElementTree as ET
nltk.download('brown')
nltk.download('punkt')

from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Construir la URL completa
# En caso de estar corriendolo en local sustituir grobid por localhost
grobid_url = "http://grobid:8070/api/processFulltextDocument"

# Definir la carpeta que contiene los archivos PDF
folder_path = "../resources"

# Obtener la lista de archivos en la carpeta
file_list = os.listdir(folder_path)

text = ""
num_images_list = []

# Definir la carpeta que contiene los archivos PDF
for filename in file_list:
    if filename.endswith(".pdf"):
        # Construir la ruta completa del archivo
        filepath = os.path.join(folder_path, filename)

        # Leer el contenido del archivo
        with open(filepath, 'rb') as pdf_file:
            file_content = pdf_file.read()

        # Enviar la solicitud a Grobid
        response = requests.post(grobid_url, files={'input': file_content})

        # Procesar la respuesta
        if response.status_code == 200:
            # La respuesta es un documento TEI en XML
            texto = response.content

            #--------------Nube de palabras-------------
            soup = BeautifulSoup(texto, 'lxml')
            texto_limpio = soup.get_text(strip=True)
            blob = TextBlob(texto_limpio)
            palabras_clave = blob.noun_phrases

            # Unir las palabras clave en una cadena separada por espacios
            text = " ".join(palabras_clave)

            #---------Nº de Imágenes------------
            root = ET.fromstring(texto)

            num_figures = len(root.findall('.//{http://www.tei-c.org/ns/1.0}figure'))
            num_images_list.append(num_figures)

            #---------Links-----------
            # Define la expresión regular para buscar URLs
            patron_url = re.compile(r'(?:http[s]?://)?(www\.[^\s]+)')

            # Busca todas las URLs en el texto
            urls_encontradas = re.findall(patron_url, texto_limpio)
            print(f"En el archivo: {filename}, aparececen estos links: {urls_encontradas}")
        else:
            # Si hay algún error, se muestra el mensaje de error de Grobid
            print("Error al procesar el archivo: ", filename)
            print(response.text)

# Crear una instancia de la clase WordCloud
wordcloud = WordCloud(width = 800, height = 800, background_color ='white', min_font_size = 10).generate(text)

# Mostrar la nube de palabras utilizando matplotlib
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)

if not os.path.exists("../resources/figures"):
    os.makedirs("../resources/figures")               
plt.savefig('../resources/figures/wordcloud.png')

# Crear un gráfico de barras que muestre el número de imágenes
fig2=plt.figure()
plt.bar([os.path.splitext(filename)[0] for filename in os.listdir(folder_path) if filename.endswith('.pdf')], num_images_list)
plt.xticks(rotation=90)
plt.ylabel('Número de imágenes')
plt.title('Número de imágenes en cada archivo')

plt.savefig('../resources/figures/numfigs.png')

        