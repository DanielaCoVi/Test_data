#!/usr/bin/env python
# coding: utf-8

# In[2]:


from selenium import webdriver


# In[3]:


from selenium.webdriver.common.keys import Keys
import time
import os
import requests
from bs4 import BeautifulSoup

# Inicializar el navegador
driver = webdriver.Chrome() # Asegúrate de tener el driver de Chrome instalado

# Palabra clave para buscar imágenes en Google
keyword = "gatos"

# Navegar a la página de búsqueda de imágenes de Google
driver.get("https://www.google.com/search?tbm=isch&q=" + keyword)

# Esperar un momento para que la página cargue
time.sleep(2)

# Realizar scrolling para cargar más imágenes
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Obtener los enlaces de las imágenes
soup = BeautifulSoup(driver.page_source, 'html.parser')
image_links = []
for img in soup.find_all('img'):
    if img.get('data-src'):
        image_links.append(img.get('data-src'))

# Crear un directorio para almacenar las imágenes descargadas
if not os.path.exists(keyword):
    os.makedirs(keyword)

# Descargar las imágenes
for i, link in enumerate(image_links):
    try:
        response = requests.get(link)
        with open(os.path.join(keyword, f"image_{i}.jpg"), "wb") as f:
            f.write(response.content)
        print(f"Image {i} downloaded successfully")
    except Exception as e:
        print(f"Error downloading image {i}: {e}")

# Cerrar el navegador
driver.quit()


# In[ ]:




