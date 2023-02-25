import streamlit as st

# Set page title and icon
st.set_page_config(page_title="My Streamlit App", page_icon=":wave:")

# Define the greeting message
message = "Hello everyone, welcome to my Streamlit app! You can find me on LinkedIn by clicking the link below:"

# Define the LinkedIn URL
linkedin_url = "www.linkedin.com/in/harshmalik424"

# Add a header with the greeting message
st.header(message)

# Add a link to your LinkedIn profile
st.markdown(f'<a href="{linkedin_url}" style="font-size: 24px;">LinkedIn</a>', unsafe_allow_html=True)

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
