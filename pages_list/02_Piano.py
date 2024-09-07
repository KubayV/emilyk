# Core Pkgs
import streamlit as st

from PIL import Image
from PIL import ImageOps
import sys

from functions.functions import set_bg_hack

set_bg_hack("Style/cool-backgroundBlue.png")
st.title("EmilyK®")
img2 = Image.open("Images/PianoKeyboard2.png")
st.image(img2, use_column_width=True)
# st.divider()

with st.expander("Year 2024"):
#     st.write('''
#         The chart above shows some numbers I picked for you.
#         I rolled actual dice for these, so they're *guaranteed* to
#         be random.
#     ''')
    col1, col2 = st.columns(2)

    with col1:
        VIDEO_URL = "https://youtu.be/DDJ4kAVz4cg"
        st.video(VIDEO_URL)
        st.subheader("Emily K - May 2024. ")
        st.subheader("Linus And Lucy - Vince Guaraldi")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        VIDEO_URL = "https://youtu.be/9j1vDkElnkA"
        st.video(VIDEO_URL)
        st.subheader("Emily K - March 2024. "
                     "Lowside Blues - Joanna MacGregor")

    with col2:
        VIDEO_URL = "https://youtu.be/VniidxskOWI"
        st.video(VIDEO_URL)
        st.subheader("Emily K - May 2024. "
                     "Introduction and Fugato in D Minor - Cuthbert Harris")

# st.divider()

with st.expander("Year 2023"):
#     st.write('''
#         The chart above shows some numbers I picked for you.
#         I rolled actual dice for these, so they're *guaranteed* to
#         be random.
#     ''')
    col1, col2 = st.columns(2)

    with col1:
        VIDEO_URL = "https://youtu.be/-kLUar4G2lA"
        st.video(VIDEO_URL)
        st.subheader("Emily K - April 2023. "
                     "Albert Ellmenreich - Spinnerlied ")

    with col2:
        VIDEO_URL = "https://youtu.be/g5weArAnZTY"
        st.video(VIDEO_URL)
        st.subheader("Emily K - April 2023. "
                     "Henry Mancini - Pink Panther ")

# st.divider()

with st.expander("Year 2021"):
    col1, col2 = st.columns(2)

    with col1:
        VIDEO_URL = "https://youtu.be/NO5rED-7G0g?si=pcCM1yinsaXlHT66"
        st.video(VIDEO_URL)
        st.subheader("Emily K - May 2021. "
                     "Haydn - Sonata in G, Hoboken XVI:8 Allegro ")
