import PyPDF2

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    with open(pdf_path, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)
        
        # Initialize a variable to store extracted text
        text = ''
        
        # Loop through all the pages
        for page_num in range(len(reader.pages)):
            # Extract text from each page
            page = reader.pages[page_num]
            text += page.extract_text() + '\n'
    
    return text

# Provide the path to your PDF file
pdf_path = 'C:/Users/Admin/Desktop/kaguya/시노미야 카구야.pdf'
extracted_text = extract_text_from_pdf(pdf_path)

# Display the extracted text
print(extracted_text)

def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

# Path where the extracted text will be saved
output_file = 'extracted_text.txt'
save_text_to_file(extracted_text, output_file)