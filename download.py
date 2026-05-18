import urllib.request
import zipfile
import os

url = "https://codeload.github.com/VincentSilveira/AIML/zip/refs/heads/main.zip"
zip_name = "AIML.zip"

print("Downloading repository...")
urllib.request.urlretrieve(url, zip_name)

print("Extracting files...")
with zipfile.ZipFile(zip_name, 'r') as zip_ref:
    zip_ref.extractall(".")

os.remove(zip_name)
print("Done! Repository downloaded and extracted successfully.")
