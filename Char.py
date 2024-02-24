import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with your Favorite AI",
    page_icon=":girl:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = "AIzaSyDFfw_oONfy9o1C9u55U1cnk53mnalIsvw"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Function to generate response based on user input
def generate_response(user_input, chat_session):
    # Send user's message to Gemini-Pro and get the response
    gemini_response = chat_session.send_message(user_input)
    return gemini_response

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title(":girl: Chat with your Favorite AI")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_input = st.text_input("Ask me anything:")

# Function to handle user input and generate response
if user_input:
    # Add user's message to chat and display it
    with st.chat_message("user"):
        st.markdown(user_input)
    # Generate response based on user input
    gemini_response = generate_response(user_input, st.session_state.chat_session)
    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

