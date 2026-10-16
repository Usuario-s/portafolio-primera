
import streamlit as st
import base64
import mimetypes
import html

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

    /* ==========================================
       FONDO GENERAL: DEGRADADO + TEXTURA
       ========================================== */

    .stApp {
        background:
            radial-gradient(
                ellipse at 8% 8%,
                rgba(123, 177, 231, 0.22) 0%,
                transparent 35%
            ),
            radial-gradient(
                ellipse at 92% 22%,
                rgba(174, 202, 239, 0.30) 0%,
                transparent 32%
            ),
            radial-gradient(
                ellipse at 50% 95%,
                rgba(120, 164, 218, 0.18) 0%,
                transparent 40%
            ),
            linear-gradient(
                135deg,
                #eef4fb 0%,
                #e5edf8 45%,
                #f3f6fc 100%
            );
        background-attachment: fixed;
    }

    /* Textura decorativa con puntos muy sutiles */
    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        pointer-events: none;
        z-index: 0;
        opacity: 0.24;
        background-image: radial-gradient(
            rgba(68, 102, 148, 0.24) 0.65px,
            transparent 0.65px
        );
        background-size: 9px 9px;
        mask-image: linear-gradient(
            to bottom,
            rgba(0, 0, 0, 0.55),
            transparent 90%
        );
    }

    /* Mantener el contenido por encima de la textura */
    .stMainBlockContainer {
        position: relative;
        z-index: 1;
    }

    /* Fondo del área principal */
    [data-testid="stAppViewContainer"] {
        background: transparent;
    }

    [data-testid="stHeader"] {
        background: rgba(238, 244, 251, 0.65);
    }

    /* ==========================================
       BARRA LATERAL
       ========================================== */

    [data-testid="stSidebar"] {
        background: linear-gradient(
            160deg,
            #102b4e 0%,
            #173b65 55%,
            #24527e 100%
        );
        border-right: 1px solid rgba(255, 255, 255, 0.12);
    }

    [data-testid="stSidebar"] * {
        color: #f4f8ff;
    }

    [data-testid="stSidebar"] p {
        line-height: 1.7;
    }

    /* ==========================================
       ENCABEZADO DEL PORTAFOLIO
       ========================================== */

    .portfolio-header {
        padding: 35px 30px;
        margin: 8px 0 28px 0;
        border-radius: 24px;
        background:
            radial-gradient(
                circle at 90% 10%,
                rgba(106, 165, 226, 0.25),
                transparent 35%
            ),
            linear-gradient(
                125deg,
                rgba(255, 255, 255, 0.94),
                rgba(234, 242, 253, 0.91)
            );
        border: 1px solid rgba(255, 255, 255, 0.85);
        box-shadow: 0 12px 35px rgba(36, 67, 108, 0.09);
        position: relative;
        overflow: hidden;
    }

    .portfolio-header::after {
        content: "";
        position: absolute;
        width: 180px;
        height: 180px;
        right: -60px;
        bottom: -105px;
        border-radius: 50%;
        border: 25px solid rgba(77, 132, 194, 0.09);
    }

    .eyebrow {
        color: #3972ad;
        font-size: 12px;
        font-weight: 800;
        letter-spacing: 3px;
        margin-bottom: 12px;
    }

    .main-title {
        color: #163354;
        font-size: clamp(28px, 4vw, 43px);
        font-weight: 800;
        line-height: 1.15;
        margin: 0 0 12px 0;
    }

    .main-subtitle {
        color: #61758d;
        font-size: 16px;
        line-height: 1.7;
        margin: 0;
        max-width: 720px;
    }

    /* ==========================================
       TÍTULOS DE SECCIÓN
       ========================================== */

    .section-title {
        color: #193a5d;
        font-size: 25px;
        font-weight: 800;
        margin: 26px 0 8px 0;
    }

    .section-subtitle {
        color: #647991;
        font-size: 14px;
        margin: 0 0 24px 0;
    }

    /* ==========================================
       TARJETAS DE APLICACIONES
       ========================================== */

    .app-card {
        box-sizing: border-box;
        width: 100%;
        min-height: 390px;
        height: 100%;
        padding: 23px 18px 20px;
        margin-bottom: 24px;

        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;

        background: rgba(255, 255, 255, 0.96);
        border: 1px solid rgba(207, 222, 240, 0.95);
        border-radius: 20px;

        box-shadow:
            0 8px 22px rgba(32, 66, 108, 0.07),
            0 2px 5px rgba(32, 66, 108, 0.03);

        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease,
            border-color 0.25s ease;
    }

    .app-card:hover {
        transform: translateY(-5px);
        border-color: #a8c8ed;
        box-shadow: 0 16px 32px rgba(32, 66, 108, 0.13);
    }

    .app-card-title {
        width: 100%;
        min-height: 54px;
        display: flex;
        justify-content: center;
        align-items: center;

        color: #193b60;
        font-size: 18px;
        font-weight: 800;
        line-height: 1.4;

        margin-bottom: 13px;
    }

    .app-card-image {
        width: 100%;
        height: 155px;
        flex-shrink: 0;

        display: flex;
        justify-content: center;
        align-items: center;

        margin: 0 auto 16px;
        overflow: hidden;
        border-radius: 12px;
    }

    .app-card-image img {
        display: block;
        max-width: 100%;
        max-height: 150px;
        object-fit: contain;
        border-radius: 10px;
    }

    .image-missing {
        width: 100%;
        height: 140px;
        display: flex;
        align-items: center;
        justify-content: center;

        background: #edf3fa;
        color: #71859b;
        border-radius: 12px;
        font-size: 13px;
    }

    .app-card-description {
        width: 100%;
        min-height: 62px;

        color: #65778c;
        font-size: 14px;
        line-height: 1.65;

        margin-bottom: 20px;
    }

    .app-card-action {
        width: 100%;
        margin-top: auto;

        display: flex;
        justify-content: center;
    }

    .app-button {
        box-sizing: border-box;
        display: inline-block;
        width: 100%;
        max-width: 240px;
        padding: 12px 16px;

        color: #ffffff !important;
        background: linear-gradient(135deg, #245d96, #397fc0);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 11px;

        font-size: 14px;
        font-weight: 700;
        text-align: center;
        text-decoration: none !important;

        box-shadow: 0 4px 10px rgba(37, 94, 151, 0.17);
        transition: all 0.2s ease;
    }

    .app-button:hover {
        background: linear-gradient(135deg, #174574, #286aa9);
        box-shadow: 0 7px 16px rgba(37, 94, 151, 0.24);
        transform: translateY(-2px);
    }

    /* ==========================================
       TARJETA DE GITHUB
       ========================================== */

    .github-card {
        box-sizing: border-box;
        width: 100%;
        padding: 25px 28px;
        margin: 12px 0 30px 0;

        display: flex;
        align-items: center;
        justify-content: space-between;
        flex-wrap: wrap;
        gap: 22px;

        background:
            radial-gradient(
                circle at 95% 5%,
                rgba(98, 155, 216, 0.17),
                transparent 35%
            ),
            rgba(255, 255, 255, 0.96);

        border: 1px solid #d4e2f2;
        border-radius: 19px;
        box-shadow: 0 8px 22px rgba(32, 66, 108, 0.07);
    }

    .github-info {
        flex: 1;
        min-width: 220px;
    }

    .github-title {
        color: #193b60;
        font-size: 20px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    .github-description {
        color: #65778c;
        font-size: 14px;
        line-height: 1.65;
    }

    .github-button {
        box-sizing: border-box;
        display: inline-block;
        padding: 13px 20px;

        color: #ffffff !important;
        background: linear-gradient(135deg, #183858, #2d5d88);
        border-radius: 11px;

        text-decoration: none !important;
        font-size: 14px;
        font-weight: 700;
        text-align: center;

        box-shadow: 0 5px 13px rgba(24, 56, 88, 0.17);
        transition: all 0.2s ease;
    }

    .github-button:hover {
        background: linear-gradient(135deg, #102b47, #204b75);
        transform: translateY(-2px);
    }

    /* ==========================================
       PIE DE PÁGINA
       ========================================== */

    .footer {
        margin-top: 30px;
        padding: 22px 10px 12px;
        border-top: 1px solid rgba(114, 143, 176, 0.25);

        color: #6d8096;
        font-size: 13px;
        text-align: center;
        line-height: 1.8;
    }

    /* ==========================================
       AJUSTES PARA PANTALLAS PEQUEÑAS
       ========================================== */

    @media (max-width: 700px) {
        .portfolio-header {
            padding: 25px 20px;
        }

        .github-card {
            padding: 22px;
        }

        .github-button {
            width: 100%;
        }

        .app-card {
            min-height: 370px;
        }
    }

</style>
""", unsafe_allow_html=True)

# =========================================================
# BARRA LATERAL
# =========================================================

with st.sidebar:
    st.markdown("## 💻 Mi portafolio")

    st.markdown("""
    Aplicaciones desarrolladas con **Streamlit, GitHub y Python**.

    Durante el curso se han explorado nuevas herramientas
    y tecnologías para comprender mejor el desarrollo de
    aplicaciones interactivas.
    """)

    st.markdown("---")

    st.markdown("### 📚 Contenido")
    st.markdown("""
    - Aplicaciones desarrolladas
    - Proyectos de reconocimiento
    - Herramientas de texto y traducción
    - Inteligencia artificial
    """)

    st.markdown("---")

    st.caption("Portafolio académico · 2026")

# =========================================================
# ENCABEZADO
# =========================================================

st.markdown("""
<div class="portfolio-header">
    <div class="eyebrow">PORTAFOLIO ACADÉMICO</div>
    <div class="main-title">
        Portafolio de seguimiento - Aplicaciones
    </div>
    <p class="main-subtitle">
        Un recorrido por los proyectos desarrollados con Python,
        Streamlit y diferentes herramientas de inteligencia artificial.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# SECCIÓN DE GITHUB
# =========================================================

url_github = "https://github.com/Usuario-s?tab=repositories"

st.markdown(f"""
<div class="github-card">
    <div class="github-info">
        <div class="github-title">🚀 Explora mis proyectos en GitHub</div>
        <div class="github-description">
            Consulta los repositorios y conoce más sobre el código
            detrás de las aplicaciones de este portafolio.
        </div>
    </div>
    <a class="github-button"
       href="{url_github}"
       target="_blank"
       rel="noopener noreferrer">
       Ver repositorios ↗
    </a>
</div>
""", unsafe_allow_html=True)

# =========================================================
# FUNCIÓN PARA MOSTRAR CADA APLICACIÓN
# =========================================================

def mostrar_app(titulo, imagen_path, descripcion, url, ancho=200):
    """
    Cada tarjeta se genera dentro de un único bloque HTML.
    Así, la imagen, el texto y el enlace quedan dentro
    de la misma tarjeta blanca.
    """

    titulo_html = html.escape(titulo)
    descripcion_html = html.escape(descripcion)
    url_html = html.escape(url, quote=True)

    try:
        with open(imagen_path, "rb") as archivo:
            imagen_bytes = archivo.read()

        imagen_base64 = base64.b64encode(imagen_bytes).decode("utf-8")
        mime_type = mimetypes.guess_type(imagen_path)[0] or "image/png"

        imagen_html = f"""
            <img
                src="data:{mime_type};base64,{imagen_base64}"
                alt="{titulo_html}"
                style="width:{ancho}px; max-width:100%;"
            >
        """

    except FileNotFoundError:
        imagen_html = """
            <div class="image-missing">
                Imagen no encontrada
            </div>
        """

    tarjeta_html = f"""
    <div class="app-card">

        <div class="app-card-title">
            {titulo_html}
        </div>

        <div class="app-card-image">
            {imagen_html}
        </div>

        <div class="app-card-description">
            {descripcion_html}
        </div>

        <div class="app-card-action">
            <a class="app-button"
               href="{url_html}"
               target="_blank"
               rel="noopener noreferrer">
               Abrir aplicación ↗
            </a>
        </div>

    </div>
    """

    st.markdown(tarjeta_html, unsafe_allow_html=True)

# =========================================================
# TÍTULO DE LAS APLICACIONES
# =========================================================

st.markdown("""
<div class="section-title">Mis aplicaciones</div>
<div class="section-subtitle">
    Selecciona un proyecto para abrirlo y explorar su funcionamiento.
</div>
""", unsafe_allow_html=True)

# =========================================================
# LISTA DE APLICACIONES
# =========================================================

apps = [
    {
        "titulo": "Primera app de texto",
        "imagen": "imagen1.png",
        "descripcion": "Mi primera app en Streamlit.",
        "url": "https://intro-app-1-su8r5tpxlwpwnflpltft2y.streamlit.app/",
        "ancho": 190
    },
    {
        "titulo": "Reconocimiento de Objetos",
        "imagen": "imagen2.jpg",
        "descripcion": "En el siguiente enlace veremos cómo se detectan objetos en imágenes.",
        "url": "https://miaahora-fjj6fujljb6rzv2zwvzoat.streamlit.app/",
        "ancho": 200
    },
    {
        "titulo": "Traductor",
        "imagen": "imagen3.png",
        "descripcion": "Podrás traducir lo que dices a varios idiomas.",
        "url": "https://traductor-multimodales-msvwvk3xeyowm3ofhsebtq.streamlit.app/",
        "ancho": 200
    },
    {
        "titulo": "Imagen a texto",
        "imagen": "imagen4.jpg",
        "descripcion": "Reconocimiento de imágenes para extraer el texto que contienen.",
        "url": "https://ocr-imagen-1-hjea2xr4z9ddlpyoibf4pb.streamlit.app/",
        "ancho": 200
    },
    {
        "titulo": "Reconocimiento de caracteres",
        "imagen": "imagen5.jpg",
        "descripcion": "Un reconocimiento de caracteres con datos.",
        "url": "https://ocr-audio-traductor-2-suib88gv4xbfrjn33prrb8.streamlit.app/",
        "ancho": 190
    },
    {
        "titulo": "Worldcloud Studio",
        "imagen": "imagen6.jpg",
        "descripcion": "Una nube de palabras.",
        "url": "https://wordcloudmio-dpzz2zwohcpixhtiqhfefz.streamlit.app/",
        "ancho": 200
    },
    {
        "titulo": "Consultorio psicológico",
        "imagen": "imagen7.jpg",
        "descripcion": "En base a una frase, te diremos el mood de tu día.",
        "url": "https://sentimentpsic-nmnxejormvmhg8vgjeajm6.streamlit.app/",
        "ancho": 190
    },
    {
        "titulo": "Demo TF-IDF",
        "imagen": "imagen8.png",
        "descripcion": "Preguntas y lectura de documentos.",
        "url": "https://espa-ol-espa-ol-pryjfznrx6oev7g57t7nok.streamlit.app/",
        "ancho": 200
    },
    {
        "titulo": "Detección de objetos en imágenes",
        "imagen": "imagen9.png",
        "descripcion": "Detecta cualquier objeto con tu cámara.",
        "url": "https://yolov5555-xx2ljp8ij9xinsthel5juu.streamlit.app/",
        "ancho": 200
    },
    {
        "titulo": "Reconocimiento de imágenes",
        "imagen": "imagen10.jpg",
        "descripcion": "Toma una foto y te dirá todo.",
        "url": "https://tm-detection-npqnkslgj6ps87sj9fvtre.streamlit.app/",
        "ancho": 200
    }
]

# =========================================================
# DISTRIBUCIÓN EN TRES COLUMNAS
# =========================================================

for inicio in range(0, len(apps), 3):
    columnas = st.columns(3, gap="large")

    for indice, columna in enumerate(columnas):
        posicion = inicio + indice

        if posicion < len(apps):
            app = apps[posicion]

            with columna:
                mostrar_app(
                    titulo=app["titulo"],
                    imagen_path=app["imagen"],
                    descripcion=app["descripcion"],
                    url=app["url"],
                    ancho=app["ancho"]
                )

# =========================================================
# PIE DE PÁGINA
# =========================================================

st.markdown("""
<div class="footer">
    <strong>Portafolio de seguimiento</strong><br>
    Desarrollado con Python y Streamlit<br>
    Explorando nuevas herramientas, una aplicación a la vez.
</div>
""", unsafe_allow_html=True)



