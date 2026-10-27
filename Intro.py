
import streamlit as st
import base64
import mimetypes
import html
from pathlib import Path

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
.stApp {
    background:
        radial-gradient(ellipse at 8% 8%, rgba(123,177,231,.22), transparent 35%),
        radial-gradient(ellipse at 92% 22%, rgba(174,202,239,.30), transparent 32%),
        radial-gradient(ellipse at 50% 95%, rgba(120,164,218,.18), transparent 40%),
        linear-gradient(135deg, #eef4fb, #e5edf8 45%, #f3f6fc);
    background-attachment: fixed;
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: transparent;
}

[data-testid="stHeader"] {
    background: rgba(238,244,251,.65);
}

[data-testid="stSidebar"] {
    background: linear-gradient(160deg, #102b4e, #173b65 55%, #24527e);
}

[data-testid="stSidebar"] * {
    color: #f4f8ff;
}

.stMainBlockContainer {
    position: relative;
    z-index: 1;
}

/* ENCABEZADO */

.portfolio-header {
    padding: 35px 30px;
    margin: 8px 0 28px;
    border-radius: 24px;
    background:
        radial-gradient(circle at 90% 10%, rgba(106,165,226,.25), transparent 35%),
        linear-gradient(125deg, rgba(255,255,255,.97), rgba(234,242,253,.94));
    border: 1px solid rgba(255,255,255,.85);
    box-shadow: 0 12px 35px rgba(36,67,108,.09);
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
    line-height: 1.2;
    margin: 0 0 12px;
}

.main-subtitle {
    color: #61758d;
    font-size: 16px;
    line-height: 1.7;
    margin: 0;
}

/* SECCIONES */

.section-title {
    color: #193a5d;
    font-size: 25px;
    font-weight: 800;
    margin: 26px 0 8px;
}

.section-subtitle {
    color: #647991;
    font-size: 14px;
    margin: 0 0 24px;
}

/* TARJETAS ORIGINALES */

.app-card {
    box-sizing: border-box;
    width: 100%;
    min-height: 390px;
    padding: 23px 18px 20px;
    margin-bottom: 24px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    background: #ffffff;
    border: 1px solid #d5e3f2;
    border-radius: 20px;
    box-shadow: 0 8px 22px rgba(32,66,108,.08);
    transition: transform .25s ease, box-shadow .25s ease;
}

.app-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 16px 32px rgba(32,66,108,.14);
}

.app-card-title {
    width: 100%;
    min-height: 54px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #193b60;
    font-size: 18px;
    font-weight: 800;
    line-height: 1.4;
    margin-bottom: 13px;
}

.app-card-image {
    width: 100%;
    height: 155px;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    margin-bottom: 16px;
}

.app-card-image img {
    display: block;
    max-width: 100%;
    max-height: 150px;
    height: auto;
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
    overflow-wrap: anywhere;
    padding: 8px;
    box-sizing: border-box;
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
}

.app-button {
    box-sizing: border-box;
    display: block;
    width: 100%;
    max-width: 240px;
    margin: 0 auto;
    padding: 12px 16px;
    color: #ffffff !important;
    background: linear-gradient(135deg, #245d96, #397fc0);
    border-radius: 11px;
    font-size: 14px;
    font-weight: 700;
    text-align: center;
    text-decoration: none !important;
    box-shadow: 0 4px 10px rgba(37,94,151,.17);
    transition: all .2s ease;
}

.app-button:hover {
    background: linear-gradient(135deg, #174574, #286aa9);
    box-shadow: 0 7px 16px rgba(37,94,151,.24);
}

/* =========================================================
   SEGUNDA PARTE: CHAT PDF HASTA VOICE
   TARJETAS NEGRAS Y LETRAS BLANCAS
   ========================================================= */

.app-card.app-card-second {
    background: linear-gradient(145deg, #101010, #1b1b1b);
    border: 1px solid #383838;
    box-shadow: 0 10px 26px rgba(0,0,0,.22);
}

.app-card.app-card-second:hover {
    background: linear-gradient(145deg, #181818, #242424);
    border-color: #555555;
    box-shadow: 0 16px 34px rgba(0,0,0,.32);
}

.app-card.app-card-second .app-card-title {
    color: #ffffff;
}

.app-card.app-card-second .app-card-description {
    color: #dedede;
}

.app-card.app-card-second .image-missing {
    background: #292929;
    color: #eeeeee;
    border: 1px solid #414141;
}

/* BOTONES ROJOS DE LA SEGUNDA PARTE */

.app-card.app-card-second .app-button {
    color: #ffffff !important;
    background: linear-gradient(135deg, #b5121b, #ed2939);
    box-shadow: 0 4px 12px rgba(237,41,57,.22);
}

.app-card.app-card-second .app-button:hover {
    background: linear-gradient(135deg, #8f0d15, #c91828);
    box-shadow: 0 7px 18px rgba(237,41,57,.35);
}

/* GITHUB */

.github-card {
    box-sizing: border-box;
    width: 100%;
    padding: 25px 28px;
    margin: 12px 0 30px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 22px;
    background: linear-gradient(120deg, #fff, #edf4fc);
    border: 1px solid #d4e2f2;
    border-radius: 19px;
    box-shadow: 0 8px 22px rgba(32,66,108,.07);
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
    display: inline-block;
    padding: 13px 20px;
    color: #fff !important;
    background: linear-gradient(135deg, #183858, #2d5d88);
    border-radius: 11px;
    text-decoration: none !important;
    font-size: 14px;
    font-weight: 700;
    text-align: center;
}

.github-button:hover {
    background: #102b47;
}

/* PIE */

.footer {
    margin-top: 30px;
    padding: 22px 10px 12px;
    border-top: 1px solid rgba(114,143,176,.25);
    color: #6d8096;
    font-size: 13px;
    text-align: center;
    line-height: 1.8;
}

@media (max-width: 700px) {
    .portfolio-header {
        padding: 25px 20px;
    }

    .github-card {
        padding: 22px;
    }

    .github-button {
        width: 100%;
        box-sizing: border-box;
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

    st.write(
        "Aplicaciones con Streamlit, GitHub y Python."
    )

    st.write(
        "Aplicaciones hechas durante el curso. "
        "Se han aprendido nuevas e interesantes herramientas "
        "para aplicar y comprender mejor estas tecnologías."
    )

    st.markdown("---")
    st.markdown("### 📚 Contenido")

    st.markdown("""
    - Aplicaciones desarrolladas
    - Reconocimiento de objetos
    - Texto y traducción
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
    <div class="main-title">Portafolio de seguimiento - Aplicaciones</div>
    <p class="main-subtitle">
        Un recorrido por los proyectos desarrollados con Python,
        Streamlit y diferentes herramientas de inteligencia artificial.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# GITHUB
# =========================================================

url_github = "https://github.com/Usuario-s?tab=repositories"

st.markdown("""
<div class="github-card">
    <div class="github-info">
        <div class="github-title">🚀 Explora mis proyectos en GitHub</div>
        <div class="github-description">
            Consulta los repositorios y conoce más sobre el código
            detrás de las aplicaciones de este portafolio.
        </div>
    </div>
    <a class="github-button"
       href="https://github.com/Usuario-s?tab=repositories"
       target="_blank" rel="noopener noreferrer">
       Ver repositorios ↗
    </a>
</div>
""", unsafe_allow_html=True)

# =========================================================
# FUNCIÓN PARA MOSTRAR LAS TARJETAS
# =========================================================

def mostrar_app(
    titulo,
    imagen_path,
    descripcion,
    url,
    ancho=200,
    segunda_parte=False
):
    titulo_html = html.escape(titulo)
    descripcion_html = html.escape(descripcion)
    url_html = html.escape(url, quote=True)

    ruta = Path(imagen_path)

    if ruta.is_file():
        with ruta.open("rb") as archivo:
            datos = base64.b64encode(
                archivo.read()
            ).decode("ascii")

        mime = (
            mimetypes.guess_type(str(ruta))[0]
            or "image/png"
        )

        imagen_html = (
            f'<img src="data:{mime};base64,{datos}" '
            f'alt="{titulo_html}" '
            f'style="width:{ancho}px;max-width:100%;">'
        )
    else:
        imagen_html = (
            '<div class="image-missing">'
            'Imagen no encontrada: '
            + html.escape(imagen_path)
            + '</div>'
        )

    # Aplicar diseño especial únicamente a la segunda parte
    clase_tarjeta = (
        "app-card app-card-second"
        if segunda_parte
        else "app-card"
    )

    tarjeta_html = f"""
    <div class="{clase_tarjeta}">
        <div class="app-card-title">{titulo_html}</div>
        <div class="app-card-image">{imagen_html}</div>
        <div class="app-card-description">{descripcion_html}</div>
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

    st.markdown(
        tarjeta_html,
        unsafe_allow_html=True
    )

# =========================================================
# LISTA DE APLICACIONES (19 EN TOTAL)
# =========================================================

st.markdown("""
<div class="section-title">Mis aplicaciones</div>
<div class="section-subtitle">
    Selecciona un proyecto para abrirlo y explorar su funcionamiento.
</div>
""", unsafe_allow_html=True)

apps = [
    # -----------------------------------------------------
    # APLICACIONES ORIGINALES (1-10)
    # -----------------------------------------------------
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
        "descripcion": "En base a una frase te diremos el mood de tu día.",
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
    },

    # -----------------------------------------------------
    # SEGUNDA PARTE (11-19)
    # Tarjetas negras, letras blancas y botones rojos
    # -----------------------------------------------------
    {
        "titulo": "Chat PDF",
        "imagen": "im1.jpg",
        "descripcion": "Chatea con la IA",
        "url": "https://chatea-pdf-k4mke22znp5eapzqklyzar.streamlit.app/",
        "ancho": 200
    },
    {
        "titulo": "Inter- de imagenes con IA",
        "imagen": "im2.jpg",
        "descripcion": "Interpretacion de imagenes con IA",
        "url": "https://inter-de-imagenes-con-ia-vtvwyqnb2dwnzfz3vnougm.streamlit.app/",
        "ancho": 200
    },
    {
        "titulo": "Tablero Inteligente",
        "imagen": "im3.jpg",
        "descripcion": "Tablero comun",
        "url": "https://port2-drawrecog-enzmsvgmq7x3ccy9uba2ha.streamlit.app/",
        "ancho": 200
    },
    {
        "titulo": "Numeros",
        "imagen": "im4.jpg",
        "descripcion": "Escribe los numeros que quieras",
        "url": "https://port2---reconocimiento-numeros-8q2tduyvojm24mjcapzbbs.streamlit.app/",
        "ancho": 200
    },
    {
        "titulo": "Tablero personal",
        "imagen": "im5.jpg",
        "descripcion": "Todo a tu creatividad",
        "url": "https://port2-maybe-app-mine-q4gprc6a5iapp3yanjvtykq.streamlit.app/",
        "ancho": 200
    },
    {
        "titulo": "Tablero inteligente ultra hd",
        "imagen": "im6.jpg",
        "descripcion": "Tablero aun mas inteligente",
        "url": "https://port2-hist-4th-app-vcqepbfrojh4edityvjgvw.streamlit.app/",
        "ancho": 200
    },
    {
        "titulo": "Sensor reader",
        "imagen": "im7.jpg",
        "descripcion": "sensor mqtt reader de textos",
        "url": "https://recepmqtt-portf2-mio-6vecwa2gr8x3gdjkzubaem.streamlit.app/undefined",
        "ancho": 200
    },
    {
        "titulo": "space control mqtt",
        "imagen": "im8.jpg",
        "descripcion": "app de control mqtt",
        "url": "https://sendcmqtt-portf2-mcgst6sqf9czkuft5yy83n.streamlit.app/",
        "ancho": 200
    },
    {
        "titulo": "voice",
        "imagen": "im9.jpg",
        "descripcion": "Sistema de reconocimiento vocal",
        "url": "https://ctrlvoice-portf2-han5hijiban4ibn8jcwfan.streamlit.app/",
        "ancho": 200
    }
]

# =========================================================
# DISTRIBUCIÓN AUTOMÁTICA EN TRES COLUMNAS
# =========================================================

for inicio in range(0, len(apps), 3):
    columnas = st.columns(3, gap="large")

    for desplazamiento, columna in enumerate(columnas):
        posicion = inicio + desplazamiento

        if posicion < len(apps):
            app = apps[posicion]

            with columna:
                mostrar_app(
                    titulo=app["titulo"],
                    imagen_path=app["imagen"],
                    descripcion=app["descripcion"],
                    url=app["url"],
                    ancho=app["ancho"],
                    segunda_parte=posicion >= 10
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

