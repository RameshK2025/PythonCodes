import os
import PyPDF2
import pdb

def create_folders(base_folder, sub_folders):
    try:
        # Create base folder if it doesn't exist
        if not os.path.exists(base_folder):
            os.makedirs(base_folder)
        
        # Create sub folders
        for folder in sub_folders:
            sub_folder_path = os.path.join(base_folder, folder)
            if not os.path.exists(sub_folder_path):
                os.makedirs(sub_folder_path)
        
        return "Folders created successfully."
    
    except Exception as e:
        return str(e)

def add_pdf_files(base_folder, sub_folders, pdf_file_name):
    try:
        for folder in sub_folders:
            pdb.set_trace()
            sub_folder_path = os.path.join(base_folder, folder)
            print("Sub Folder Path is",sub_folder_path)
            pdf_file_path = os.path.join(base_folder, pdf_file_name)
            print("Reading PDF file from Main Path ",pdf_file_path)
            
            # Copy the PDF file to each sub folder
##            with open(pdf_file_name, 'rb') as src_file:
##                pdb.set_trace()
##                with open(pdf_file_path, 'wb') as dest_file:
##                    dest_file.write(src_file.read())
            sub_folder_file=os.path.join(sub_folder_path,pdf_file_name)
            print(sub_folder_file)
            with open(pdf_file_path, 'rb') as src_file:
                pdb.set_trace()
                with open(sub_folder_file, 'wb') as dest_file:
                    dest_file.write(src_file.read())
        
        return "PDF files added successfully."
    
    except Exception as e:
        return str(e)

def read_pdf_to_text(pdf_path):
    try:
        # Check if the PDF file exists
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"The file '{pdf_path}' does not exist.")
        
        # Open the PDF file
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text_content = ""
            pdb.set_trace()
            
            # Iterate through each page and extract text
            for page_num in range(len(reader.pages)):
                pdb.set_trace()
                page = reader.pages[page_num]
                pdb.set_trace()
                text_content += page.extract_text() + "\n"
                print(text_content)
        return text_content

    except Exception as e:
        return str(e)

def write_text_to_file(text, output_path):
    try:
        # Write the text content to the output file
        with open(output_path, 'w',encoding='utf-8') as f:
            f.write(text)
        return f"The content has been successfully written to '{output_path}'."
    
    except Exception as e:
        return str(e)

# Define paths and folders
base_folder = 'content'
sub_folders = ['one', 'two', 'three']
pdf_file_name = 'Chemistry Questions.pdf'
output_file_name = 'output.txt'

# Step 1: Create folders
create_folders_result = create_folders(base_folder, sub_folders)
print(create_folders_result)

# Step 2: Add PDF files to sub folders
add_pdf_files_result = add_pdf_files(base_folder, sub_folders, pdf_file_name)
print(add_pdf_files_result)

# Step 3: Load all PDF files and write content to output.txt in each sub folder
for folder in sub_folders:
    sub_folder_path = os.path.join(base_folder, folder)
    pdf_path = os.path.join(sub_folder_path, pdf_file_name)
    output_path = os.path.join(sub_folder_path, output_file_name)
    
    # Read PDF content
    pdf_text = read_pdf_to_text(pdf_path)
    
    # Write to output file
    result_message = write_text_to_file(pdf_text, output_path)
    
    print(result_message)
