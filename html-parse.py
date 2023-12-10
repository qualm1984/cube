from llama_index.node_parser import HTMLNodeParser
from llama_index import SimpleDirectoryReader
from bs4 import BeautifulSoup
import os

# Define the folder and filename
folder_path = 'content'
file_name = 'revolut-case-study-automating-compliance-for-continued-growth.html'  # Replace with your actual file name

# Construct the full file path
file_path = os.path.join(folder_path, file_name)

# Read the HTML content from the file
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Process the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
div_content = str(soup.find("div", class_="gb-block-layout-column-inner"))

# Save the extracted div content to a new HTML file
div_file_path = os.path.join(folder_path, 'extracted_div.html')
with open(div_file_path, 'w', encoding='utf-8') as file:
    file.write(div_content)

# Use SimpleDirectoryReader to read the new file as a Document object
documents = SimpleDirectoryReader(folder_path).load_data()

# Initialize the HTMLNodeParser
parser = HTMLNodeParser(tags=["div"])  # Or other tags as needed

# Parse the loaded documents
nodes = parser.get_nodes_from_documents(documents)

print("Number of nodes:", len(nodes))
