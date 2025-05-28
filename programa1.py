import streamlit as st
st.title("Caja de sorpresas Checkbox")

# Widget: checkbox
mostrar = st.checkbox("Haz click aquí")

if mostrar:
    st.success("🎉 ¡Sorpresa!")
    st.balloons()
    st. write ("Tengo algo para ti")

    import streamlit as st

# Columnas con imagenes
import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    st.header("un oso")
    st.image("https://www.amigurumistore.com/wp-content/uploads/2019/11/Oso-Grande-Blanco-Amigurumi-Patron-Gratis-Paso-a-Paso-3.jpg")

with col2:
    st.header("Patrones gratis!")
    st.image("https://img77.uenicdn.com/image/upload/v1576164667/service_images/shutterstock_1099382681.jpg")

with col3:
    st.header("ánimate a tejer!")
    st.image("https://patronamigurumi.top/wp-content/uploads/tortuga.jpg")

    # Cargar Archivos
import streamlit as st
import pandas as pd

st.title("Carga imágenes de tus proyectos en jpg")

# Widget: file_uploader
archivo = st.file_uploader("Sube un archivo jpg", type="jpg")

if archivo:
       st.success("si cargó la imagen!")

