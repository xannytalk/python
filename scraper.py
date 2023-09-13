import os
import requests
import base64
from bs4 import BeautifulSoup
from urllib.parse import urljoin


url = "//"


download_folder = "//"


os.makedirs(download_folder, exist_ok=True)


response = requests.get(url)
html_content = response.content


soup = BeautifulSoup(html_content, "html.parser")
img_tags = soup.find_all("img")

for img_tag in img_tags:
    img_url = img_tag.get("src")
    img_url = urljoin(url, img_url)  
    img_name = os.path.basename(img_url)

    
    if img_url.startswith('data:image'):
        img_data = img_url.split(",")[1]
        img_data = base64.b64decode(img_data)
        img_path = os.path.join(download_folder, img_name)
        with open(img_path, "wb") as img_file:
            img_file.write(img_data)
        print(f"Heruntergeladen: {img_name}")
    else:
       
        img_path = os.path.join(download_folder, img_name)
        img_response = requests.get(img_url)
        with open(img_path, "wb") as img_file:
            img_file.write(img_response.content)
        print(f"Heruntergeladen: {img_name}")

print("Bilder wurden heruntergeladen und gespeichert.")
