import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?   
    - Check out [streamlit.io](https://streamlit.io)
    - Jump into our [documentation](https://docs.streamlit.io)
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)

st.markdown(
    """
    **Selecione um dos itens abaixo ou abre o menu ao lado**
    """)

col1, col2, col3 = st.columns(3)

with col1:
    AA = st.button("Plotting demo")
    if AA:
        switch_page("1_📈_Plotting_Demo.py")

with BB:
    BB = st.button("Mapping demo")
    if BB:
        switch_page("2_🌍_Mapping_Demo.py")

with CC:
    CC = st.button("Data demo")
    if CC:
        switch_page("3_📊_DataFrame_Demo.py")
