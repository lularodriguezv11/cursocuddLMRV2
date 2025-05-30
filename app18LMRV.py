import streamlit as st
from openai import OpenAI

st.sidebar.title("💬 Carga tu tarea de Fisicoquímica.")

st.sidebar.write("Sigue las instrucciones para cargar tu archivo.")
st.sidebar.write("Sube tu tarea y haz preguntas sobre ella.")
st.sidebar.image("escudo.png")

openai_api_key = st.secrets["api_key"]
client = OpenAI(api_key=openai_api_key)

# Subida del archivo de texto
archivo = st.sidebar.file_uploader("📤 Sube tu tarea (PDF, DOCX o TXT)",
    type=["txt", "pdf", "docx"],
    help="Formatos soportados: .txt, .pdf, .docx")

if archivo is None:
    st.sidebar.info("💡 Esperando archivo...")
    st.success("✅ Archivo cargado correctamente. ¡Puedes hacer preguntas sobre tu tarea!")
prompt = st.chat_input("Ej: ¿Cuál es el objetivo principal de esta tarea?")
  

# Leer contenido del archivo
contexto_local = archivo.read().decode("utf-8")

# Chat interactivo
st.success("✅ Archivo cargado correctamente. ¡Puedes hacer preguntas sobre tu tarea!")
prompt = st.chat_input("Ej: ¿Cuál es el objetivo principal de esta tarea?")

if prompt:
    # Mostrar pregunta del usuario
    with st.chat_message("user", avatar="🎓"):
        st.markdown(prompt)

    # Consultar a OpenAI con el contexto de la tarea
    respuesta = client.chat.completions.create(
        model="gpt-4-turbo",  # o "gpt-3.5-turbo" si prefieres
        messages=[
            {"role": "system", "content": f"Eres un asistente universitario. Usa este contexto para responder:\n\n{contexto_tarea}"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3  # Para respuestas más precisas
    ).choices[0].message.content

    # Mostrar respuesta del asistente
    with st.chat_message("assistant", avatar="🤖"):
        st.write(respuesta)

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
with st.chat_message("assistant"):
    st.write(respuesta)
