import streamlit as st
from convert_to_text import convert

st.markdown("# PDF/img to tekst")

st.markdown("Aplikacija omogoča uporabniku da tekst, ki je zajet v sliki ali pdf dokumentu pretvori v besedilo, ki  ga lahko tudi prense.")



image_file = st.file_uploader("Naložite sliko", type=["jpg", "png", "jpeg","pdf"])
button = st.button("Prični transformacijo v txt")

if image_file is not None:
    text=convert.extract_text(image_file)
    # Step 4: Display the extracted text on the webpage
    st.write("Izločeno je bilo besedilo:")
    st.write(text)

    # Step 5: Add a "Download" button
    if st.button("Prenesi"):
        st.text("Shranjevanje datoteke ......")
        with open("besedilo.txt", "w") as f:
            f.write(text)
        st.text("Preneseno.")