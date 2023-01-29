import streamlit as st
from convert_to_text import convert

st.markdown("Pretvori v sliko")
image_file = st.file_uploader("Naložite sliko", type=["jpg", "png", "jpeg","pdf"])
button = st.button("Prični transformacijo v txt")

if image_file is not None:
    text=convert.extract_text(image_file)
    # Step 4: Display the extracted text on the webpage
    st.write("Extracted text:")
    st.write(text)

    # Step 5: Add a "Download" button
    if st.button("Download"):
        st.text("Saving file...")
        with open("extracted_text.txt", "w") as f:
            f.write(text)
        st.text("Downloaded")