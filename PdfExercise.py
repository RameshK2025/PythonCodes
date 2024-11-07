import os
import PyPDF2
import pdb

def read_pdf_to_text(pdf_path):
    try:
        # Check if the PDF file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"The file '{pdf_path}' does not exist.")
        
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text_content = ""
            
            # Iterate through each page and extract text
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text_content += page.extract_text() + "\n"
        
        return text_content

    except Exception as e:
        return str(e)

def write_text_to_file(text, output_path):
    try:
        # Write the text content to the output file
        # Set a trace using Python Debugger
        
        with open(output_path, 'w',encoding='utf-8') as f:
            f.write(text)
        return f"The content has been successfully written to '{output_path}'."
    
    except Exception as e:
        return str(e)

# Define paths
content_folder = 'content'
pdf_file_name = 'Chemistry Questions.pdf'
output_file_name = 'output.txt'

# Ensure the content folder exists
if not os.path.exists(content_folder):
    os.makedirs(content_folder)

# Define full paths
pdf_path = os.path.join(content_folder, pdf_file_name)
output_path = os.path.join(content_folder, output_file_name)

# Read PDF content
pdb.set_trace()
pdf_text = read_pdf_to_text(pdf_path)


# Write to output file
pdb.set_trace()
result_message = write_text_to_file(pdf_text, output_path)

print(result_message)
