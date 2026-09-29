import streamlit as st
from PIL import Image
st.title("Portafolio de seguimiento - aplicaciones.")

with st.sidebar:
  st.subheader("Aplicaciones con streamlit, github, py.")
  parrafo = (
    "Aplicaciones hechan en el proceso del curso "
    "Se han aprendido nuevas e interesantes herramientas para aplicar "
    "Todo con el fin de entender mejor este tipo de tecnologías"
  )
  st.write(parrafo)

url_ia="https://github.com/Usuario-s?tab=repositories"
st.subheader("En el siguiente enlace puedes ver los repositorios a github")
st.write(f"Enlace aqui: [Enlace]({url_ia})")
col1, col2, col3 = st.columns(3)

with col1:
 
 st.subheader("Primera app de texto")
 image = Image.open('imagen1.png')
 st.image(image, width=190)
 st.write("Mi primera app en streamlit") 
 url = "https://intro-app-1-su8r5tpxlwpwnflpltft2y.streamlit.app/"
 st.write(f"Aqui el enlace: [Enlace]({url})")

 st.subheader("Reconocimiento de Objetos")
 image = Image.open('imagen2.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos como se detectan objetos en Imágenes.") 
 url = "https://miaahora-fjj6fujljb6rzv2zwvzoat.streamlit.app/"
 st.write(f"Aqui el enlace: [Enlace]({url})")

 st.subheader("Traductor")
 image = Image.open('imagen3.png')
 st.image(image, width=200)
 st.write("Podras traducir lo que dices a varios idiomas") 
 url = "https://traductor-multimodales-msvwvk3xeyowm3ofhsebtq.streamlit.app/"
 st.write(f"Aqui en enlace: [Enlace]({url})")

with col2: 
 st.subheader("Imagen a texto")
 image = Image.open('imagen4.jpg')
 st.image(image, width=200)
 st.write("Aqui veran reconocimiento de imagenes para reconocer el texto de ellas") 
 url = "https://ocr-imagen-1-hjea2xr4z9ddlpyoibf4pb.streamlit.app/"
 st.write(f"Aqui en enlace: [Enlace]({url})")

 st.subheader("Reconocimiento de caracteres")
 image = Image.open('imagen5.jpg')
 st.image(image, width=190)
 st.write("Un reconocimiento de caracteres con datos ") 
 url = "https://ocr-audio-traductor-2-suib88gv4xbfrjn33prrb8.streamlit.app/"
 st.write(f"Aqui en enlace: [Enlace]({url})")

 st.subheader("Worldcloud studio")
 image = Image.open('imagen6.jpg')
 st.image(image, width=200)
 st.write("Una nube de palabras") 
 url = "https://wordcloudmio-dpzz2zwohcpixhtiqhfefz.streamlit.app/"
 st.write(f"Aqui en enlace: [Enlace]({url})")


with col3: 
 st.subheader("Generación en Contexto")
 image = Image.open('Chat_pdf.png')
 st.image(image, width=190)
 st.write("En la siguiente veremos una aplicación que usa RAG a partir de un documento (PDF).") 
 url = "https://chatpdf-cc.streamlit.app/"
 st.write(f"RAG: [Enlace]({url})")

 st.subheader("Análisis de Imagen")
 image = Image.open('OIG4.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de análisis en Imágenes.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")
 
 st.subheader("Sistema Ciberfísico")
 image = Image.open('OIG6.jpg')
 st.image(image, width=200)
 st.write("En la siguiente enlace veremos la capacidad de interacción con el mundo físico.") 
 url = "https://vision2-gpt4o.streamlit.app/"
 st.write(f"Vision: [Enlace]({url})")


