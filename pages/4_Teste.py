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
    		st.subheader("AAAAAAAAAAAAAAAAAAAAAA")
	with tab2:
		└─── pages/testes/
		  └─── About.py # This is a page
  		  └─── 2_Teste.py # This is another page

