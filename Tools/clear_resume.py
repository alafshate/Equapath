import fitz  # PyMuPDF
import pytesseract
from PIL import Image

def extract_name_from_pdf(input_pdf_path):
    pdf_document = fitz.open(input_pdf_path)
    
    # Analyze the first page to find potential name text (assuming name is on the first page)
    first_page = pdf_document[0]
    pix = first_page.get_pixmap()
    
    # Convert to a PIL image for OCR
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    
    # Use Tesseract OCR to extract text from the image
    extracted_text = pytesseract.image_to_string(img)
    
    # Simple heuristic: Assume the name is in the first few lines
    lines = extracted_text.splitlines()
    for line in lines:
        if line.strip() and any(word.isalpha() for word in line.split()):  # Basic filter for non-empty and alphabetic
            return line.strip()
    
    return None  # Return None if no probable name is found

def whiten_name_in_pdf(input_pdf_path, output_pdf_path):
    # Extract name from the PDF
    name_to_whiten = extract_name_from_pdf(input_pdf_path)
    if not name_to_whiten:
        print("Could not detect a probable name in the PDF.")
        return
    
    print(f"Detected name: {name_to_whiten}")
    
    # Open the input PDF file
    pdf_document = fitz.open(input_pdf_path)
    
    # Iterate over each page
    for page_num in range(pdf_document.page_count):
        page = pdf_document[page_num]
        
        # Search for the name text on the page
        name_instances = page.search_for(name_to_whiten)
        
        # If name is found, whiten it out
        for rect in name_instances:
            # Draw a white rectangle over the name's bounding box
            page.draw_rect(rect, color=(1, 1, 1), fill=(1, 1, 1))
    
    # Save the modified PDF to a new file
    pdf_document.save(output_pdf_path)
    pdf_document.close()
    print(f"Name '{name_to_whiten}' has been whitened out in the PDF and saved as '{output_pdf_path}'.")

# Usage
input_pdf_path = "resume.pdf"  # Path to the input PDF
output_pdf_path = "resume_whitened.pdf"  # Path to save the output PDF

whiten_name_in_pdf(input_pdf_path, output_pdf_path)
