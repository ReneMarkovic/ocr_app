import streamlit as st
from PIL import Image
import pytesseract
import re
import pdf2image





pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
pytesseract.pytesseract.tesseract_cmd = r'C://Program Files//Tesseract-OCR//tesseract.exe'
# Step 1: Allow the user to select an image file

def extract_text(image_file):
    if image_file.type=="application/pdf":
        images = pdf2image.convert_from_bytes(image_file.read())
        pc=0
        text=''
        for page in images:
            st.image(page, use_column_width=True)
            page.save(f'image_{pc+1}.jpg', 'PNG')
            image = Image.open(f'image_{pc+1}.jpg')
            text+= pytesseract.image_to_string(image)
            text_proc=re.sub(r"\s\s+",r" ",text)
            text_proc=re.sub(r"[*]",r" ",text)
            text_proc=re.sub(r"\n\n",r"\n",text)
            pc+=1
    else:
        if image_file is not None:
            # Step 2: Open the image file and convert it to a format Pytesseract can read
            image = Image.open(image_file)
            # Step 3: Perform OCR on the image and extract the text
            text = pytesseract.image_to_string(image)
            text_proc=re.sub(r"\s\s+",r" ",text)
            text_proc=re.sub(r"[*]",r" ",text)
            text_proc=re.sub(r"\n\n",r"\n",text)
    return text_proc