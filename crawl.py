import selenium
selenium.__version__
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import time
import os

service = Service()

# Setting up Chrome options for headless browsing if needed
options = Options()
options.headless = True

# Initialize the WebDriver with the service and options
driver = webdriver.Chrome(service=service, options=options)

# URL to be scraped
url = "https://www.cube.global/resource/revolut-case-study-automating-compliance-for-continued-growth/"

# Navigate to the page
driver.get(url)

# Wait for the page to load completely
time.sleep(5)  # Adjust the sleep time based on your network speed

# Extract the page source
html_content = driver.page_source

# Parse the URL to extract the last path segment
parsed_url = urlparse(url)
url_path = parsed_url.path
file_name = url_path.strip('/').split('/')[-1] + '.html'

# Ensure the file name is not empty, else set a default
if not file_name.strip('.html'):
    file_name = 'default.html'

# Check if the 'content' folder exists, and create it if it doesn't
folder_path = 'content'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Define the path to save the file
file_path = os.path.join(folder_path, file_name)

# Save the HTML content to a file
with open(file_path, 'w', encoding='utf-8') as file:
    file.write(html_content)

# Close the driver
driver.quit()