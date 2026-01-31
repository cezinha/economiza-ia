"""
Economiza+ MVP Dashboard
Aplicação principal Streamlit

Executar com: streamlit run app.py
"""

import streamlit as st

# Configuração da página - deve ser o primeiro comando Streamlit
st.set_page_config(
    page_title="Economiza+ MVP",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Definir páginas com títulos acentuados
home = st.Page("pages/0_Home.py", title="Início", icon="🏠", default=True)
visao_geral = st.Page("pages/1_Visao_Geral.py", title="Visão Geral", icon="📊")
analise_usuario = st.Page("pages/2_Analise_Usuario.py", title="Análise de Usuário", icon="🔍")
comparativo = st.Page("pages/3_Comparativo.py", title="Comparativo", icon="📈")

# Criar navegação
pg = st.navigation([home, visao_geral, analise_usuario, comparativo])

# Executar página selecionada
pg.run()
