import streamlit as st
import os
from matplotlib import image
# Set page title and icon
st.set_page_config(page_title="My Streamlit App", page_icon=":wave:")
message = "Hello everyone :wave:"
st.title(message)
st.header("Welcome to my Streamlit app! You can find me on :blue[LinkedIn] by clicking the link below:")

# Define the LinkedIn URL
linkedin_url = "www.linkedin.com/in/harshmalik424"
# Add a link to your LinkedIn profile
st.markdown(f'<a href="{linkedin_url}" style="font-size: 30px;">LinkedIn</a>', unsafe_allow_html=True)

# Apply some styling to the link and background color
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    a {
        color: #0084b4;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.subheader("Lets connect and grow together! :sunglasses:")

btn_click = st.button("Click Me!")



image_dir = 'C:/Users/harsh/Desktop/Intern/project2/resources/images/f_img.jpg'
image_name = 'f_img.jpsg'
image_path = os.path.join(image_dir, image_name)




if btn_click == True:
    # Display the image using Streamlit
    st.image(image_path, use_column_width=True)