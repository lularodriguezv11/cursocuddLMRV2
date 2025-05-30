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

contexto_tarea = None
if archivo is not None:
    with st.sidebar.spinner("Procesando tu archivo..."):
        contexto_tarea = leer_archivo(archivo)

if contexto_tarea:
        st.sidebar.success("✅ Archivo cargado correctamente")
        st.sidebar.success("¡Puedes hacer preguntas sobre tu tarea!")

  


