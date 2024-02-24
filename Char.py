import streamlit as st
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with your Favorite AI",
    page_icon=":girl:",  # Favicon emoji
    layout="centered",  # Page layout option
)

GOOGLE_API_KEY = "AIzaSyDFfw_oONfy9o1C9u55U1cnk53mnalIsvw"  # Replace with your actual API key

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

# Define example questions and their corresponding contexts
example_questions = [
    "What makes SubHub different from other social media platforms?",
    "How does SubHub use AI technology to enhance user experience?",
    "Can you explain how influencers customize their avatars on SubHub?",
    "What opportunities does SubHub offer for influencers to monetize their presence on the platform?",
    "How does SubHub target its audience, and why is it geared towards Gen Z and Millennial fans?",
    "Can you elaborate on the ways SubHub makes money, including subscription models and advertising?",
    "How do personalized bots on SubHub improve interaction between influencers and their followers?",
    "What role do bots play in content distribution on SubHub?",
    "How do bots on SubHub encourage audience engagement and community building?",
    "In what ways do bots on SubHub assist influencers in data collection and audience insights?",
    "How do bots on SubHub automate tasks for influencers, and why is this beneficial?",
    "Can you explain how influencers can monetize their presence on SubHub with the help of bots?",
    "Why is 24/7 availability important for bots on SubHub, and how does it benefit followers?"
]

example_contexts = [
    "SubHub stands out from other social media platforms because it focuses on providing a more personalized and interactive experience for both fans and influencers.",
    "SubHub leverages AI technology to tailor content and interactions based on user preferences, making the platform more engaging and enjoyable for everyone involved.",
    "Influencers on SubHub have the freedom to create and customize their own avatars, allowing them to express their unique personalities and connect with fans on a deeper level.",
    "SubHub offers various monetization opportunities for influencers, including selling merchandise, offering subscriptions, and promoting products or sponsored content.",
    "SubHub is designed to appeal to younger audiences, particularly Gen Z and Millennials, who are seeking authentic connections and meaningful interactions with their favorite influencers.",
    "SubHub generates revenue through subscription models, transaction fees, advertising, premium features, affiliate marketing, and sponsored content collaborations with brands.",
    "Personalized bots on SubHub facilitate real-time interactions between influencers and followers, providing timely updates, responses, and engagement opportunities.",
    "Bots play a crucial role in distributing content on SubHub by sharing updates, videos, articles, and other relevant content with followers, keeping them informed and engaged.",
    "Bots encourage audience engagement and community building on SubHub by facilitating interactive experiences such as polls, quizzes, and Q&A sessions.",
    "Bots help influencers collect valuable insights and feedback from followers, enabling them to better understand their audience demographics and preferences.",
    "Bots automate repetitive tasks for influencers on SubHub, such as scheduling posts, managing messages, and tracking analytics, freeing up time for more meaningful interactions.",
    "Influencers can monetize their presence on SubHub by leveraging bots to promote sponsored content, affiliate products, and exclusive deals to their followers.",
    "24/7 availability ensures that bots on SubHub can provide round-the-clock support and assistance to followers, enhancing the overall user experience and satisfaction."
]

# Function to generate responses based on user input
def generate_response(user_input):
    # Check if the user input is one of the example questions
    if user_input in example_questions:
        # Get the index of the question in the list
        question_index = example_questions.index(user_input)
        # Retrieve the corresponding context for the question
        context = example_contexts[question_index]
        # Generate a response based on the question and context
        response = model.start_chat(history=[context, user_input])
        return response
    else:
        # Generate a general response if the user input is not an example question
        response = model.start_chat(history=[user_input])
        return response

# Display the chatbot's title on the page
st.title(":girl: Chat with your Favorite AI")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.text_input("Ask me anything:")
if user_prompt:
    if user_prompt.lower() == "example":
        # Display example questions
        st.write("Here are some example questions:")
        for question in example_questions:
            st.write("-", question)
    else:
        # Add user's message to chat and display it
        st.write("You:", user_prompt)
        # Generate response based on user input
        gemini_response = generate_response(user_prompt)
        # Display Gemini-Pro's response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.parts[0].text)
