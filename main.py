from ctypes.wintypes import LPWIN32_FIND_DATAA
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title("STREAMLIT")

st.write("progress bar")
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range (100):
  latest_iteration.text(f"iteration {i+1}")
  bar.progress(i+1)
  time.sleep(0.1)


expander = st.expander('Click for other games!')
expander.button("game 1")
expander.write("game 2")
expander.write("game 3")
expander.write("game 4")
expander.write("game 5")

# option =st.text_input('Please tell me your hobby!')
# condition = st.slider('Hows your body condition from scale 1-100',0, 100, 50)

# "your hobby is",option
# "condition :" , condition


# if st.checkbox('Show Image'):
#   img = Image.open('spongboobs.jpg')
#   st.image(img, caption='spongebob',use_column_width=True)


# left_column, right_column = st.columns(2)
# left_button = left_column.button('left column show words')
# if left_button:
#   right_column.write('This is right column')