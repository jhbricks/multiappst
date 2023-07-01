import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

options = st.sidebar.selectbox("Selecione uma opção:", ("Paraná", "Núcleo Territorial Central"))

if options == "Paraná":
	tab1, tab2 = st.tabs(["intro", "start game"])
	with tab1:
		st.subheader("| Intro")
    		st.write(f'<p style="color:#9c9d9f">{intro_text}</p>', unsafe_allow_html=True)
	with tab2:
		└─── pages/testes/
		  └─── About.py # This is a page
  		  └─── 2_Teste.py # This is another page

