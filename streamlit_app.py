# Import required libraries
from dotenv import load_dotenv
from itertools import zip_longest

import streamlit as st
from streamlit_chat import message

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage


# Load environment variables
load_dotenv()

# Set streamlit page configuration
st.set_page_config(page_title="ChatBot Bimbingan Konseling")
st.title("ChatBot Bimbingan Konseling: Teman Virtual Anda")

# Initialize session state variables
if "generated" not in st.session_state:
    st.session_state["generated"] = []  # Store AI generated responses

if "past" not in st.session_state:
    st.session_state["past"] = []  # Store past user inputs

if "entered_prompt" not in st.session_state:
    st.session_state["entered_prompt"] = ""  # Store the latest user input


# Initialize the ChatOpenAI model
chat = ChatOpenAI(temperature=0.5, model_name="gpt-3.5-turbo")


def create_whatsapp_link(number, message):
    return f"https://api.whatsapp.com/send?phone={number}&text={message}"


def build_message_list():
    """
    Build a list of messages including system, human and AI messages.
    """
    # Start zipped_messages with the SystemMessage
    zipped_messages = [
        SystemMessage(
            content="A Professional Guidance and Counseling Assistant, equipped to guide students in personal, social, academic, and career-related concerns. If a question falls outside the realm of guidance counseling or the aforementioned areas, please respond with 'That's beyond my capabilities' or 'I cannot answer that'."
        )
    ]

    # Zip together the past and generated messages
    for human_msg, ai_msg in zip_longest(
        st.session_state["past"], st.session_state["generated"]
    ):
        if human_msg is not None:
            zipped_messages.append(HumanMessage(content=human_msg))  # Add user messages
        if ai_msg is not None:
            zipped_messages.append(AIMessage(content=ai_msg))  # Add AI messages

    return zipped_messages


def generate_response():
    """
    Generate AI response using the ChatOpenAI model.
    """
    # Build the list of messages
    zipped_messages = build_message_list()

    # Generate response using the chat model
    ai_response = chat(zipped_messages)

    return ai_response.content


# Define function to submit user input
def submit():
    # Set entered_prompt to the current value of prompt_input
    st.session_state.entered_prompt = st.session_state.prompt_input
    # Clear prompt_input
    st.session_state.prompt_input = ""


# Create a text input for user
st.text_input("Saya: ", key="prompt_input", on_change=submit)


# Get user query and check for trigger words within the same block
if st.session_state.entered_prompt != "":
    # Get user query
    user_query = st.session_state.entered_prompt

    # Append user query to past queries
    st.session_state.past.append(user_query)

    # Generate response
    output = generate_response()

    # Append AI response to generated responses
    st.session_state.generated.append(output)

    # Check for specific user keywords to trigger the report functionality
    trigger_words = [
        "laporkan",
        "pembulian",
        "pingin chat",
        "pribadi",
        "masalah keluarga",
    ]
    if any(word in user_query.lower() for word in trigger_words):
        whatsapp_number = "6281809460647"  # nomor tujuan Anda
        report_message = "Halo, saya ingin melaporkan tentang..."  # pesan awal yang akan muncul di chat WhatsApp
        link = create_whatsapp_link(whatsapp_number, report_message)

        if st.button("Laporkan Via WhatsApp"):
            st.write(
                f'<meta http-equiv="refresh" content="0; URL={link}">',
                unsafe_allow_html=True,
            )

# Display the chat history
if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        # Display AI response
        message(st.session_state["generated"][i], key=str(i))
        # Display user message
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")


# Add credit
st.markdown(
    """
---
 Selalu Hadir, Selalu Membimbing"""
)

# Sidebar
st.sidebar.title("ChatBot Bimbingan Konseling")
st.sidebar.subheader("Teman Virtual Anda")
st.sidebar.text(
    """
Platform ini dirancang untuk membantu siswa dengan 
pertanyaan-pertanyaan mengenai bimbingan konseling. 
Untuk menggunakannya, cukup ketikkan pertanyaan 
atau pernyataan Anda pada kotak chat dan Anda akan 
mendapatkan tanggapan dari ChatBot.
"""
)
with st.sidebar.expander("Butuh Bantuan Langsung?"):
    st.write(
        """
        Jika Anda menghadapi masalah serius seperti pembulian atau memerlukan bantuan langsung dari guru BK, Anda dapat menyampaikannya langsung melalui platform ini. 
        Ketik pesan Anda dan kami akan mengarahkan Anda untuk berkomunikasi langsung dengan guru BK melalui WhatsApp.
    """
    )
