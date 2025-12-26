import streamlit as st
import os
from datetime import datetime
import re
import io
from dotenv import load_dotenv
import streamlit.components.v1 as components



# Load environment variables from .env file
load_dotenv()

# Retrieve admin credentials from environment variables
admin_username = os.getenv("ADMIN_USERNAME")
admin_password = os.getenv("ADMIN_PASSWORD")

st.set_page_config(page_title="Um afiliado no Brasil", page_icon=":memo:", initial_sidebar_state="collapsed",)

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            .streamlit-ico {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

@st.cache(allow_output_mutation=True)
def enable_indexability():
    meta_tags = {
        'robots': 'index,follow',
        'googlebot': 'index,follow',
        'description': 'Blog - Um afiliado no Brasil',
        'keywords': 'afiliado, marketing, dicas, ofersas, nutra',
        'google-site-verification': 'sJbVjLAelpAAjiePKc8Monk8R4V1ppa-ytXMAzYBCUk'
    }

    for name, content in meta_tags.items():
        st.write(f"<meta name='{name}' content='{content}'>", unsafe_allow_html=True)

    st.write("<link rel='canonical' href='https://umafiliadonobrasil.onrender.com/blog' />", unsafe_allow_html=True)


# Display the Google Analytics code


st.markdown('<h1 style="margin-bottom:0rem;margin-top:-4rem;text-align: center">Um afiliado no Brasil</h1>', unsafe_allow_html=True)
st.markdown('<h5 style="color:grey;margin-bottom:0rem;margin-top:-1rem;text-align: center">Vivência de um afiliado no Brasil</h5>', unsafe_allow_html=True)

# Specify the name of the custom folder in the root directory
custom_folder_name = "itens"

# Get the current directory

current_dir = os.path.join(custom_folder_name)

# Function to display blog post
def display_blog_post(title, date, content):

        # Find image links in the content
    image_links = find_image_links(content)

        # Display images using st.image
    for image_link in image_links:
        st.image(image_link, caption="Image", use_column_width=True)

        # Remove image links from content
    content = remove_image_links(content)

    st.markdown(content)
    st.markdown('---------')


# Function to find image links in the content
def find_image_links(content):
    # Use regular expression to find image links in Markdown format
    pattern = r"!\[[^\]]*\]\((.*?)\)"
    matches = re.findall(pattern, content)
    return matches


    # Function to remove image links from the content
def remove_image_links(content):
    # Use regular expression to remove image links in Markdown format
    pattern = r"!\[[^\]]*\]\((.*?)\)"
    replaced_content = re.sub(pattern, "", content)
    return replaced_content


    # Function to save blog post as Markdown file
def save_blog_post(title, content, image, date):
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"{timestamp}_{title.replace(' ', '_')}.md"
    file_path = os.path.join(current_dir, filename)

    # Save Markdown file
    with io.open(file_path, "w", encoding="utf-8") as file:
        file.write(f"# {title}\n\n")
        file.write(f"Publicado  {date}\n\n")
        file.write(content)

    # Save uploaded image
    if image is not None:
        image_filename = f"{timestamp}_{title.replace(' ', '_')}.{image.name.split('.')[-1]}"
        image_path = os.path.join(current_dir, image_filename)
        with open(image_path, "wb") as img_file:
            img_file.write(image.getvalue())

        # Update Markdown content with image link
        image_link = f"![Uploaded Image](./itens/{image_filename})"
        new_content = f"{image_link}\n\n{content}"
        with io.open(file_path, "w", encoding="utf-8") as file:
            file.write(f"# {title}\n\n")
            file.write(f"Publicado  {date}\n\n")
            file.write(new_content)

    st.success("Blog post saved successfully!")

def load_blog_posts():
    posts = []
    files = sorted(os.listdir(current_dir))  # Get the list of files in the directory
    for file_name in files:
        if file_name.endswith(".md"):
            file_path = os.path.join(current_dir, file_name)
            with io.open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                if len(lines) >= 3:
                    title = lines[0].strip("# \n")
                    date_line = lines[1].strip("Publicado  ")
                    try:
                        date = datetime.strptime(date_line, "%Y-%m-%d").date()
                    except ValueError:
                        date = datetime.min.date()  # Set default value for invalid dates
                    content = "".join(lines[2:])
                    posts.append((title, date, content))
    return posts


    # Session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

st.sidebar.text("Login")

# Login

if not st.session_state.logged_in:
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Log In") and username == admin_username and password == admin_password:
        st.session_state.logged_in = True


# Check if user is logged in
def is_logged_in():
    return st.session_state.logged_in


# Log Out button
if is_logged_in():
    if st.sidebar.button("Log Out"):
        st.session_state.logged_in = False

# Blog title
st.markdown("---")

# Create new blog post (logged-in users)
if is_logged_in():
    st.subheader("Create New Blog Post")

    # Title input
    new_post_title = st.text_input("Title ")
    if not new_post_title:
        st.warning("Please enter a title for the blog post.")

    # Content input
    new_post_content = st.text_area("Content:")
    if not new_post_content:
        st.warning("Please enter the content for the blog post.")

    # Image upload
    uploaded_image = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

    # Display uploaded image
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Publish button
    if st.button("Publish", key="publish_button"):
        if new_post_title and new_post_content:
            new_post_date = datetime.now().strftime("%Y-%m-%d")
            save_blog_post(new_post_title, new_post_content, uploaded_image, new_post_date)
            # Pass uploaded_image as an argument
            st.success("Blog post published successfully!")
            # Clear the input fields after publishing
            new_post_title = ""
            new_post_content = ""
            uploaded_image = None  # Reset the uploaded image
        else:
            st.error("Please enter both a title and content for the blog post.")

    st.markdown("---")


posts = load_blog_posts()

sorted_posts = sorted(posts, key=lambda x: x[1], reverse=True)

if sorted_posts:
    for post in sorted_posts:
        display_blog_post(post[0], post[1], post[2])
else:
    st.info("No blog posts found.")



# Footer
st.markdown(
    """
    <style>
    .footer {
        padding: 20px;
        text-align: center;
    }
    .footer a {
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="footer">
        <p>Informação de contato:</p>
        <p>Email: <a href="contato.afiliados@adcombo.com">contato.afiliados@adcombo.com</a></p>
        <p>Skype: Ivan_AdCombo</p>
        <p>Tg: Ivan_AdCombo</p>
     </div>
    """,
    unsafe_allow_html=True
)
