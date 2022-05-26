import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time
import random

st.title("Welcome!")

st.header("This is a website created by `Brian Salim`")
st.write("click [here](https://github.com/SIT21A3804) to check my GitHub\n")

"lets play a food quiz!"
country = st.selectbox('どの国の料理が一番好きですか？',('日本','中国' , '韓国','アメリカ'))

carbs = st.selectbox('どんな炭水化物が好きですか？',('ごはん','めん' , 'パン'))

junk = st.radio("ジャンクフードは好きですか？",('はい', 'いいえ'))

if st.button('おすすめの食べ物は：'):
  latest_iteration = st.empty()
  bar = st.progress(0)

  for i in range (100):
    latest_iteration.text(f"少々お待ちください {i+1}")
    bar.progress(i+1)
    time.sleep(0.01)
  if country == '日本':
    if carbs == 'めん':
      if junk == 'はい':
        "カップ麺"
      else :
        "そば"
    elif carbs == 'ごはん':
      if junk == 'はい' :
        "ごはんバーガー"
      else :
        "焼き飯"
    else :
      if junk == 'はい':
        "マックドナルド"
      else :
        "カレーパン"
  elif country == '中国':
    if carbs == 'めん':
      if junk == 'はい':
        "担々麵"
      else :
        "焼きそば"
    elif carbs == 'ごはん':
      if junk == 'はい' :
        "ごはんはジャンクフードじゃないよ！"
      else :
        "チャーハン"
    else :
      if junk == 'はい':
        "マックドナルド"
      else :
        "肉まん"
  elif country == '韓国':
    if carbs == 'めん':
      if junk == 'はい':
        "辛ラーメン"
      else :
        "ジャージャー麺"
    elif carbs == 'ごはん':
      if junk == 'はい' :
        "ごはんはジャンクフードじゃないよ！"
      else :
        "ビビンパ"
    else :
      if junk == 'はい':
        "マックドナルド"
      else :
        "クリームチーズガーリックパン"
  else:
    if carbs == 'めん':
      if junk == 'はい':
        "マカロニ・チーズ"
      else :
        "スパゲッティとミートボール"
    elif carbs == 'ごはん':
      if junk == 'はい' :
        "ごはんはジャンクフードじゃないよ！"
      else :
        "ロコモコ"
    else :
      if junk == 'はい':
        "マックドナルド"
      else :
        "ハムサンド"
  





























# guess_number = 3
# tries = 5
# count = 0
# st.write(guess_number)
# while tries > 0:
#   guess =st.selectbox(
#   "数字を選ぼう!",
#   list(range(0, 21)),help=f' {str(tries)} 回トライがが残ってる')

#   ##
#   while guess == 0: st.stop()
#   ##

#   if guess > 0.:
#     if guess == guess_number:
#       st.write("勝利！\n")
#       st.stop()
#     elif guess > guess_number:
#       st.write('数字が大きすぎ、 もっと小さい数字を入れて！\n')
#     elif guess < guess_number:
#       st.write('数字が小さすぎ、　もっと大きい数字を入れて！\n')

#   tries -= 1
#   count += 1

# if tries ==0:
#   st.write('数字は ' + str(guess_number)+ 'です。')
#   st.write('敗北!\n')





  



# expander = st.expander('Click for other games!')
# expander.button("game 1")
# expander.write("game 2")
# expander.write("game 3")
# expander.write("game 4")
# expander.write("game 5")

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