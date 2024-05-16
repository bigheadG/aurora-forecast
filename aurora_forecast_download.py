import requests
from bs4 import BeautifulSoup
import os

# URL of the directory containing the files
url = "https://services.swpc.noaa.gov/images/animations/enlil/" 
#jpg
#"https://services.swpc.noaa.gov/images/animations/enlil/" 
#"https://services.swpc.noaa.gov/images/animations/ovation/south/"   
#"https://services.swpc.noaa.gov/images/animations/enlil/" 

# Directory to save downloaded files
download_directory = 'downloaded_enlil_files'

# List of file types to be downloaded
file_types = ['.png', '.jpg']

# Send a GET request to the URL
response = requests.get(url)
if response.status_code != 200:
    print("Failed to retrieve the webpage")
    exit()

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all links on the page
links = soup.find_all('a')

# Create a directory to store the downloaded files
os.makedirs(download_directory, exist_ok=True)

# Get a list of filenames already downloaded
downloaded_files = os.listdir(download_directory)

# Loop through the links and download the files
for link in links:
    href = link.get('href')
    # Ensure href is not None and ends with one of the specified file types
    if href and any(href.endswith(file_type) for file_type in file_types):
        filename = href.split('/')[-1]
        if filename in downloaded_files:
            print(f"Skipping {filename} as it's already downloaded")
            continue
        print(f"Downloading {filename}.......")
        file_url = url + href
        # Download the file
        response = requests.get(file_url)
        if response.status_code == 200:
            with open(os.path.join(download_directory, filename), 'wb') as f:
                f.write(response.content)
                print(f"Downloaded {filename}")
        else:
            print(f"Failed to download {filename}")

print("All files downloaded successfully!")
