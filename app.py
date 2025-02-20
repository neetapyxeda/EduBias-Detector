import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
from rag import extract_text_from_pdf

PDF_NAME = "uploaded.pdf"
IMAGE_ADDRESS = "https://europe.ippf.org/sites/europe/files/styles/header_background_xs/public/2022-12/illustration-14-website-no-logos-no-text.jpg?itok=y-vJsgkS"

# title
st.title("EduBias Detector")

# set the image
st.image(IMAGE_ADDRESS)

option = st.selectbox(
    "Please select the type of educational resource you have",
    ("PDF", "Text", "Image"),
)

#st.write("You selected:", option)

if option == 'PDF':
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_file:
    # save the file
        with open(PDF_NAME, "wb") as f:
         f.write(uploaded_file.getbuffer())

        with st.sidebar:
            st.subheader("PDF 📖")
            pdf_viewer(PDF_NAME)
        with st.spinner("Analysing............"):
            text = extract_text_from_pdf(PDF_NAME)


if option == 'Text':
    user_text=st.text_input("Enter your text")
    if user_text:
        with st.sidebar:
            st.subheader("TEXT 💬")
            #displaying the entered text
            st.write(user_text)
    

if option == 'Image':
    image=st.file_uploader("Upload an image",type= ['jpeg','png','jpg'])
    
    if image:
        with st.sidebar:
            st.subheader("IMAGE 🏞️")
            #displaying the image
            st.image(image, caption = "Uploaded Image")


    
    
