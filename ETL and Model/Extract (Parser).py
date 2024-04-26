import pdfplumber
import pandas as pd
def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

# Example usagec
text = extract_text_from_pdf("Financial_Statements.pdf")
# print(text)
# df = pd.DataFrame({"Extracted Text ":text})
# Save extracted text to a text file
output_file = "extracted_text.txt"
with open(output_file, "w") as file:
    file.write(text)
