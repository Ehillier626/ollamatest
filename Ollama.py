import ollama
import streamlit as st


# Use Ollama to analyze the image with Llama 3.2-Vision
upload = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# function feeds image data into ollama


def llm_read(image_data):

    response = ollama.chat(
        model="llama3.2-vision",
        messages=[{
            "role": "user",
            "content": "Please Extract all relevant resume information from the uploaded image."
            " If it doesn't look like a resume please inform user. Relevant info would be"
            "things like experience, phone and email, please put all info you "
            "find into a table with catagories for each",
            "images": [image_data]
        }]
    )
    cleaned_text = response['message']['content'].strip()
    return cleaned_text


# If image is uploaded, call llm_read, return response


if upload is not None:
    image_data = upload.read()
    if st.button("run model"):
        response = llm_read(image_data)
        st.write(response)
