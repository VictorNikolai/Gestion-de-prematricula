import streamlit as st
from PIL import Image

def login(encoded_logo, User, Password):
    st.markdown(f"""
        <style>
        .header-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 2rem;
        }}
        .header-container img {{
            max-height: 100px;
            margin-right: 20px;
        }}
        .header-container h1 {{
            font-size: 2.5rem;
            margin: 0;
        }}
        .login-form {{
            max-width: 400px;
            background-color: #333333;
            padding: 20px;
            border-radius: 10px;
            margin-top: 50px;
        }}
        .login-form input[type="text"], 
        .login-form input[type="password"] {{
            background-color: #444444;
            color: white;
            border: none;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
            width: 100%;
        }}
        .login-form input[type="submit"] {{
            background-color: #1f77b4;
            color: white;
            padding: 12px 15px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            width: 100%;
        }}
        </style>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <div class="header-container">
            <img src="data:image/png;base64,{encoded_logo}" alt="Logo UPCH">
            <h1>Plataforma de Gestión de Cursos - UPCH</h1>
        </div>
    """, unsafe_allow_html=True)

    st.subheader("Inicio de Sesión")

    with st.form(key="login_form"):
        st.markdown('<style>div[data-baseweb="input"] input {color: white !important;}</style>', unsafe_allow_html=True)
        username = st.text_input("Usuario:", value="")
        password = st.text_input("Contraseña:", type="password", value="")
        submit = st.form_submit_button("Iniciar Sesión")

    if submit:
        if username == User and password == Password:
            st.session_state.logged_in = True
            st.success("¡Inicio de sesión exitoso!")
            st.balloons()
            st.experimental_rerun()
        else:
            st.error("Usuario o contraseña incorrectos. Por favor, inténtalo de nuevo.")

