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
 st.subheader("Consultorio psicologico")
 image = Image.open('imagen7.jpg')
 st.image(image, width=190)
 st.write("En base a una frase te diremos el mood de tu día") 
 url = "https://sentimentpsic-nmnxejormvmhg8vgjeajm6.streamlit.app/"
 st.write(f"Aqui en enlace: [Enlace]({url})")

 st.subheader("Demo TF-IDF")
 image = Image.open('imagen8.png')
 st.image(image, width=200)
 st.write("Preguntas y lectura de documentos") 
 url = "https://espa-ol-espa-ol-pryjfznrx6oev7g57t7nok.streamlit.app/"
 st.write(f"Aqui en enlace: [Enlace]({url})")
 
 st.subheader("Detección de objetos en imagenes")
 image = Image.open('imagen9.png')
 st.image(image, width=200)
 st.write("Detecta cualquier objeto con tu camara") 
 url = "https://yolov5555-xx2ljp8ij9xinsthel5juu.streamlit.app/"
 st.write(f"Aqui en enlace: [Enlace]({url})")


