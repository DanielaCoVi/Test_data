from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import requests
from bs4 import BeautifulSoup

# Initialize the browser
driver = webdriver.Chrome() # Asegúrate de tener el driver de Chrome instalado

# We maximize the browser
driver.maximize_window()

# Keyword to search images on Google
keyword = "gatos"

# Navigating to the Google image search page
url = "https://www.google.com/search?tbm=isch&q="
driver.get(url + keyword)

# Wait a moment for the page to load
time.sleep(2)

# Scrolling to load more images
for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

# Obtain links to images
soup = BeautifulSoup(driver.page_source, 'html.parser')
image_links = []
for img in soup.find_all('img'):
    if img.get('data-src'):
        image_links.append(img.get('data-src'))

# Create a directory to store downloaded images
if not os.path.exists(keyword):
    os.makedirs(keyword)

# Download images
for i, link in enumerate(image_links):
    try:
        response = requests.get(link)
        with open(os.path.join(keyword, f"image_{i}.jpg"), "wb") as f:
            f.write(response.content)
        print(f"Image {i} downloaded successfully")
    except Exception as e:
        print(f"Error downloading image {i}: {e}")

# Close the browser
driver.quit()
