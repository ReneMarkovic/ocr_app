import streamlit as st
from PIL import Image
import pytesseract
import re
import pdf2image

pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
pytesseract.pytesseract.tesseract_cmd = r'C://Program Files//Tesseract-OCR//tesseract.exe'
# Step 1: Allow the user to select an image file
image_file = st.file_uploader("Naložite sliko", type=["jpg", "png", "jpeg","pdf"])
ext=print(image_file.name.split(".")[1])
if ext=="pdf":
    images = pdf2image.convert_from_bytes(image_file.read())
    pc=0
    for page in images:
        st.image(page, use_column_width=True)
        page.save(f'data//image_{pc+1}.jpg', 'PNG')
        pc+=1
if image_file is not None:
    # Step 2: Open the image file and convert it to a format Pytesseract can read
    image = Image.open(image_file)
    # Step 3: Perform OCR on the image and extract the text
    text = pytesseract.image_to_string(image)
    text_proc=re.sub(r"\s\s+",r" ",text)
    text_proc=re.sub(r"[*]",r" ",text)
    text_proc=re.sub(r"\n\n",r"\n",text)
    
    # Step 4: Display the extracted text on the webpage
    st.write("Extracted text:")
    st.write(text_proc)

    # Step 5: Add a "Download" button
    if st.button("Download"):
        st.text("Saving file...")
        with open("extracted_text.txt", "w") as f:
            f.write(text_proc)
        st.text("Downloaded")