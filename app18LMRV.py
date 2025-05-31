import streamlit as st
from openai import OpenAI

st.sidebar.title("💬 Carga tu tarea.")

st.sidebar.write("Sigue las instrucciones para cargar tu archivo.")
st.sidebar.write("Sube tu tarea y haz preguntas sobre ella.")
st.sidebar.image("escudo.png")

openai_api_key = st.secrets["api_key"]
client = OpenAI(api_key=openai_api_key)

# Subida del archivo de texto
archivo = st.sidebar.file_uploader("Carga tu archivo.", type="txt")
if archivo is None:
    st.sidebar.info("💡 Esperando archivo...")
    st.stop()

# Leer contenido del archivo
contexto_local = archivo.read().decode("utf-8")

# Entrada del usuario
prompt = st.sidebar.chat_input("Haz tu pregunta sobre modelos GPT...")
if prompt is None:
    st.stop()

# Mostrar entrada del usuario
with st.sidebar.chat_message("user", avatar="🦖"):
    st.markdown(prompt)

# Consulta a OpenAI con el contexto
stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"Usa el siguiente contexto para responder:\n\n{contexto_local}"},
        {"role": "user", "content": prompt}
    ],
    max_tokens=800,
    temperature=0,
)

respuesta = stream.choices[0].message.content
with st.sidebar.chat_message("assistant"):
    st.write(respuesta)
