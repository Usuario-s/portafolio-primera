
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
# ESTILOS VISUALES
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --navy: #102A43;
    --blue: #1677C8;
    --blue-dark: #105A96;
    --background: #F2F6FB;
    --border: #D8E4F0;
    --text: #334E68;
    --muted: #627D98;
}

.stApp {
    background-color: var(--background);
    font-family: 'Inter', sans-serif;
}

.main .block-container {
    max-width: 1450px;
    padding: 2.5rem 2rem 3rem;
}

/* TÍTULOS */

h1 {
    color: var(--navy) !important;
    font-size: clamp(28px, 3vw, 42px) !important;
    font-weight: 800 !important;
    letter-spacing: -1px;
    line-height: 1.2 !important;
}

h2, h3 {
    color: var(--navy) !important;
}

p {
    color: var(--text);
}

/* BARRA LATERAL */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #102A43 0%, #174A70 100%);
    border-right: 1px solid #234F70;
}

section[data-testid="stSidebar"] > div {
    padding-top: 2rem;
}

section[data-testid="stSidebar"] h3 {
    color: #FFFFFF !important;
    font-size: 20px !important;
    font-weight: 800 !important;
    line-height: 1.5;
}

section[data-testid="stSidebar"] p {
    color: #E0EDF8 !important;
    font-size: 14px;
    line-height: 1.85;
}

/* ETIQUETA SUPERIOR */

.badge {
    display: inline-block;
    background: #DCEEFF;
    color: #075A9E;
    padding: 7px 13px;
    border: 1px solid #C1E0FA;
    border-radius: 30px;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.1px;
    margin-bottom: 15px;
}

/* LÍNEA DECORATIVA */

.linea {
    width: 78px;
    height: 5px;
    background: linear-gradient(90deg, #1677C8, #57B5F5);
    border-radius: 10px;
    margin: 15px 0 30px;
}

/* TARJETAS */

.card {
    background: #FFFFFF;
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 24px 18px 22px;
    margin-bottom: 24px;
    min-height: 355px;
    box-shadow: 0 5px 18px rgba(16, 42, 67, 0.055);
    transition: transform 0.25s ease,
                box-shadow 0.25s ease,
                border-color 0.25s ease;
}

.card:hover {
    transform: translateY(-4px);
    border-color: #8CC9F3;
    box-shadow: 0 12px 28px rgba(16, 42, 67, 0.12);
}

/* CONTENIDO DE LAS TARJETAS */

.card-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    width: 100%;
}

/* TÍTULOS DE APLICACIONES */

.card-title {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: var(--navy);
    font-size: 18px;
    font-weight: 800;
    line-height: 1.4;
    min-height: 50px;
    margin: 0 0 15px;
    width: 100%;
}

/* DESCRIPCIONES */

.card-description {
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: #52677B;
    font-size: 13px;
    line-height: 1.7;
    min-height: 65px;
    width: 100%;
    margin: 0 0 14px;
}

/* IMÁGENES */

div[data-testid="stImage"] {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin: 0 auto 15px;
}

div[data-testid="stImage"] img {
    object-fit: contain;
    border-radius: 10px;
}

/* BOTONES */

.boton {
    display: inline-flex;
    justify-content: center;
    align-items: center;
    gap: 7px;
    background: var(--blue);
    color: #FFFFFF !important;
    border: 1px solid var(--blue);
    padding: 11px 16px;
    border-radius: 10px;
    text-decoration: none !important;
    font-size: 13px;
    font-weight: 700;
    text-align: center;
    transition: background 0.2s ease,
                transform 0.2s ease,
                box-shadow 0.2s ease;
}

.boton:hover {
    background: var(--blue-dark);
    border-color: var(--blue-dark);
    color: #FFFFFF !important;
    transform: translateY(-2px);
    box-shadow: 0 5px 14px rgba(22, 119, 200, 0.23);
}

.boton-container {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin-top: 4px;
}

/* SECCIÓN GITHUB */

.github-box {
    background: #FFFFFF;
    border: 1px solid #D4E3F0;
    border-left: 5px solid #1677C8;
    border-radius: 16px;
    padding: 23px 25px;
    margin: 10px 0 15px;
    box-shadow: 0 5px 18px rgba(16, 42, 67, 0.06);
}

.github-content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
}

.github-left {
    flex: 1;
    min-width: 220px;
}

.github-label {
    color: #1677C8;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.2px;
    text-transform: uppercase;
    margin-bottom: 7px;
}

.github-title {
    color: #102A43;
    font-size: 21px;
    font-weight: 800;
    line-height: 1.4;
    margin-bottom: 6px;
}

.github-text {
    color: #52677B;
    font-size: 13px;
    line-height: 1.7;
}

.github-icon {
    display: flex;
    align-items: center;
    justify-content: center;
    min-width: 62px;
    height: 62px;
    padding: 12px;
    border-radius: 15px;
    background: #E8F4FF;
    color: #105A96;
    font-size: 29px;
}

/* FOOTER */

.footer {
    text-align: center;
    margin-top: 35px;
    padding-top: 24px;
    border-top: 1px solid #D8E4F0;
    color: #627D98;
    font-size: 12px;
    letter-spacing: 0.2px;
}

/* COLUMNAS */

div[data-testid="stHorizontalBlock"] {
    align-items: stretch;
}

/* RESPONSIVE */

@media (max-width: 768px) {
    .main .block-container {
        padding: 1.5rem 1rem 2rem;
    }

    .card {
        padding: 20px 14px;
        min-height: auto;
    }

    .card-title {
        font-size: 17px;
    }

    .github-box {
        padding: 19px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# BARRA LATERAL
# =========================================================

with st.sidebar:
    st.subheader("Aplicaciones con Streamlit, GitHub y Python.")

    parrafo = (
        "Aplicaciones hechas en el proceso del curso. "
        "Se han aprendido nuevas e interesantes herramientas "
        "para aplicar. Todo con el fin de entender mejor "
        "este tipo de tecnologías."
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
# REPOSITORIOS GITHUB
# =========================================================

url_ia = "https://github.com/Usuario-s?tab=repositories"

st.markdown(f"""
<div class="github-box">
    <div class="github-content">
        <div class="github-left">
            <div class="github-label">CÓDIGO Y PROYECTOS</div>
            <div class="github-title">Repositorios en GitHub</div>
            <div class="github-text">
                En el siguiente enlace puedes ver los repositorios
                desarrollados durante el proceso del curso.
            </div>
        </div>
        <div class="github-icon">⌘</div>
    </div>
</div>

<div class="boton-container">
    <a class="boton"
       href="{url_ia}"
       target="_blank"
       rel="noopener noreferrer">
       Ver repositorios en GitHub ↗
    </a>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")


# =========================================================
# FUNCIÓN PARA CREAR TARJETAS
# =========================================================

def mostrar_app(titulo, imagen_path, descripcion, url, ancho=200):

    st.markdown(
        '<div class="card"><div class="card-content">',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="card-title">{titulo}</div>',
        unsafe_allow_html=True
    )

    try:
        imagen = Image.open(imagen_path)
        st.image(imagen, width=ancho)

    except FileNotFoundError:
        st.warning(f"No se encontró la imagen: {imagen_path}")

    st.markdown(
        f'<div class="card-description">{descripcion}</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="boton-container">
            <a class="boton"
               href="{url}"
               target="_blank"
               rel="noopener noreferrer">
               Abrir aplicación ↗
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('</div></div>', unsafe_allow_html=True)


# =========================================================
# DISTRIBUCIÓN DE APLICACIONES
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
        "En el siguiente enlace veremos como se detectan objetos en Imágenes.",
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

