
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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

.stApp {
    background-color: #F1F5FA;
    font-family: 'Inter', sans-serif;
}

.main .block-container {
    max-width: 1450px;
    padding: 2.5rem 2rem 3rem;
}

/* TÍTULOS PRINCIPALES */

h1 {
    color: #102A43 !important;
    font-size: clamp(28px, 3vw, 42px) !important;
    font-weight: 800 !important;
    letter-spacing: -1px;
}

h2, h3 {
    color: #102A43 !important;
}

/* BARRA LATERAL */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #102A43, #174A70);
}

section[data-testid="stSidebar"] h3 {
    color: white !important;
}

section[data-testid="stSidebar"] p {
    color: #E0EDF8 !important;
    line-height: 1.8;
}

/* ETIQUETA */

.badge {
    display: inline-block;
    background: #DCEEFF;
    color: #075A9E;
    border: 1px solid #C1E0FA;
    padding: 7px 13px;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
    margin-bottom: 15px;
}

/* LÍNEA */

.linea {
    width: 78px;
    height: 5px;
    background: linear-gradient(90deg, #1677C8, #57B5F5);
    border-radius: 10px;
    margin: 15px 0 30px;
}

/* =========================================================
   TARJETAS NATIVAS DE STREAMLIT
   ========================================================= */

/* Fondo blanco en los contenedores con borde */

div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF !important;
    border: 1px solid #D5E2EF !important;
    border-radius: 18px !important;
    box-shadow: 0 5px 18px rgba(16, 42, 67, 0.08);
    overflow: hidden;
}

/* Padding interno de cada tarjeta */

div[data-testid="stVerticalBlockBorderWrapper"] > div {
    background-color: #FFFFFF !important;
    padding: 18px 16px !important;
}

/* Los elementos internos deben ser transparentes,
   para que se vea el fondo blanco de la tarjeta */

div[data-testid="stVerticalBlockBorderWrapper"] [data-testid="stVerticalBlock"] {
    background-color: transparent !important;
}

/* TÍTULOS DE LAS TARJETAS */

.card-title {
    color: #102A43;
    font-size: 18px;
    font-weight: 800;
    text-align: center;
    line-height: 1.45;
    min-height: 52px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 12px;
    overflow-wrap: anywhere;
}

/* DESCRIPCIÓN */

.card-description {
    color: #52677B;
    font-size: 13px;
    line-height: 1.7;
    text-align: center;
    min-height: 68px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 8px 0 12px;
    overflow-wrap: anywhere;
}

/* IMÁGENES */

div[data-testid="stImage"] {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin: 8px auto 14px;
}

div[data-testid="stImage"] img {
    object-fit: contain;
    border-radius: 10px;
}

/* BOTONES NATIVOS */

div[data-testid="stLinkButton"] {
    display: flex;
    justify-content: center;
    width: 100%;
    margin: 10px 0 4px;
}

div[data-testid="stLinkButton"] a {
    background-color: #1677C8 !important;
    border: 1px solid #1677C8 !important;
    color: #FFFFFF !important;
    border-radius: 10px !important;
    font-size: 13px !important;
    font-weight: 700 !important;
    text-align: center;
    transition: background-color 0.2s ease;
}

div[data-testid="stLinkButton"] a:hover {
    background-color: #105A96 !important;
    border-color: #105A96 !important;
    color: #FFFFFF !important;
}

/* GITHUB */

.github-label {
    color: #1677C8;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.2px;
    margin-bottom: 7px;
}

.github-title {
    color: #102A43;
    font-size: 21px;
    font-weight: 800;
    margin-bottom: 8px;
}

.github-text {
    color: #52677B;
    font-size: 13px;
    line-height: 1.7;
}

.github-icon {
    background: #E8F4FF;
    color: #105A96;
    border-radius: 14px;
    padding: 12px;
    text-align: center;
    font-size: 28px;
}

/* PIE DE PÁGINA */

.footer {
    text-align: center;
    margin-top: 35px;
    padding-top: 24px;
    border-top: 1px solid #D8E4F0;
    color: #627D98;
    font-size: 12px;
}

/* MÓVILES */

@media (max-width: 768px) {
    .main .block-container {
        padding: 1.5rem 1rem 2rem;
    }

    .card-title {
        font-size: 17px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# BARRA LATERAL
# =========================================================

with st.sidebar:
    st.subheader("Aplicaciones con Streamlit, GitHub, Python.")

    st.write(
        "Aplicaciones hechas en el proceso del curso. "
        "Se han aprendido nuevas e interesantes herramientas "
        "para aplicar. Todo con el fin de entender mejor "
        "este tipo de tecnologías."
    )


# =========================================================
# ENCABEZADO
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
# REPOSITORIOS GITHUB
# =========================================================

url_ia = "https://github.com/Usuario-s?tab=repositories"

with st.container(border=True):

    github_col1, github_col2 = st.columns([5, 1])

    with github_col1:
        st.markdown(
            '<div class="github-label">CÓDIGO Y PROYECTOS</div>'
            '<div class="github-title">Repositorios en GitHub</div>'
            '<div class="github-text">'
            'En el siguiente enlace puedes ver los repositorios '
            'desarrollados durante el proceso del curso.'
            '</div>',
            unsafe_allow_html=True
        )

    with github_col2:
        st.markdown(
            '<div class="github-icon">⌘</div>',
            unsafe_allow_html=True
        )

    st.link_button(
        "Ver repositorios en GitHub ↗",
        url_ia
    )

st.write("")
st.write("")


# =========================================================
# FUNCIÓN PARA MOSTRAR APLICACIONES
# =========================================================

def mostrar_app(titulo, imagen_path, descripcion, url, ancho=200):

    # Crear un contenedor REAL con fondo blanco.
    # Todos los componentes se crean dentro de este bloque.
    with st.container(border=True):

        # Título
        st.markdown(
            f'<div class="card-title">{titulo}</div>',
            unsafe_allow_html=True
        )

        # Imagen
        try:
            imagen = Image.open(imagen_path)

            espacio_izq, centro, espacio_der = st.columns(
                [1, 4, 1]
            )

            with centro:
                st.image(
                    imagen,
                    width=ancho
                )

        except FileNotFoundError:
            st.warning(
                f"No se encontró la imagen: {imagen_path}"
            )

        # Descripción
        st.markdown(
            f'<div class="card-description">'
            f'{descripcion}'
            f'</div>',
            unsafe_allow_html=True
        )

        # Botón
        col_izq, col_boton, col_der = st.columns(
            [0.5, 4, 0.5]
        )

        with col_boton:
            st.link_button(
                "Abrir aplicación ↗",
                url,
                use_container_width=True
            )


# =========================================================
# COLUMNAS DE APLICACIONES
# =========================================================

col1, col2, col3 = st.columns(3, gap="large")


# =========================================================
# COLUMNA 1
# =========================================================

with col1:

    mostrar_app(
        "Primera app de texto",
        "imagen1.png",
        "Mi primera app en streamlit",
        "https://intro-app-1-su8r5tpxlwpwnflpltft2y.streamlit.app/",
        190
    )

    mostrar_app(
        "Reconocimiento de Objetos",
        "imagen2.jpg",
        "En la siguiente enlace veremos como se detectan objetos en Imágenes.",
        "https://miaahora-fjj6fujljb6rzv2zwvzoat.streamlit.app/",
        200
    )

    mostrar_app(
        "Traductor",
        "imagen3.png",
        "Podrás traducir lo que dices a varios idiomas",
        "https://traductor-multimodales-msvwvk3xeyowm3ofhsebtq.streamlit.app/",
        200
    )


# =========================================================
# COLUMNA 2
# =========================================================

with col2:

    mostrar_app(
        "Imagen a texto",
        "imagen4.jpg",
        "Aquí verán reconocimiento de imágenes para reconocer el texto de ellas",
        "https://ocr-imagen-1-hjea2xr4z9ddlpyoibf4pb.streamlit.app/",
        200
    )

    mostrar_app(
        "Reconocimiento de caracteres",
        "imagen5.jpg",
        "Un reconocimiento de caracteres con datos",
        "https://ocr-audio-traductor-2-suib88gv4xbfrjn33prrb8.streamlit.app/",
        190
    )

    mostrar_app(
        "Worldcloud Studio",
        "imagen6.jpg",
        "Una nube de palabras",
        "https://wordcloudmio-dpzz2zwohcpixhtiqhfefz.streamlit.app/",
        200
    )


# =========================================================
# COLUMNA 3
# =========================================================

with col3:

    mostrar_app(
        "Consultorio psicológico",
        "imagen7.jpg",
        "En base a una frase te diremos el mood de tu día",
        "https://sentimentpsic-nmnxejormvmhg8vgjeajm6.streamlit.app/",
        190
    )

    mostrar_app(
        "Demo TF-IDF",
        "imagen8.png",
        "Preguntas y lectura de documentos",
        "https://espa-ol-espa-ol-pryjfznrx6oev7g57t7nok.streamlit.app/",
        200
    )

    mostrar_app(
        "Detección de objetos en imágenes",
        "imagen9.png",
        "Detecta cualquier objeto con tu cámara",
        "https://yolov5555-xx2ljp8ij9xinsthel5juu.streamlit.app/",
        200
    )

    mostrar_app(
        "Reconocimiento de imágenes",
        "imagen10.jpg",
        "Toma una foto y te dirá todo",
        "https://tm-detection-npqnkslgj6ps87sj9fvtre.streamlit.app/",
        200
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">
    Portafolio de aplicaciones · Streamlit · Python · GitHub
</div>
""", unsafe_allow_html=True)


