import os
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
            page_num=page_number
            print("Page number inputted is and type is  ",page_number)
            page = reader.pages[page_number - 1]
            pdb.set_trace()
            print("Page number read is", page)
            text_content = page.extract_text()
            pdb.set_trace()
            print(text_content)
        
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

# Take a page number as input from command prompt
try:
    page_number = int(input("Enter the page number to read: "))
except ValueError:
    print("Invalid input. Please enter a valid page number.")
    exit()

# Read PDF content from the specified page
print("pdf file path is ", pdf_path)
pdf_text = read_pdf_to_text(pdf_path, page_number)

# Write to output file
result_message = write_text_to_file(pdf_text, output_path)

print(result_message)
