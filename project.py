# Bible verse Knowledge And Explainer using AI models

# Import necessary libraries
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv


def get_verse_text(verse_reference):
    """Gets the text of a Bible verse using the Gemini API."""
    prompt = f"What is the text of the Bible verse {verse_reference}?"
    model = genai.GenerativeModel('gemini-pro-latest')
    response = model.generate_content(prompt)
    return response.text


def verse_explain(verse_text):
    """Explains a Bible verse in simple words using the Gemini API."""
    prompt = f"Explain the following Bible verse in simple terms:\n\n{verse_text}"
    model = genai.GenerativeModel('gemini-pro-latest')
    response = model.generate_content(prompt)
    return response.text


def truth_finder(verse_text, user_explanation):
    """Determines if a user's explanation of a Bible verse is true or false."""
    prompt = f"Based on the following Bible verse:\n\n{verse_text}\n\nIs the following explanation true or false?\n\n'{user_explanation}'\n\nRespond with only 'True' or 'False'."
    model = genai.GenerativeModel('gemini-pro-latest')
    response = model.generate_content(prompt)
    return response.text


def main():
    """Main function to run the Streamlit app."""
    load_dotenv()
    st.title("Bible Verse Knowledge and Explainer")

    # Initialize session state
    if 'verse_text' not in st.session_state:
        st.session_state.verse_text = ""
    if 'explanation' not in st.session_state:
        st.session_state.explanation = ""

    # Configure the Gemini API
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    except Exception as e:
        st.error(f"Error configuring the Gemini API: {e}")
        st.info("Please make sure you have a .env file with your GEMINI_API_KEY.")
        return

    # Get user input
    verse_reference = st.text_input(
        "Enter a Bible verse reference (e.g., John 3:16):")
    user_explanation = st.text_area("Enter your explanation of the verse:")

    if st.button("Get Verse and Explanation"):
        if verse_reference:
            # Get the verse text
            st.session_state.verse_text = get_verse_text(verse_reference)
            st.subheader("Verse Text:")
            st.write(st.session_state.verse_text)

            # Get the explanation
            st.session_state.explanation = verse_explain(
                st.session_state.verse_text)
            st.subheader("Explanation:")
            st.write(st.session_state.explanation)
        else:
            st.warning("Please enter a Bible verse reference.")

    if st.button("Check My Explanation"):
        if verse_reference and user_explanation:
            # Get the verse text
            if not st.session_state.verse_text:
                st.session_state.verse_text = get_verse_text(verse_reference)

            # Check the user's explanation
            result = truth_finder(
                st.session_state.verse_text, user_explanation)
            st.subheader("Is your explanation correct?")
            st.write(result)
        else:
            st.warning(
                "Please enter both a Bible verse reference and your explanation.")


if __name__ == "__main__":
    main()
