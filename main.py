import streamlit as st
import pandas as pd
import time as ts
from datetime import time
from matplotlib import pyplot as plt
import numpy as np
tabel=pd.DataFrame({'Column 1':[1,2,3,4,5,6]})

st.markdown("""
            <style>
            .st-emotion-cache-w3nhqi.ef3psqc5
            {
            visibility: hidden
            }
            </style>
            """, unsafe_allow_html=True)
st.title("Я люблю булочки!")
st.subheader("Спасибо за булочку!")
st.header('И за кофе!')
st.text("Лови поцелуйчики от меня!")
st.image("i.jpg", caption='Мои поцелуйчики', width=180)
st.audio('zvuk-poceluya.mp3')
st.markdown("")
json={'a', 'b'}
st.json(json)
st.latex(r'\begin{pmatrix}a&b\\c&d\\e&o\end{pmatrix}')
st.write('### H3')
st.metric(label='Wind Speed', value="120ms", delta='1.4ms')
st.table(tabel)
st.dataframe(tabel)
state = st.checkbox('проверка чек бокса', value=True)
if state:
    st.write('Hi')
else:
    pass
def change():
    print(st.session_state.checker)
state=st.checkbox("Checkbox", value=True, on_change=change, key="checker")
#radio_btn = st.radio("Где ты живешь?", options=("US","UK","Russia"))
#print(radio_btn)
def btn_click():
    print('Button cleket for save info')
btn=st.button("Click Me!", on_click=btn_click)
select=st.selectbox("What is your favorite car?", options=("Lada", "Toyota", "BMW"))
print(select)
multi_select=st.multiselect("What is your favorite Tech Barand?", options=("Microsoft", "Apple", "Yandex"))
st.write(multi_select)
st.title("Uploading Files")
st.markdown("---")
image = st.file_uploader("Please upload an Image", type=["png", "jpg", "pdf"])
if image is not None:
    st.image(image)

video = st.file_uploader("Please upload an Video", type=["mp4"])
if image is not None:
    st.video(video)

audio = st.file_uploader("Please upload an audio", type=["mp3"])
if image is not None:
    st.audio(audio)
def converter(value):
    m,s,mm=value.split(":")
    t_s=int(m)*60+int(s)+int(mm)/1000
    return t_s
images = st.file_uploader("Please upload an Image or Video", type=["png", "jpg", "pdf"], accept_multiple_files=True)
if images is not None:
    for image in images:
        st.image(image)

val = st.slider('Ползунок', min_value=10, max_value=110, value=70)
print(val)

vals = st.text_input("Введине названия", max_chars=50)
print(vals)

valss = st.text_area("Описание темы")
print(valss)

val_data = st.date_input("Введите дату")
print(val_data)


val_timer = st.time_input("Введение время", value=time(0,0,0))
print(val_timer)
if str(val_timer) == "00:00:00":
    st.write("Введение время")
else:
    sec = converter(str(val_timer))
    print(sec)
    bar = st.progress(0)
    per=sec/100
    progress_status=st.empty()
    for i in range(100):
        bar.progress(i+1)
        progress_status.write(str(i+1) + "%")
        ts.steep(per)
st.markdown("<h1 style='text-align: center;'>User Registration</h1>", unsafe_allow_html=True)
form = st.form("Form 1")
form.text_input("First Name")
form.form_submit_button("Submit")

st.markdown("<h1 style='text-align: right;'>User Registration 2</h1>", unsafe_allow_html=True)
with st.form("Form 2"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input("First Name")
    l_name = col2.text_input("Last name")
    st.text_input("Email Address")
    st.text_input("Password")
    st.text_input("Confirm Password")
    day, month, year=st.columns(3)
    day.text_input("Day")
    month.text_input("Month")
    year.text_input("Year")
    s_state = st.form_submit_button("Submit")
    if s_state:
        if f_name == "" and l_name == "":
            st.warning("Please Fill above fields")
        else:
            st.success("Submitted Succesesfully")
x=np.linspace(0,10,100)
bar_x=np.array([1,2,3,4,5])
ept = st.sidebar.radio("Select Any Grapgh", options=("Line", "Bar", "H-bar"))
if ept == 'Line':
    st.markdown("<h1 style='text-align: right;'>Line Chart</h1>", unsafe_allow_html=True)
    fig=plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")

    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x), '--')
    st.write(fig)
elif ept == 'Bar':
    st.markdown("<h1 style='text-align: right;'>Bar Chart</h1>", unsafe_allow_html=True)
    fig=plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.bar(bar_x, bar_x*10)
    st.write(fig)
else:
    st.markdown("<h1 style='text-align: right;'>H Chart</h1>", unsafe_allow_html=True)
    fig=plt.figure()
    plt.style.use("https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle")
    plt.barh(bar_x*10, bar_x)
    st.write(fig)