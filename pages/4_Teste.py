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
    		col1, col2 = st.columns(2, gap="small")
    		with col1:
			# main_image
        		st.image("graphics/other/dungeon_crawler.png")

        		st.caption("The Dungeon: a streamlit dungeon crawler game", unsafe_allow_html=True)
   		with col2:
        		intro_text = """
	  		Explore the depths of an ancient dungeon in the first streamlit-based dungeon crawler game!
        		Navigate through dangerous traps, defeat fearsome monsters and uncover the secrets of the DuNgeOn.
        		With intuitive controls and beautiful graphics, this game will keep you entertained for hours.
        		Experience the thrill of adventure as you progress through levels and uncover powerful treasures.
        		Join the adventure today and become the hero of the dungeon!
        		"""
        		st.write(f'<p style="color:#9c9d9f">{intro_text}</p>', unsafe_allow_html=True)
	

    			st.subheader("| Game start")
    			st.write(
				'<p style="color:#9c9d9f">To start the game go to the "start game" tab. Please be sure to switch to <b>dark mode</b> or the custom theme. The Dungeon is meant to be played in the dark! </p><p style="color:#9c9d9f">Game update (april 2023): currently testing level2</p>',
				unsafe_allow_html=True,)
    				st.subheader("| Controls")
    			st.write(
        			'<p style="color:#9c9d9f">Desktop: please use keyboard arrows | Mobile (Android, Chrome): please use on-screen buttons | iOS: unfortunately, the auto-scrolling feature does not work yet for iOS.</p><br>',
        			unsafe_allow_html=True,)


	with tab2:

		st.markdown("""AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA""")

