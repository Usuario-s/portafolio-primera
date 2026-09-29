import streamlit as st
from PIL import Image

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Portafolio de Aplicaciones",
    page_icon="💻",
    layout="wide"
)

# =========================================================
# ESTILOS
# =========================================================

st.markdown("""
<style>

    /* =========================
       FONDO GENERAL
       ========================= */

    .stApp {
        background-color: #f4f8fc;
    }

    .main .block-container {
        max-width: 1400px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }


    /* =========================
       TÍTULOS
       ========================= */

    h1 {
        color: #0b2d4d !important;
        font-size: 42px !important;
        font-weight: 800 !important;
        letter-spacing: -1px;
        margin-bottom: 5px !important;
    }

    h2, h3 {
        color: #123b5d !important;
    }

    p {
        color: #536577;
    }


    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {
        background-color: #0b2d4d;
    }

    section[data-testid="stSidebar"] h3 {
        color: white !important;
        font-size: 20px !important;
    }

    section[data-testid="stSidebar"] p {
        color: #dceaf5 !important;
        line-height: 1.7;
    }


    /* =========================
       LÍNEA DECORATIVA
       ========================= */

    .linea {
        width: 75px;
        height: 5px;
        background: #1683d8;
        border-radius: 10px;
        margin-bottom: 28px;
    }


    /* =========================
       ENCABEZADO
       ========================= */

    .header-box {
        background: white;
        border-radius: 18px;
        padding: 28px 32px;
        margin-bottom: 25px;
        border: 1px solid #dce8f2;
        box-shadow: 0 5px 18px rgba(20, 70, 110, 0.06);
    }

    .header-title {
        font-size: 27px;
        font-weight: 750;
        color: #123b5d;
        margin-bottom: 7px;
    }

    .header-text {
        color: #607486;
        font-size: 15px;
        line-height: 1.6;
    }


    /* =========================
       TARJETAS
       ========================= */

    .card {
        background: #ffffff;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 22px;

        border: 1px solid #dce8f2;

        box-shadow:
            0px 5px 18px rgba(20, 70, 110, 0.07);

        transition: all 0.25s ease;
    }

    .card:hover {
        transform: translateY(-4px);

        box-shadow:
            0px 10px 28px rgba(20, 70, 110, 0.14);

        border-color: #9ccbea;
    }


    /* =========================
       TÍTULO DE APP
       ========================= */

    .card-title {
        color: #0b2d4d;
        font-size: 20px;
        font-weight: 750;
        margin-bottom: 13px;
    }


    /* =========================
       DESCRIPCIÓN
       ========================= */

    .card-description {
        color: #657789;
        font-size: 14px;
        line-height: 1.55;
        min-height: 45px;
        margin-top: 8px;
        margin-bottom: 8px;
    }


    /* =========================
       BOTONES
       ========================= */

    .boton {
        display: inline-block;

        background: #1683d8;
        color: white !important;

        padding: 9px 16px;

        border-radius: 9px;

        text-decoration: none !important;

        font-size: 14px;
        font-weight: 650;

        margin-top: 7px;

        transition: all 0.2s ease;
    }

    .boton:hover {
        background: #0b6db7;
        color: white !important;
    }


    /* =========================
       GITHUB
       ========================= */

    .github-box {
        background: white;

        border-left: 5px solid #1683d8;

        border-radius: 14px;

        padding: 20px 24px;

        margin-top: 10px;
        margin-bottom: 14px;

        border-top: 1px solid #dce8f2;
        border-right: 1px solid #dce8f2;
        border-bottom: 1px solid #dce8f2;

        box-shadow:
            0px 4px 15px rgba(20, 70, 110, 0.06);
    }

    .github-title {
        color: #123b5d;
        font-size: 20px;
        font-weight: 750;
        margin-bottom: 5px;
    }

    .github-text {
        color: #657789;
        font-size: 14px;
    }


    /* =========================
       ETIQUETA SUPERIOR
       ========================= */

    .badge {
        display: inline-block;

        background: #e5f3ff;
        color: #0873bd;

        padding: 6px 12px;

        border-radius: 20px;

        font-size: 12px;
        font-weight: 700;

        margin-bottom: 10px;
    }


    /* =========================
       FOOTER
       ========================= */

    .footer {
        text-align: center;

        margin-top: 35px;
        padding-top: 25px;

        border-top: 1px solid #dce8f2;

        color: #718394;

        font-size: 13px;
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.subheader("Aplicaciones con Streamlit, GitHub, Python.")

    parrafo = (
        "Aplicaciones hechas en el proceso del curso "
        "Se han aprendido nuevas e interesantes herramientas para aplicar "
        "Todo con el fin de entender mejor este tipo de tecnologías"
    )

    st.write(parrafo)


# =========================================================
# ENCABEZADO PRINCIPAL
# =========================================================

st.markdown(
    '<div class="badge">PORTAFOLIO ACADÉMICO</div>',
    unsafe_allow_html=True
)

st.title("Portafolio de seguimiento - Aplicaciones.")

st.markdown(
    '<div class="linea"></div>',
    unsafe_allow_html=True
)


# =========================================================
# GITHUB
# =========================================================

url_ia = "https://github.com/Usuario-s?tab=repositories"

st.markdown("""
<div class="github-box">

    <div class="github-title">
        Repositorios en GitHub
    </div>

    <div class="github-text">
        En el siguiente enlace puedes ver los repositorios
        desarrollados durante el proceso del curso.
    </div>

</div>
""", unsafe_allow_html=True)

st.markdown(
    f'<a class="boton" href="{url_ia}" target="_blank">'
    'Ver repositorios en GitHub ↗'
    '</a>',
    unsafe_allow_html=True
)

st.write("")


# =========================================================
# APLICACIONES
# =========================================================

col1, col2, col3 = st.columns(3, gap="large")


# =========================================================
# COLUMNA 1
# =========================================================

with col1:

    # -----------------------------------------------------
    # PRIMERA APP
    # -----------------------------------------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Primera app de texto</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen1.png")
    st.image(image, width=190)

    st.markdown(
        '<div class="card-description">'
        'Mi primera app en streamlit'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://intro-app-1-su8r5tpxlwpwnflpltft2y.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">'
        'Abrir aplicación ↗'
        '</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # -----------------------------------------------------
    # RECONOCIMIENTO DE OBJETOS
    # -----------------------------------------------------

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
        f'<a class="boton" href="{url}" target="_blank">'
        'Abrir aplicación ↗'
        '</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # -----------------------------------------------------
    # TRADUCTOR
    # -----------------------------------------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Traductor</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen3.png")
    st.image(image, width=200)

    st.markdown(
        '<div class="card-description">'
        'Podrás traducir lo que dices a varios idiomas'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://traductor-multimodales-msvwvk3xeyowm3ofhsebtq.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">'
        'Abrir aplicación ↗'
        '</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# COLUMNA 2
# =========================================================

with col2:

    # -----------------------------------------------------
    # IMAGEN A TEXTO
    # -----------------------------------------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Imagen a texto</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen4.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="card-description">'
        'Aquí verán reconocimiento de imágenes para reconocer el texto de ellas'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://ocr-imagen-1-hjea2xr4z9ddlpyoibf4pb.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">'
        'Abrir aplicación ↗'
        '</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # -----------------------------------------------------
    # RECONOCIMIENTO DE CARACTERES
    # -----------------------------------------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Reconocimiento de caracteres</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen5.jpg")
    st.image(image, width=190)

    st.markdown(
        '<div class="card-description">'
        'Un reconocimiento de caracteres con datos'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://ocr-audio-traductor-2-suib88gv4xbfrjn33prrb8.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">'
        'Abrir aplicación ↗'
        '</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # -----------------------------------------------------
    # WORLDCLOUD
    # -----------------------------------------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Worldcloud Studio</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen6.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="card-description">'
        'Una nube de palabras'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://wordcloudmio-dpzz2zwohcpixhtiqhfefz.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">'
        'Abrir aplicación ↗'
        '</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# COLUMNA 3
# =========================================================

with col3:

    # -----------------------------------------------------
    # CONSULTORIO PSICOLÓGICO
    # -----------------------------------------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Consultorio psicológico</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen7.jpg")
    st.image(image, width=190)

    st.markdown(
        '<div class="card-description">'
        'En base a una frase te diremos el mood de tu día'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://sentimentpsic-nmnxejormvmhg8vgjeajm6.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">'
        'Abrir aplicación ↗'
        '</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # -----------------------------------------------------
    # TF-IDF
    # -----------------------------------------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Demo TF-IDF</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen8.png")
    st.image(image, width=200)

    st.markdown(
        '<div class="card-description">'
        'Preguntas y lectura de documentos'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://espa-ol-espa-ol-pryjfznrx6oev7g57t7nok.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">'
        'Abrir aplicación ↗'
        '</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # -----------------------------------------------------
    # DETECCIÓN DE OBJETOS
    # -----------------------------------------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Detección de objetos en imágenes</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen9.png")
    st.image(image, width=200)

    st.markdown(
        '<div class="card-description">'
        'Detecta cualquier objeto con tu cámara'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://yolov5555-xx2ljp8ij9xinsthel5juu.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">'
        'Abrir aplicación ↗'
        '</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


    # -----------------------------------------------------
    # RECONOCIMIENTO DE IMÁGENES
    # -----------------------------------------------------

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="card-title">Reconocimiento de imágenes</div>',
        unsafe_allow_html=True
    )

    image = Image.open("imagen10.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="card-description">'
        'Toma una foto y te dirá todo'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://tm-detection-npqnkslgj6ps87sj9fvtre.streamlit.app/"

    st.markdown(
        f'<a class="boton" href="{url}" target="_blank">'
        'Abrir aplicación ↗'
        '</a>',
        unsafe_allow_html=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    Portafolio de aplicaciones · Streamlit · Python · GitHub
</div>
""", unsafe_allow_html=True)
