import os
import re
import json
import PyPDF2
import pdb

def read_pdf_to_text(pdf_path, page_number):
    try:
        # Check if the PDF file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"The file '{pdf_path}' does not exist.")
        
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            # Check if the page number is valid
            if page_number < 1 or page_number > len(reader.pages):
                raise ValueError(f"Invalid page number: {page_number}. The PDF has {reader.numPages} pages.")
            
            # Extract text from the specified page
            page = reader.pages[page_number - 1]
            text_content = page.extract_text()
        
        return text_content

    except Exception as e:
        return str(e)

def write_text_to_file(text, output_path):
    try:
        # Write the text content to the output file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)
        return f"The content has been successfully written to '{output_path}'."
    
    except Exception as e:
        return str(e)

def load_config(config_path):
    try:
        # Check if the configuration file exists
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"The configuration file '{config_path}' does not exist.")
        
        # Load the configuration file
        with open(config_path, 'r', encoding='utf-8') as f:
            pdb.set_trace()
            config = json.load(f)
        
        # Check if the regex key is present in the configuration
        if 'pattern' not in config:
            raise KeyError("The configuration file does not contain the 'pattern' key.")
        
        return config['pattern']

    except Exception as e:
        return str(e)

# Define paths
content_folder = 'content'
pdf_file_name = 'Chemistry Questions.pdf'
output_file_name = 'output.txt'
config_file_name = 'config.json'

# Ensure the content folder exists
if not os.path.exists(content_folder):
    os.makedirs(content_folder)

# Define full paths
pdf_path = os.path.join(content_folder, pdf_file_name)
output_path = os.path.join(content_folder, output_file_name)
config_path = os.path.join(content_folder, config_file_name)

# Take a page number as input from command prompt
try:
    page_number = int(input("Enter the page number to read: "))
except ValueError:
    print("Invalid input. Please enter a valid page number.")
    exit()

# Load configuration and get regex pattern
regex_pattern = load_config(config_path)
print("Regex pattern returned is ", regex_pattern)
##if isinstance(regex_pattern, str) and regex_pattern.startswith("The "):
##    print(regex_pattern)
##    exit()

# Read PDF content from the specified page
pdf_text = read_pdf_to_text(pdf_path, page_number)
##if isinstance(pdf_text, str) and pdf_text.startswith("The "):
##    print(pdf_text)
##    exit()

print(pdf_text)
# Extract content matching the regular expression
pattern = r'\bhorizontal\b'


matched_content = re.findall(pattern, pdf_text, re.IGNORECASE)

# Write to output file
result_message = write_text_to_file('\n'.join(matched_content), output_path)

print(result_message)
