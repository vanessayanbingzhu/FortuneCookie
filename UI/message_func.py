import streamlit as st

bot_avatar = "https://static.vecteezy.com/system/resources/previews/013/153/367/original/cute-robot-cartoon-icon-illustration-technology-robot-icon-concept-isolated-premium-flat-cartoon-style-vector.jpg"
user_avatar="https://cdn4.iconfinder.com/data/icons/cute-minimal-geometric-cartoon-avatars/100/b-512.png"
# user_avatar = "https://static.vecteezy.com/system/resources/previews/037/336/395/original/user-profile-flat-illustration-avatar-person-icon-gender-neutral-silhouette-profile-picture-free-vector.jpg"
# user_avatar = 'asset/echo_avatar1.jpeg'
# bot_avatar = 'asset/user_avatar.jpeg'

def message_format(message):
    text = message['content']
    if message['role'] == 'user':
       message_alignment = "flex-end"
       message_bg_color = "linear-gradient(135deg, #00B2FF 0%, #C5EAFA 100%)"
       avatar_class = "user_avatar"
       st.write(
          f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                    <div style="background: {message_bg_color}; color: white; border-radius: 20px; padding: 10px; margin-right: 5px; max-width: 75%; font-size: 14px;">
                        {text} \n </div>
                    <img src="{user_avatar}" class="{avatar_class}" alt="avatar" style="width: 50px; height: 50px;" />
                </div>
                """,
            unsafe_allow_html=True, 
       )
    elif message['role'] == 'assistant':
        message_alignment = "flex-start"
        message_bg_color = "#DEDEDE"
        avatar_class = "bot-avatar"

        st.write(
            f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px; justify-content: {message_alignment};">
                    <img src="{bot_avatar}" class="{avatar_class}" alt="avatar" style="width: 80px; height: 80px;" />
                    <div style="background: {message_bg_color}; color: black; border-radius: 20px; padding: 10px; margin-right: 5px; margin-left: 5px; max-width: 75%; font-size: 14px;">
                        {text} \n </div>                    
                </div>
                """,
            unsafe_allow_html=True,
        )