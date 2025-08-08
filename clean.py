import fitz  # PyMuPDF
import re

def clean_pdf_text(pdf_path, output_txt_path):
    # Load PDF
    doc = fitz.open(pdf_path)
    all_text = ""

    for page in doc:
        raw_text = page.get_text()

        # Clean up:
        # - Remove extra whitespaces
        # - Remove multiple newlines
        # - Remove page numbers (standalone numbers)
        # - Remove repeated headers/footers
        cleaned = re.sub(r'\n\s*\n', '\n', raw_text)  # Collapse multiple blank lines
        cleaned = re.sub(r'^\s*\d+\s*$', '', cleaned, flags=re.MULTILINE)  # Remove standalone page numbers
        cleaned = re.sub(r'INCOME TAX LAW', '', cleaned, flags=re.IGNORECASE)  # Remove repeating title
        cleaned = cleaned.strip()
        all_text += cleaned + "\n\n"

    # Save cleaned text
    with open(output_txt_path, "w", encoding="utf-8") as f:
        f.write(all_text)

    print(f"Cleaned text saved to {output_txt_path}")

# Example usage
pdf_path = "15. Income Tax Law Author World Trade Organization.pdf"
output_txt_path = "cleaned_income_tax_law.txt"

clean_pdf_text(pdf_path, output_txt_path)
