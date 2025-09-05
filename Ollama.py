import ollama
import streamlit as st


# Use Ollama to analyze the image with Llama 3.2-Vision
upload = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

# function feeds image data into ollama


def llm_read(image_data):

    response = ollama.chat(
        model="gemma3:4b",
        messages=[{
            "role": "user",
            "content": "Please Extract all relevant resume information from "
            "the uploaded image."
            " If it doesn't look like a resume please inform user."
            " Relevant info would be"
            "things like experience, phone and email, please put all info you "
            "find into a table with catagories for each."
            " Make sure to get as much relevant info as possible."
            " Do not add any duplicates or additional notes"
            "Only list relevant info NO extra information or notes at all"
            "Keep it concise"
            "if There is no data for specific criteria then don't add it to the table"
            "DO NOT ADD A LARGE AMOUNT OF TABLES (MORE THAN 10) AND MAKE SURE EACH TABLE DOES NOT JUST SAY NONE",
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
