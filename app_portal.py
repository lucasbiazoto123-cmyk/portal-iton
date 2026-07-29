import streamlit as st

# Configuração da página
st.set_page_config(page_title="Portal ITON", page_icon="🏗️", layout="centered")

# Cabeçalho
st.markdown("<h1 style='text-align: center;'>🏗️ Portal Operacional ITON</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Selecione o sistema que deseja acessar abaixo:</p>", unsafe_allow_html=True)
st.divider()

# Botões de Acesso (É só trocar a URL entre aspas pelo link real do seu app no Streamlit)
st.markdown("### 👷 Operação em Campo")
st.link_button("📝 Acessar Diário de Obras", "https://app-diario-obras-8uhrhbzp4qjocwwnr3k7qm.streamlit.app/", use_container_width=True)

st.markdown("### 🚗 Logística e Frotas")
st.link_button("⛽ Acessar Controle de Frotas", "https://app-frotas-8mvvz4aduycpdawa5vts7w.streamlit.app/", use_container_width=True)

st.divider()
st.markdown("<p style='text-align: center; font-size: 12px; color: gray;'>Desenvolvido internamente para otimização de processos.</p>", unsafe_allow_html=True)
