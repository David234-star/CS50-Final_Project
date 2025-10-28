# Bible verse Knowledge And Explainer using AI models

# Import necessary libraries
import streamlit as st
import google.generativeai as genai
import os


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


def is_bible_verse(reference):
    """Checks if a string is a plausible Bible verse reference using the Gemini API."""
    # A simple pre-check to avoid unnecessary API calls for clearly invalid input
    if ':' not in reference and not any(char.isdigit() for char in reference):
        return False

    prompt = f"Is the following text a plausible Bible verse reference? '{reference}'. Respond with only 'Yes' or 'No'."
    model = genai.GenerativeModel('gemini-pro-latest')
    try:
        response = model.generate_content(prompt)
        return 'yes' in response.text.lower()
    except Exception:
        # If the API fails for some reason, fall back to a simple check
        return ':' in reference


def main():
    """Main function to run the Streamlit app."""

    # --- Pixel Retro CSS ---
    custom_css = """
    <style>
        /* --- General & Background --- */
        .stApp {
            background-color: #212121; /* Dark grey background */
            font-family: 'Courier New', monospace; /* Pixel-style font */
        }

        /* --- Main Title --- */
        .header-title {
            background-color: #424242;
            color: #FFFFFF;
            border: 4px double #FFFFFF;
            padding: 1rem;
            text-align: center;
            font-size: 2.5em;
            border-radius: 0;
            margin-bottom: 1rem;
        }

        /* --- Subheaders --- */
        .subheader-style {
            background-color: #616161;
            color: #FFFFFF;
            padding: 0.5rem;fsubheader-style
            font-size: 1.5em;
            text-align: center;
            border-radius: 0;
            margin-bottom: 1rem;
        }

        # /* --- Input Card --- */
        # .card {
        #     background-color: #424242;
        #     border: 4px double #BDBDBD;
        #     border-radius: 0;
        #     padding: 25px;
        #     margin-top: 1rem;
        #     margin-bottom: 1rem;
        # }

        /* --- Output Card (for generated text) --- */
        .output-card {
            background-color: #E0E0E0; /* Light grey background for readability */
            border: 4px double #000000;
            border-radius: 0;
            padding: 25px;
            margin-top: 1rem;
            margin-bottom: 1rem;
        }

        /* --- Generated Text (Classic Style) --- */
        .generated-text {
            color: #000000 !important; /* Black text */
            font-family: "Times New Roman", Times, serif;
            font-size: 1.2em;
            background-color: #FFFFFF;
            padding: 1rem;
            border: 2px solid #000000;
        }

        /* --- Warning Messages --- */
        .stAlert {
            background-color: #424242;
            border: 4px double #FFCC00;
            border-radius: 0;
        }
        .stAlert .st-emotion-cache-1wmy9hl a {
            color: #FFFFFF !important;
        }

        /* --- Input & Button Styles --- */
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {
            background-color: #E0E0E0;
            border: 2px solid #000000;
            border-radius: 0;
            color: #000000;
            font-family: 'Courier New', monospace;
        }
        .stButton>button {
            border: 4px outset #BDBDBD;
            background-color: #757575;
            color: #FFFFFF;
            padding: 10px 20px;
            border-radius: 0;
            font-weight: bold;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #9E9E9E;
        }
        .stButton>button:active {
            border-style: inset;
        }
    </style>
    """.strip()
    st.markdown(custom_css, unsafe_allow_html=True)

    # --- App Header ---
    st.markdown('<b><h3><p class="header-title">📖Bible Verse Knowledge and Explainer using AI🤖</p></h3></b>',
                unsafe_allow_html=True)

    # Initialize session state
    if 'verse_text' not in st.session_state:
        st.session_state.verse_text = ""
    if 'explanation' not in st.session_state:
        st.session_state.explanation = ""

    # Configure the Gemini API
    try:
        genai.configure(api_key="AIzaSyBZCSr2otpqNtM5pkwST-i1Fi15WJdN2Hg")
    except Exception as e:
        st.error(f"Error configuring the Gemini API: {e}")
        st.info("Please make sure you have a .env file with your GEMINI_API_KEY.")
        return

    # --- Input Card ---
    # st.markdown('<div class="card">', unsafe_allow_html=True)
    verse_reference = st.text_input(
        "Enter a Bible verse reference (e.g., John 3:16)(mention version as well e.g., KJV, NIV, ESV, etc):")
    user_explanation = st.text_area("Enter your explanation of the verse:")

    col1, col2 = st.columns(2)
    with col1:
        get_exp_button = st.button("Get Verse and Explanation")
    with col2:
        check_exp_button = st.button("Check My Explanation")
    # st.markdown('</div>', unsafe_allow_html=True)

    # --- Logic and Output ---
    if get_exp_button:
        if verse_reference:
            if is_bible_verse(verse_reference):
                with st.spinner('Fetching verse and explanation...'):
                    st.session_state.verse_text = get_verse_text(
                        verse_reference)
                    st.session_state.explanation = verse_explain(
                        st.session_state.verse_text)

                st.markdown('<div class="output-card">',
                            unsafe_allow_html=True)
                st.markdown(
                    '<p class="subheader-style">Verse Text:</p>', unsafe_allow_html=True)
                st.markdown(
                    f'<div class="generated-text">{st.session_state.verse_text}</div>', unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)

                st.markdown(
                    '<p class="subheader-style">Explanation:</p>', unsafe_allow_html=True)
                st.markdown(
                    f'<div class="generated-text">{st.session_state.explanation}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning(
                    "Invalid input. This app only processes Bible verse references (e.g., John 3:16).")
        else:
            st.warning("Please enter a Bible verse reference.")

    if check_exp_button:
        if verse_reference and user_explanation:
            if is_bible_verse(verse_reference):
                with st.spinner('Checking your explanation...'):
                    if not st.session_state.verse_text:
                        st.session_state.verse_text = get_verse_text(
                            verse_reference)
                    result = truth_finder(
                        st.session_state.verse_text, user_explanation)

                st.markdown('<div class="output-card">',
                            unsafe_allow_html=True)
                st.markdown(
                    '<p class="subheader-style">Is your explanation correct?</p>', unsafe_allow_html=True)
                st.markdown(
                    f'<div class="generated-text">{result}</div>', unsafe_allow_html=True)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.warning(
                    "Invalid input. This app only processes Bible verse references (e.g., John 3:16).")
        else:
            st.warning(
                "Please enter both a Bible verse reference and your explanation.")


if __name__ == "__main__":
    main()
