import streamlit as st
from PIL import Image
import base64
import io

def image_to_base64(image):
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

def app():
    image = Image.open('logo_upch.png')
    encoded_logo = image_to_base64(image)
    
    st.markdown(
        """
        <div style='text-align: center;'>
            <img src='data:image/png;base64,{}' alt='Logo UPCH' style='width: 100px;'>
        </div>
        """.format(encoded_logo),
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center;'>𝙱𝚒𝚎𝚗𝚟𝚎𝚗𝚒𝚍𝚘 𝚊 𝚕𝚊 𝚙𝚊́𝚐𝚒𝚗𝚊 𝚍𝚎 𝙸𝚗𝚒𝚌𝚒𝚘</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>Para comenzar con la configuración del ciclo, por favor dirígete a la parte izquierda superior.</h6>", unsafe_allow_html=True)

    st.header("Selecciona una sección para comenzar:")

    if st.button("Sobre Cayetano"):
        st.write(
            "Nuestros estudiantes eligen la Universidad Peruana Cayetano Heredia por muchas razones, entre las que resaltan la alta calidad académica. Además, eligen un perfil de profesores comprometidos con generar conocimiento valioso para impulsar el desarrollo, y el poder compartir con estudiantes muy determinados en sus objetivos y ansiosos por descubrir nuevas tendencias. Más allá de contar con los más altos estándares internacionales, académicos y de investigación, en Cayetano sentimos que tenemos un compromiso con la sociedad, y nos esforzamos juntos, investigadores, personal docente y estudiantes, para lograr un aporte significativo que genere bienestar en todos los campos en los que trabajamos."
        )
    if st.button("Admisión"):
        st.write(
            "Contamos con la mejor selección de alumnos, investigadores, docentes que nos han llevado a ser considerados entre las mejores universidades del Perú.\n\n"
            "Si el aprendizaje continuo, la curiosidad por descubrir, y el ser parte de una comunidad de excelencia y prestigio. Elige el proceso que corresponde con tu perfil, y postula a Cayetano. Cuenta con nuestro compromiso de formarte como un profesional de primer nivel."
        )
    if st.button("Teléfonos de Docentes"):
        st.write(
            "- Profesor Juan: +51 987 654 321\n"
            "- Profesora María: +51 987 123 456\n"
            "- Profesor Carlos: +51 987 789 012"
        )
    if st.button("Teléfonos de Ayuda"):
        st.write(
            "- Soporte Técnico General: +51 910 123 456\n"
            "- Ayuda con Plataforma Virtual: +51 910 789 012\n"
            "- Problemas de Acceso a Cuentas: +51 910 345 678\n"
            "- Asistencia para Problemas Técnicos: +51 910 901 234"
        )
    if st.button("Teléfonos de Administración"):
        st.write(
            "- Director Administrativo: +51 910 111 222\n"
            "- Coordinador de Finanzas: +51 910 333 444\n"
            "- Jefe de Recursos Humanos: +51 910 555 666\n"
            "- Asistente Administrativo: +51 910 777 888"
        )

if __name__ == "__main__":
    app()
