import streamlit as st
from openai import OpenAI

st.sidebar.title("💬 Carga tu tarea.")

st.sidebar.write("Sigue las instrucciones para cargar tu archivo.")
st.sidebar.write("Sube tu tarea y haz preguntas sobre ella.")
st.sidebar.image("escudo.png")

openai_api_key = st.secrets["api_key"]
client = OpenAI(api_key=openai_api_key)

# Subida del archivo de texto
archivo = st.sidebar.file_uploader("📤 Sube tu tarea (PDF o TXT)", type=["pdf", "txt"])

def leer_archivo(archivo):
    try:
        if archivo.type == "text/plain":
            return archivo.read().decode("utf-8")
        
        elif archivo.type == "application/pdf":
            pdf_reader = PyPDF2.PdfReader(archivo)
            return "\n".join([page.extract_text() for page in pdf_reader.pages])
        
        else:
            st.error("Formato no soportado")
            return None
            
    except Exception as e:
        st.error(f"Error al leer {archivo.name}: {str(e)}")
        return None

# Uso:
contexto_local = leer_archivo(archivo)
if contexto_local is None:
    st.stop()  # Detiene la ejecución si hay errores

# Entrada del usuario
prompt = st.chat_input("Haz tu pregunta sobre modelos GPT...")
if prompt is None:
    st.stop()

# Mostrar entrada del usuario
with st.chat_message("user", avatar="🦖"):
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
with st.chat_message("assistant"):
    st.write(respuesta)

  


