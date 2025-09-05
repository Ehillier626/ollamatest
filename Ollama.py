import ollama
import streamlit as st


# Use Ollama to analyze the image with Llama 3.2-Vision
upload = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# function feeds image data into ollama


Prompt = open("Prompt.txt")


def llm_read(image_data):

    response = ollama.chat(
        model="gemma3:4b",
        messages=[{
            "role": "user",
            "content": Prompt,
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
