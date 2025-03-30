import requests
import streamlit as st

api_key = "keLvyxg1cnWlfHzkUbyAyBXp4vdv0uoZcKyN7nxY"
url = (f"https://api.nasa.gov/planetary/apod?"
       f"api_key={api_key}")

# Make request
request1 = requests.get(url)

# Get a dictionary with data
content = request1.json()

# Access title, url and explanation
title = content["title"]
image_url = content["url"]
explanation = content["explanation"]

#Download the image
image_filepath = "img.png"
request2 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(request2.content)

st.title(title)
st.image(image_filepath)
st.write(explanation)
