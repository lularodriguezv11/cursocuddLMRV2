import streamlit as st
from openai import OpenAI
import PyPDF2  # Para leer PDFs
import docx  # Para leer Word

# Configuración inicial
st.set_page_config(page_title="Asistente Universitario 📚", page_icon="🎓")

# Sidebar (barra lateral)
st.sidebar.title("🎓 Asistente de Tareas")
st.sidebar.write("Sube tu tarea y haz preguntas sobre ella.")
st.sidebar.image("https://via.placeholder.com/150x150.png?text=LOGO", width=100)  # Reemplaza con tu imagen

# Conexión con OpenAI (usa tus credenciales)
openai_api_key = st.sidebar.text_input("Ingresa tu API Key de OpenAI", type="password")
if not openai_api_key:
    st.warning("🔑 Necesitas una API Key para continuar.")
    st.stop()

client = OpenAI(api_key=openai_api_key)

# Subida de archivos (PDF, Word o TXT)
archivo = st.file_uploader(
    "📤 Sube tu tarea (PDF, DOCX o TXT)",
    type=["txt", "pdf", "docx"],
    help="Formatos soportados: .txt, .pdf, .docx"
)

if not archivo:
    st.info("📂 Esperando tu archivo...")
    st.stop()

# Leer el contenido del archivo según su tipo
def leer_archivo(archivo):
    if archivo.type == "text/plain":
        return archivo.read().decode("utf-8")
    elif archivo.type == "application/pdf":
        lector = PyPDF2.PdfReader(archivo)
        texto = ""
        for pagina in lector.pages:
            texto += pagina.extract_text()
        return texto
    elif archivo.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(archivo)
        return "\n".join([parrafo.text for parrafo in doc.paragraphs])
    else:
        st.error("Formato no soportado ❌")
        st.stop()

contexto_tarea = leer_archivo(archivo)

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
