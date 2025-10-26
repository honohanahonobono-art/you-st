import streamlit as st
st.title("smoke test")
st.write("ここまで画面に表示できたらデプロイ成功🎯")
# import streamlit as st
# import numpy as np
# import pandas as pd
# from PIL import Image
# import time

# st.title("Streamlit 超入門")

# st.write("DataFrame")
# st.write("プレグレスバーの表示")
# 'Start!!'
# latest_iteration=st.empty()
# bar= st.progress(0)

# for i in range(100):
#     latest_iteration.text(f'Iteration{i+1}')
#     bar.progress (i+1)        
#     time.sleep(0.1)          


# #df=pd.DataFrame({"1列目":[1,2,3,4],"2列目":[10,20,30,40]})
# df=pd.DataFrame(np.random.rand(20,3),columns=(['a','b','c']))
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# #st.dataframe(df.style.highlight_max(axis=0), width=100, height=100) #表示するDataFrameの幅と高さを指定できる。　axis=0は列ごとに最大値をハイライト axis=1は行ごとに最大値をハイライト pandasのスタイルを使って表示できる
# # st.write(df) #これでも表示できるが、幅と高さの指定はできない
# #st.table(df) #静的な表を表示する ただ、テーブルを表示するだけなので、幅と高さの指定はできない
# #"""
# # 章
# ##節
# ### 項
# #'''python
# #import streamlit as st
# #import numpy as np
# #import pandas as pd
# #'''
# #テキストの書き方
# #"""

# df=pd.DataFrame(np.random.rand(100,2)/[50,50]+[35.69,139.70],columns=(['lat','lon']))
# st.map(df)

# st.write("Display Image")

# st.write("Interactive Widgets")

# if st.checkbox("Show Image"):
#     img=Image.open('Duolingo_Sharing.png')
#     st.image(img,caption='Duolingo',use_container_width=True)

# option=st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,10))
#     )
# "あなたの好きな数字は、",option,"です。"
# text=st.sidebar.text_input("あなたの趣味を教えてください。")
# "あなたの趣味は、",text,"です。"

# condition=st.sidebar.slider("あなたの今の調子は？",0,100,50)
# "コンディション：",condition

# left_column,right_column=st.columns(2)
# button=left_column.button("右カラムに文字を表示")
# if button:
#     right_column.write("ここは右カラムです。")

# expander=st.expander("問い合わせ")
# expander.write("問合せ内容を書く")

# text1=st.text_input("あなたの趣味を教えてください。")
# "あなたの趣味は、",text1,"です。"

# condition1=st.slider("あなたの今の調子は？",0,100,50)
# "コンディション：",condition1

