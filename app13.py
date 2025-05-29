# mini bot
import streamlit as st

st.set_page_config(page_title="Ejemplo Chat", layout="centered")

st.title("💬 Mini Chatbot Simón dice!")

st.image("https://www.shutterstock.com/shutterstock/photos/2372683083/display_1500/stock-vector-cartoon-illustration-of-a-kids-playing-simon-says-2372683083.jpg")

# Entrada tipo chat (abajo de la pantalla)
user_input = st.chat_input("Tú primero!...")

# Si el usuario escribe algo, mostramos los mensajes
if user_input:
    # Mostrar el mensaje del usuario
    st.chat_message("user").write(user_input)

    # Mostrar una respuesta simple del asistente
    st.chat_message("assistant").write(f"{user_input} <- ahora yo!")
