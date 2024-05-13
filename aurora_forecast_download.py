import requests
from bs4 import BeautifulSoup
import os

# URL of the directory containing the files
url = "https://services.swpc.noaa.gov/images/animations/ovation/south/"  
download_files = 'downloaded_files'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all links on the page
links = soup.find_all('a')

# Create a directory to store the downloaded files
os.makedirs(download_files, exist_ok=True)

# Get a list of filenames already downloaded
downloaded_files = os.listdir(download_files)

# Loop through the links and download the files
for link in links:
    href = link.get('href')
    if href.endswith('.jpg'):
        filename = href.split('/')[-1]
        if filename in downloaded_files:
            print(f"Skipping {filename} as it's already downloaded")
            continue
        print(f"Downloading {filename}.......")
        file_url = url + href
        # Download the file
        response = requests.get(file_url)
        with open(os.path.join(download_files, filename), 'wb') as f:
            f.write(response.content)
            print(f"Downloaded {filename}")

print("All files downloaded successfully!")
