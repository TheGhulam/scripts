import os
import PyPDF2

# Directory where your PDFs are stored
pdf_dir = '/mnt/c/Users/gahme/Desktop/rahul'

# Loop over all the PDF files in the directory
for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith('.pdf'):
        file_path = os.path.join(pdf_dir, pdf_file)

        # Open the PDF file
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            # Assume the heading is on the first page and in the first line
            first_page = reader.pages[0]
            first_line = first_page.extract_text().split('\n')[0].strip()

            first_line = first_line.split(',')[-1].split("0")[1]

            # Create a new file name based on the heading
            new_file_name = f"{first_line}.pdf"
            new_file_path = os.path.join(pdf_dir, new_file_name)

            # Rename the file
            os.rename(file_path, new_file_path)

print("Renaming complete.")
