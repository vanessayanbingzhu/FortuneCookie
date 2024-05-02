
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from app_config import *

# load_dotenv()
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

def generate_fortune():
    """Generate a fortune cookie quote using the language model."""
    # client = OpenAI(api_key=OPENAI_API_KEY)
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Write a fortune cookie message."}
        ],
        temperature=1.0,
        frequency_penalty=0.6
    )
    choices = response.choices[0]
    fortune = choices.message.content

    return fortune.replace('"', '')

def generate_response(prompt):
    """Generate a positive and uplifting response using the GPT-3.5-turbo model."""
    # Adding instructions for positivity to the prompt
    full_prompt = f"Respond with a positive and uplifting message to the following question: {prompt}"

    # st.session_state.messages.append({"role" : "user", "content": prompt})

    # client = OpenAI(api_key=OPENAI_API_KEY)
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Using the GPT-3.5-turbo model
        messages=[
            {"role": "system", "content": init_prompt},
            {"role": "user", "content": full_prompt}
        ],
        # prompt=full_prompt,
        # max_tokens=150,
        temperature=1.0,  # Lower temperature for more consistent output
        top_p=1.0,
        stop=["\n"],  # Stop generation at the first new line
        presence_penalty=0.6,  # Encourages the model to introduce new topics
        frequency_penalty=0.6   # Discourages repetitive responses
    )
    choices = response.choices[0]
    ans = choices.message.content

    # st.session_state.messages.append({"role": "assistant", "content": ans})
    return ans.replace('"', '')

# Adding an image to the sidebar
st.sidebar.image('https://www.redpathsugar.com/sites/redpathsugar_com/files/styles/m/public/Fortune_Cookies_500x400.jpg.webp?itok=-cFGivMC')
# st.sidebar.image('https://source.unsplash.com/1600x900/?lucky Cookie', caption='Fortune Cookie')
st.sidebar.title("🥠 Fortune Cookie")
if st.sidebar.button('Get my fortune!'):
    fortune = generate_fortune()
    st.sidebar.success(fortune)

# Main page for comforting chat
st.title('ECHO')
st.subheader('Always Here, Always Ready to Hear you')
# user_input = st.text_input("How are you feeling today?", "")
# if st.button('Talk to me'):
#     response = generate_response(user_input)
#     st.info(response)

if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Hi! I am Echo. How are you feeling today?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    msg = generate_response(prompt)
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)