import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_navigation_bar import st_navbar



#page config
st.set_page_config(page_title="Peeyush", page_icon=":tada:")

#navbar
page = st_navbar(["Home", "About Me", "Projects"])



def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#lottie animation asset
coding = load_lottieurl('https://lottie.host/be38e377-f5cc-48e9-bfc9-714b7ac9dcff/Upu4aooW2h.json')
scroll = load_lottieurl('https://lottie.host/123a306f-86cb-486b-81a6-0ec2f3af1274/YKbVMRjvMU.json')

# animation
st_lottie(coding, height = 200)

# header
st.subheader('Hi, I am Peeyush :wave:',)
st.title('An IT Professional from Cambridge')
st.write('I am passionate about learning new technology, supporting people with IT queries and have an interest in machine learning.')
st.write('')
st.write('')


#with st.container:
