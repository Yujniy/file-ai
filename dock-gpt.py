import streamlit as st
import pyperclip

@st.cache_data
def copy_to_clipboard(text):
    pyperclip.copy(text)
    return text

def main():
    st.title("File Content Viewer")
    uploaded_files = st.file_uploader("Upload your files", accept_multiple_files=True)

    if uploaded_files:
        # Create a string to store the file names and contents
        file_content = ""
        for uploaded_file in uploaded_files:
            # Read the file content
            content = uploaded_file.read().decode("utf-8")
            # Append the file name and content to the file_content string
            file_content += f"File: {uploaded_file.name}\n\n{content}\n\n"

        # Display the file names and contents using st.code()
        st.code(file_content, language="text")

if __name__ == "__main__":
    main()
