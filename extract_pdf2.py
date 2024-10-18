import pdfplumber

def extract_text_with_pdfplumber(pdf_path):
    # Open the PDF file using pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        # Initialize a variable to store the extracted text
        text = ''
        
        # Loop through all the pages
        for page in pdf.pages:
            # Extract text from the page
            text += page.extract_text() + '\n'
    
    return text

# Provide the path to your PDF file
pdf_path = 'C:/Users/Admin/Desktop/kaguya/시노미야 카구야.pdf'
extracted_text = extract_text_with_pdfplumber(pdf_path)

# Print the extracted text
print(extracted_text)

def save_text_to_file(text, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)

output_file = 'extracted_text_with_pdfplumber.txt'
save_text_to_file(extracted_text, output_file)