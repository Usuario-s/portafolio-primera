import streamlit as st
from PIL import Image

# =========================
# CONFIGURACIÓN
# =========================

st.set_page_config(
    page_title="Portafolio de aplicaciones",
    page_icon="💻",
    layout="wide"
)

# =========================
# DISEÑO / CSS
# =========================

st.markdown("""
<style>

    /* Fondo general */
    .stApp {
        background: #f5f7fb;
    }

    /* Contenedor principal */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1400px;
    }

    /* Título principal */
    h1 {
        font-size: 42px !important;
        font-weight: 800 !important;
        color: #172033 !important;
        margin-bottom: 5px !important;
    }

    /* Subtítulos */
    h2, h3 {
        color: #202938 !important;
    }

    /* Texto */
    p {
        color: #596273;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #172033;
    }

    section[data-testid="stSidebar"] h3 {
        color: white !important;
    }

    section[data-testid="stSidebar"] p {
        color: #d9deea !important;
        line-height: 1.7;
    }

    /* Línea decorativa */
    .linea {
        height: 4px;
        width: 80px;
        background: #6c63ff;
        border-radius: 20px;
        margin-bottom: 30px;
    }

    /* Tarjetas */
    .card {
        background: white;
        border-radius: 18px;
        padding: 22px;
        margin-bottom: 25px;
        box-shadow: 0px 6px 20px rgba(23, 32, 51, 0.08);
        border: 1px solid #e8ebf2;
        transition: all 0.25s ease;
    }

    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0px 12px 30px rgba(23, 32, 51, 0.14);
    }

    /* Título de las apps */
    .card-title {
        font-size: 21px;
        font-weight: 750;
        color: #202938;
        margin-bottom: 12px;
    }

    /* Descripción */
    .card-description {
        font-size: 15px;
        color: #697386;
        line-height: 1.5;
        min-height: 45px;
    }

    /* Botón */
    .boton {
        display: inline-block;
        background: #6c63ff;
        color: white !important;
        padding: 9px 17px;
        border-radius: 9px;
        text-decoration: none !important;
        font-weight: 600;
        font-size: 14px;
        margin-top: 8px;
        transition: 0.2s;
    }

    .boton:hover {
        background: #5148e5;
        color: white !important;
    }

    /* Separador de columnas */
    .columna {
        padding: 5px;
    }

    /* Enlace Github */
    .github-box {
        background: white;
        padding: 20px 25px;
        border-radius: 15px;
        border: 1px solid #e5e8ef;
        box-shadow: 0px 4px 15px rgba(23, 32, 51, 0.06);
        margin-bottom: 35px;
    }

</style>
""", unsafe_allow_html=True)


# =========================
# SIDEBAR
# =========================

with st.sidebar:
    st.subheader("Aplicaciones con Streamlit, GitHub, Python.")

    parrafo = (
        "Aplicaciones hechas en el proceso del curso. "
        "Se han aprendido nuevas e interesantes herramientas para aplicar "
        "todo con el fin de entender mejor este tipo de tecnologías."
    )

    st.write(parrafo)


# =========================
# ENCABEZADO
# =========================

st.title("Portafolio de seguimiento - Aplicaciones.")
st.markdown('<div class="linea"></div>', unsafe_allow_html=True)


# =========================
# GITHUB
# =========================

url_ia = "https://github.com/Usuario-s?tab=repositories"

st.markdown("""
<div class="github-box">
    <h3>Repositorio de proyectos</h3>
    <p>
        En el siguiente enlace puedes consultar los repositorios
        y proyectos desarrollados durante el curso.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<a class="boton" href="{url_ia}" target="_blank">Ver repositorios en GitHub ↗</a>',
    unsafe_allow_html=True
)

st.write("")


# =========================
# COLUMNAS
# =========================

col1, col2, col3 = st.columns(3)


# ============================================================
# COLUMNA 1
# ============================================================

with col1:

    # APP 1
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Primera app de texto</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen1.png")
    st.image(image, width=190)

    st.markdown(
        '<div class="card-description">Mi primera app en Streamlit</div>',
        unsafe_allow_html=True
    )

    url = "https://intro-app-1-su8r5tpxlwpwnflpltft2y.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">Abrir aplicación ↗</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # APP 2
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Reconocimiento de Objetos</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen2.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="card-description">'
        'En la siguiente enlace veremos como se detectan objetos en Imágenes.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://miaahora-fjj6fujljb6rzv2zwvzoat.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">Abrir aplicación ↗</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # APP 3
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Traductor</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen3.png")
    st.image(image, width=200)

    st.markdown(
        '<div class="card-description">'
        'Podrás traducir lo que dices a varios idiomas.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://traductor-multimodales-msvwvk3xeyowm3ofhsebtq.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">Abrir aplicación ↗</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# COLUMNA 2
# ============================================================

with col2:

    # APP 4
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Imagen a texto</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen4.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="card-description">'
        'Aquí verán reconocimiento de imágenes para reconocer el texto de ellas.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://ocr-imagen-1-hjea2xr4z9ddlpyoibf4pb.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">Abrir aplicación ↗</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # APP 5
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Reconocimiento de caracteres</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen5.jpg")
    st.image(image, width=190)

    st.markdown(
        '<div class="card-description">'
        'Un reconocimiento de caracteres con datos.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://ocr-audio-traductor-2-suib88gv4xbfrjn33prrb8.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">Abrir aplicación ↗</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # APP 6
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Worldcloud Studio</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen6.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="card-description">'
        'Una nube de palabras.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://wordcloudmio-dpzz2zwohcpixhtiqhfefz.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">Abrir aplicación ↗</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# COLUMNA 3
# ============================================================

with col3:

    # APP 7
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Consultorio psicológico</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen7.jpg")
    st.image(image, width=190)

    st.markdown(
        '<div class="card-description">'
        'En base a una frase te diremos el mood de tu día.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://sentimentpsic-nmnxejormvmhg8vgjeajm6.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">Abrir aplicación ↗</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # APP 8
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Demo TF-IDF</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen8.png")
    st.image(image, width=200)

    st.markdown(
        '<div class="card-description">'
        'Preguntas y lectura de documentos.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://espa-ol-espa-ol-pryjfznrx6oev7g57t7nok.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">Abrir aplicación ↗</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # APP 9
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Detección de objetos en imágenes</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen9.png")
    st.image(image, width=200)

    st.markdown(
        '<div class="card-description">'
        'Detecta cualquier objeto con tu cámara.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://yolov5555-xx2ljp8ij9xinsthel5juu.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">Abrir aplicación ↗</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # APP 10
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Reconocimiento de imágenes</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen10.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="card-description">'
        'Toma una foto y te dirá todo.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://tm-detection-npqnkslgj6ps87sj9fvtre.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">Abrir aplicación ↗</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)

