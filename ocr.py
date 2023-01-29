import streamlit as st
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C://Program Files//Tesseract-OCR//tesseract.exe'

# Step 1: Allow the user to select an image file
image_file = st.file_uploader("Upload an image file", type=["jpg", "png", "jpeg"])

if image_file is not None:
    # Step 2: Open the image file and convert it to a format Pytesseract can read
    image = Image.open(image_file)
    # Step 3: Perform OCR on the image and extract the text
    text = pytesseract.image_to_string(image, lang="slv")

    # Step 4: Display the extracted text on the webpage
    st.write("Extracted text:")
    st.write(text)

    # Step 5: Add a "Download" button
    if st.button("Download"):
        st.text("Saving file...")
        with open("extracted_text.txt", "w") as f:
            f.write(text)
        st.text("Downloaded")