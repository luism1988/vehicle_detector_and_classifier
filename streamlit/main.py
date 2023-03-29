import streamlit as st
from IPython.display import HTML
import base64


# create sidebar with two "pages": ["Home page","Vehicle Detector and Classifier"]
with st.sidebar:
    sidebar_selection = st.radio('Navigation', ["Home page","Vehicle Detector and Classifier"])

if sidebar_selection == "Home page":
    #Title and header image 
    st.markdown("<h1 style='text-align: center; color: black;'>VEHICLE DETECTOR AND CLASSIFIER</h1>", unsafe_allow_html=True)
    #st.image('./img/barcelona_5.png')
    st.markdown("in construction")
   
    st.subheader("**Created by:**")
    st.subheader("Luis Manuel Rodríguez")
    st.markdown("**Data Scientist | Six Sigma Black Belt | Process Engineer**")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/luis-manuel-rodríguez-román-9b19a8bb)")
    st.markdown("[Github](https://github.com/luism1988)")
  

#page two: show Population and location by District
if sidebar_selection == "Vehicle Detector and Classifier":

    #Title and header image 
    st.markdown("<h1 style='text-align: center; color: black;'>VEHICLE DETECTOR AND CLASSIFIER</h1>", unsafe_allow_html=True)
    #st.image('./img/barcelona_5.png')

    #Subtitle
    st.markdown("**Select a video:**")
    selection = st.selectbox("",["Select a video","Video_1","Video_2","Video_3","Video_4"])
    if selection == "Video_1":
        video_file = open('stars-6962.mp4','rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
    if selection == "Video_2":
        video_file = open('prueba.mp4','rb')
        video_bytes = video_file.read()
        st.video(video_bytes)


    if selection == "Video_3":
        video_file = open('mer17_mod.mp4','rb')
        video_bytes = video_file.read()

        video_html = """
        <video width="720" height="960" controls>
        <source src="data:video/mp4;base64,{}" type="video/mp4">
        Your browser does not support the video tag.
        </video>
        """.format(base64.b64encode(video_bytes).decode('utf-8'))

        st.markdown(video_html, unsafe_allow_html=True)
      
    