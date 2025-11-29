# CS50-Final_Project

#### Video Demo: [Video](https://youtu.be/HMzdar7v1oA?si=-CXDyXdrdDfABQp6)

#### Live on: [App](https://projectpy-hjvgyzprbcqqgbzsudewiv.streamlit.app/)

#### Description:

This project is a web application that I built using Streamlit and the Google Gemini API. It's designed to help users understand and test their knowledge of Bible verses.

There are three main features:

1.  **Get Verse Text:** You can enter a Bible verse reference (like "John 3:16"), and the app will fetch and display the full text of that verse.
2.  **Verse Explainer:** After fetching a verse, the app can provide a simple and easy-to-understand explanation of what the verse means.
3.  **Truth Finder:** This feature lets you test your own understanding. You can write your own explanation for a verse, and the app will use the Gemini API to tell you if your explanation is "True" or "False".

### Use Cases:

- **For Students:** Quickly look up verses for a paper or study guide.
- **For Teachers:** Prepare for a lesson by getting a simple explanation of a verse.
- **For Personal Study:** Test your own understanding of a verse and get immediate feedback.
- **For a Friend:** Easily share a verse and its explanation with someone who is curious.

To run this project, you'll need to have Python and Streamlit installed. You'll also need to get a Gemini API key and store it in a `.env` file in the project's root directory.

To start the app, run the following command in your terminal:

```
streamlit run project.py
```
