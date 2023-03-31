import streamlit as st
from IPython.display import HTML
import base64
import cv2
import cv2
import time
from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
# Load car classifier
car_classifier = cv2.CascadeClassifier('../datasets/cars.xml')
#load model
modelt = load_model("../nn_model_Mobilenet_200.h5")



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

    run = st.checkbox('Play video and detection') #boton para activar la ejecucion del video.

    names = ['bus', 'car', 'truck']
    FRAME_WINDOW = st.image([]) #imagen en streamlit
    cap = cv2.VideoCapture('mer1_mod.mp4')

    while run: #si se la ha dado al boton o no

        ret, frame = cap.read()
        if not ret:
            break   
            
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect cars in the frame
        cars = car_classifier.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5, minSize=(50, 50))

        # Draw bounding boxes and labels around the vehicles 
        for (x,y,w,h) in cars:
            #texto = "Prueba"
            posicion_etiqueta = (x , y - 10)
            
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
            
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #haciendo la imagen que va a mostrar streamlit
        FRAME_WINDOW.image(frame) #pintamos la imagen actual del video despues de todas las características que hemos puesto

    else: 
        st.write("Has salido de la app") #si el boton no esta puesto
        cap.release()
        cv2.destroyAllWindows() #cierra todo



      