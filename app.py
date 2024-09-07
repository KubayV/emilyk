# Core Pkgs
import streamlit as st
import sys

from functions.functions import set_bg_hack

# pg = st.navigation([st.Page("pages/01_Home.py"), st.Page("pages/02_Piano.py")])
home_page = st.Page("pages_list/01_Home.py", title="Home", icon="🩷")
piano_page = st.Page("pages_list/02_Piano.py", title="Piano", icon="🎹")
lamda_page = st.Page("pages_list/03_Lamda.py", title="Lamda", icon="🎭")
violin_page = st.Page("pages_list/04_Violin.py", title="Violin", icon="🎻")
paintings_page = st.Page("pages_list/05_Paintings.py", title="Paintings", icon="🎨")
# piano_page_2024 = st.Page("pages_list/Piano_years/2024/Piano_2024.py", title="Piano 2024", icon="💯")


pg = st.navigation([home_page, piano_page, lamda_page, violin_page, paintings_page])
st.set_page_config(page_title="Main", page_icon="🩷🩷")
# st.set_page_config(page_title="Main", page_icon=":material/edit:")
pg.run()


#     set_bg_hack("Style/cool-backgroundBlue.png")

    # Adding some content to the sidebar
    # st.sidebar.header("EmilyK®")
    # st.sidebar.divider()

    # menu = ["Home🩷", "Piano🎹", "Lamda🎭", "Violin🎻", "Paintings🎨"]
    # choice = st.sidebar.selectbox("Menu", menu)
    #
    # if choice == 'Home🩷':
    #     st.title("EmilyK®")
    #     st.divider()
    #
    #
    #     col1, col2 = st.columns(2)
    #
    #     with col1:
    #         img = Image.open("Images/Emily2022.jpeg")
    #         img2 = ImageOps.exif_transpose(img)
    #         st.image(img2)
    #
    #     with col2:
    #         st.subheader("Emily K is a girl that lives in South West of UK. "
    #                  "This website is designed to keep track of "
    #                  "Emily's activities and her progress. ")
    #         st.subheader("Please make a selection from the Menu to see her latest "
    #                  "Piano 🎹, Lamda 🎭 or Violin 🎻 videos. You can also view Emily's artwork 🎨")
    #
    # if choice == 'Piano🎹':
    #     st.title("EmilyK®")
    #     img2 = Image.open("Images/PianoKeyboard2.png")
    #     st.image(img2, use_column_width=True)
    #     st.divider()
    #
    #     col1, col2 = st.columns(2)
    #
    #     with col1:
    #         VIDEO_URL = "https://youtu.be/DDJ4kAVz4cg"
    #         st.video(VIDEO_URL)
    #         st.subheader("Emily K - May 2024. ")
    #         st.subheader("Linus And Lucy - Vince Guaraldi")
    #
    #     st.divider()
    #
    #     col1, col2 = st.columns(2)
    #
    #     with col1:
    #         VIDEO_URL = "https://youtu.be/9j1vDkElnkA"
    #         st.video(VIDEO_URL)
    #         st.subheader("Emily K - March 2024. "
    #                      "Lowside Blues - Joanna MacGregor")
    #
    #     with col2:
    #         VIDEO_URL = "https://youtu.be/VniidxskOWI"
    #         st.video(VIDEO_URL)
    #         st.subheader("Emily K - May 2024. "
    #                      "Introduction and Fugato in D Minor - Cuthbert Harris")
    #
    #     st.divider()
    #
    #
    #     col1, col2 = st.columns(2)
    #
    #     with col1:
    #         VIDEO_URL = "https://youtu.be/-kLUar4G2lA"
    #         st.video(VIDEO_URL)
    #         st.subheader("Emily K - April 2023. "
    #                      "Albert Ellmenreich - Spinnerlied ")
    #
    #     with col2:
    #         VIDEO_URL = "https://youtu.be/g5weArAnZTY"
    #         st.video(VIDEO_URL)
    #         st.subheader("Emily K - April 2023. "
    #                      "Henry Mancini - Pink Panther ")
    #
    #     st.divider()
    #
    #
    #     col1, col2 = st.columns(2)
    #
    #     with col1:
    #         VIDEO_URL = "https://youtu.be/NO5rED-7G0g?si=pcCM1yinsaXlHT66"
    #         st.video(VIDEO_URL)
    #         st.subheader("Emily K - May 2021. "
    #                      "Haydn - Sonata in G, Hoboken XVI:8 Allegro ")
    #
    #
    # if choice == 'Violin🎻':
    #     st.title("EmilyK®")
    #     img = Image.open("Images/ViolinImg.png")
    #     st.image(img, use_column_width=True)
    #     st.divider()



    # st.divider()
