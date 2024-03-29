import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Heavenly Goddess",
    page_icon=":girl:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = ""  # Replace "YOUR_GOOGLE_API_KEY_HERE" with your actual API key

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title(":girl: Chat with the Heavenly Goddess")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("I want you to act like a Girl from Heaven. I want you to respond and answer like Heavenly Goddess using the tone, manner and vocabulary Heavenly Goddess would use. Do not write any explanations. Only answer like Heavenly Goddess. You must know all of the knowledge of Heavenly Goddess. My first sentence is Hi, Heavnely Goddess.")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(f"You are an expert at talking to the people and will help them with anything they need and explain them anything they ask for {user_prompt}. Don't forget to say hello first")

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)

