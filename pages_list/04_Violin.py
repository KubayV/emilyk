# Core Pkgs
import streamlit as st

from PIL import Image
from PIL import ImageOps
import sys

from functions.functions import set_bg_hack

set_bg_hack("Style/cool-backgroundBlue.png")

st.title("EmilyK®")
img = Image.open("Images/ViolinImg.png")
st.image(img, use_column_width=True)
st.divider()
