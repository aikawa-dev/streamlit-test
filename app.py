import streamlit as st

st.title('私のPythonアプリへようこそ！')
st.write('これはStreamlitで作成したWebアプリです。')

# ユーザーに名前を聞く
name = st.text_input('あなたのお名前は？')

if name:
    st.write(f'こんにちは、{name}さん！')
    st.button('ここを押してみて', on_click=lambda: st.balloons())
