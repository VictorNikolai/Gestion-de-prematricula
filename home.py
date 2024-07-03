import streamlit as st
from PIL import Image

def app():
    image = Image.open('logo_upch.png')

    st.markdown(
        """
        <div style='text-align: center;'>
            <img src='data:image/png;base64,{}' alt='Logo UPCH' style='width: 100px;'>
        </div>
        """.format(image_to_base64(image)),
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center;'>𝙱𝚒𝚎𝚗𝚟𝚎𝚗𝚒𝚍𝚘 𝚊 𝚕𝚊 𝚙𝚊́𝚐𝚒𝚗𝚊 𝚍𝚎 𝙸𝚗𝚒𝚌𝚒𝚘</h1>", unsafe_allow_html=True)
    st.markdown("<h6 style='text-align: center;'>𝑃𝑎𝑟𝑎 𝑐𝑜𝑚𝑒𝑛𝑧𝑎𝑟 𝑐𝑜𝑛 𝑙𝑎 𝑐𝑜𝑛𝑓𝑖𝑔𝑢𝑟𝑎𝑐𝑖𝑜́𝑛 𝑑𝑒𝑙 𝑐𝑖𝑐𝑙𝑜, 𝑝𝑜𝑟 𝑓𝑎𝑣𝑜𝑟 𝑑𝑖𝑟𝑖́𝑔𝑒𝑡𝑒 𝑎 𝑙𝑎 𝑝𝑎𝑟𝑡𝑒 𝑖𝑧𝑞𝑢𝑖𝑒𝑟𝑑𝑎 𝑠𝑢𝑝𝑒𝑟𝑖𝑜𝑟.</h6>", unsafe_allow_html=True)

    
    st.header("𝐒𝐞𝐥𝐞𝐜𝐜𝐢𝐨𝐧𝐚 𝐮𝐧𝐚 𝐬𝐞𝐜𝐜𝐢𝐨́𝐧 𝐩𝐚𝐫𝐚 𝐜𝐨𝐦𝐞𝐧𝐳𝐚𝐫:")

    if st.button("𝚂𝚘𝚋𝚛𝚎 𝙲𝚊𝚢𝚎𝚝𝚊𝚗𝚘"):
        st.query_params["page"] = "sobre_cayetano"
        st.write(
            "𝙽𝚞𝚎𝚜𝚝𝚛𝚘𝚜 𝚎𝚜𝚝𝚞𝚍𝚒𝚊𝚗𝚝𝚎𝚜 𝚎𝚕𝚒𝚐𝚎𝚗 𝚊 𝚕𝚊 𝚄𝚗𝚒𝚟𝚎𝚛𝚜𝚒𝚍𝚊𝚍 𝙲𝚊𝚢𝚎𝚝𝚊𝚗𝚘 𝙷𝚎𝚛𝚎𝚍𝚒𝚊 𝚙𝚘𝚛 𝚖𝚞𝚌𝚑𝚊𝚜 𝚛𝚊𝚣𝚘𝚗𝚎𝚜, 𝚎𝚗𝚝𝚛𝚎 𝚕𝚊𝚜 𝚚𝚞𝚎 𝚛𝚎𝚜𝚊𝚕𝚝𝚊𝚗 𝚕𝚊 𝚊𝚕𝚝𝚊 𝚌𝚊𝚕𝚒𝚍𝚊𝚍 𝚊𝚌𝚊𝚍𝚎́𝚖𝚒𝚌𝚊. 𝙰𝚍𝚎𝚖𝚊́𝚜, 𝚎𝚕𝚒𝚐𝚎𝚗 𝚞𝚗 𝚙𝚎𝚛𝚏𝚒𝚕 𝚍𝚎 𝚙𝚛𝚘𝚏𝚎𝚜𝚘𝚛𝚎𝚜 𝚌𝚘𝚖𝚙𝚛𝚘𝚖𝚎𝚝𝚒𝚍𝚘𝚜 𝚌𝚘𝚗 𝚐𝚎𝚗𝚎𝚛𝚊𝚛 𝚌𝚘𝚗𝚘𝚌𝚒𝚖𝚒𝚎𝚗𝚝𝚘 𝚟𝚊𝚕𝚒𝚘𝚜𝚘 𝚙𝚊𝚛𝚊 𝚒𝚖𝚙𝚞𝚕𝚜𝚊𝚛 𝚎𝚕 𝚍𝚎𝚜𝚊𝚛𝚛𝚘𝚕𝚕𝚘, 𝚢 𝚎𝚕 𝚙𝚘𝚍𝚎𝚛 𝚌𝚘𝚖𝚙𝚊𝚛𝚝𝚒𝚛 𝚌𝚘𝚗 𝚎𝚜𝚝𝚞𝚍𝚒𝚊𝚗𝚝𝚎𝚜 𝚖𝚞𝚢 𝚍𝚎𝚝𝚎𝚛𝚖𝚒𝚗𝚊𝚍𝚘𝚜 𝚎𝚗 𝚜𝚞𝚜 𝚘𝚋𝚓𝚎𝚝𝚒𝚟𝚘𝚜 𝚢 𝚊𝚗𝚜𝚒𝚘𝚜𝚘𝚜 𝚙𝚘𝚛 𝚍𝚎𝚜𝚌𝚞𝚋𝚛𝚒𝚛 𝚗𝚞𝚎𝚟𝚊𝚜 𝚝𝚎𝚗𝚍𝚎𝚗𝚌𝚒𝚊𝚜. 𝙼𝚊́𝚜 𝚊𝚕𝚕𝚊́ 𝚍𝚎 𝚌𝚘𝚗𝚝𝚊𝚛 𝚌𝚘𝚗 𝚕𝚘𝚜 𝚖𝚊́𝚜 𝚊𝚕𝚝𝚘𝚜 𝚎𝚜𝚝𝚊́𝚗𝚍𝚊𝚛𝚎𝚜 𝚒𝚗𝚝𝚎𝚛𝚗𝚊𝚌𝚒𝚘𝚗𝚊𝚕𝚎𝚜, 𝚊𝚌𝚊́𝚍𝚎𝚖𝚒𝚌𝚘𝚜 𝚢 𝚍𝚎 𝚒𝚗𝚟𝚎𝚜𝚝𝚒𝚐𝚊𝚌𝚒𝚘́𝚗, 𝚎𝚗 𝙲𝚊𝚢𝚎𝚝𝚊𝚗𝚘 𝚜𝚎𝚗𝚝𝚒𝚖𝚘𝚜 𝚚𝚞𝚎 𝚝𝚎𝚗𝚎𝚖𝚘𝚜 𝚞𝚗 𝚌𝚘𝚖𝚙𝚛𝚘𝚖𝚒𝚜𝚘 𝚌𝚘𝚗 𝚕𝚊 𝚜𝚘𝚌𝚒𝚎𝚍𝚊𝚍, 𝚢 𝚗𝚘𝚜 𝚎𝚜𝚏𝚘𝚛𝚣𝚊𝚖𝚘𝚜 𝚓𝚞𝚗𝚝𝚘𝚜, 𝚒𝚗𝚟𝚎𝚜𝚝𝚒𝚐𝚊𝚍𝚘𝚛𝚎𝚜, 𝚍𝚘𝚌𝚎𝚗𝚝𝚎 𝚢 𝚎𝚜𝚝𝚞𝚍𝚒𝚊𝚗𝚝𝚎𝚜, 𝚙𝚊𝚛𝚊 𝚕𝚘𝚐𝚛𝚊𝚛 𝚞𝚗 𝚊𝚙𝚘𝚛𝚝𝚎 𝚜𝚒𝚐𝚗𝚒𝚏𝚒𝚌𝚊𝚝𝚒𝚟𝚘 𝚚𝚞𝚎 𝚐𝚎𝚗𝚎𝚛𝚎 𝚋𝚒𝚎𝚗𝚎𝚜𝚝𝚊𝚛 𝚎𝚗 𝚝𝚘𝚍𝚘𝚜 𝚕𝚘𝚜 𝚌𝚊𝚖𝚙𝚘𝚜 𝚎𝚗 𝚕𝚘𝚜 𝚚𝚞𝚎 𝚝𝚛𝚊𝚋𝚊𝚓𝚊𝚖𝚘𝚜."
        )
    if st.button("𝙰𝚍𝚖𝚒𝚜𝚒𝚘́𝚗"):
        st.query_params["page"] = "admision"
        st.write(
            "Contamos con la mejor selección de alumnos, investigadores, docentes que nos han llevado a ser considerados entre las mejores universidades del Perú.\n\n"
            "Si el aprendizaje continuo, la curiosidad por descubrir, y el ser parte de una comunidad de excelencia y prestigio. Elige el proceso que corresponde con tu perfil, y postula a Cayetano. Cuenta con nuestro compromiso de formarte como un profesional de primer nivel."
        )
    if st.button("𝚃𝚎𝚕𝚎́𝚏𝚘𝚗𝚘𝚜 𝚍𝚎 𝙳𝚘𝚌𝚎𝚗𝚝𝚎𝚜"):
        st.query_params["page"] = "telefonos_docentes"
        st.write(
            "- Profesor Juan: +51 987 654 321\n"
            "- Profesora María: +51 987 123 456\n"
            "- Profesor Carlos: +51 987 789 012"
        )
    if st.button("𝚃𝚎𝚕𝚎́𝚏𝚘𝚗𝚘𝚜 𝚍𝚎 𝙰𝚢𝚞𝚍𝚊"):
        st.query_params["page"] = "telefonos_ayuda"
        st.write(
            "- Soporte Técnico General: +51 910 123 456\n"
            "- Ayuda con Plataforma Virtual: +51 910 789 012\n"
            "- Problemas de Acceso a Cuentas: +51 910 345 678\n"
            "- Asistencia para Problemas Técnicos: +51 910 901 234"
        )
    if st.button("𝚃𝚎𝚕𝚎́𝚏𝚘𝚗𝚘𝚜 𝚍𝚎 𝙰𝚍𝚖𝚒𝚗𝚒𝚜𝚝𝚛𝚊𝚌𝚒𝚘́𝚗"):
        st.query_params["page"] = "telefonos_administracion"
        st.write(
            "- Director Administrativo: +51 910 111 222\n"
            "- Coordinador de Finanzas: +51 910 333 444\n"
            "- Jefe de Recursos Humanos: +51 910 555 666\n"
            "- Asistente Administrativo: +51 910 777 888"
        )

def image_to_base64(image):
    import base64
    import io
    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

app()
