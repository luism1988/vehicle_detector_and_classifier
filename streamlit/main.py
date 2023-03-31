import streamlit as st
import cv2
#from keras.applications.imagenet_utils import preprocess_input, decode_predictions
from keras.models import load_model
#import matplotlib.pyplot as plt
import numpy as np
from funtions import roi_detection, vehicle_classifier_and_labeler

# Load car classifier
car_classifier = cv2.CascadeClassifier('../datasets/cars.xml')
#load model
model = load_model("../nn_model_Mobilenet_200.h5")



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
    cap.set(cv2.CAP_PROP_FPS,0.1)
    count = 2
    while run: #si se la ha dado al boton o no

        # Read the next frame from the video
        ret, frame = cap.read()
        if not ret:
            break

        # Detect cars in the frame
        # Define las coordenadas del ROI (Region of interest)
        x1, y1 = 100, 550
        x2, y2 = 720, 750

        #Region of interest
        roi = frame[y1:y2,x1:x2]

        cars = roi_detection(frame,car_classifier, roi, x1,x2,y1,y2)

        # Para cada deteccion realizar la clasificacion y dibujar la etiqueta
        
        for (x,y,w,h) in cars:
            cv2.rectangle(frame, (x+x1, y+y1), (x+x1+w, y+y1+h), (0, 255, 255), 2)
            if count % 2 ==0:    
                preds = vehicle_classifier_and_labeler(x, y, x1, y1, w, h, model, frame, roi)
                #Dibujar el rectangulo de l deteccion
            
                posicion_etiqueta = (x+x1 , y+y1 - 10)
                #Colocar etiqueta
            preds2 = preds 
            pos = posicion_etiqueta
            cv2.putText(frame, names[np.argmax(preds2)], pos, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
        count += 1       
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #haciendo la imagen que va a mostrar streamlit
        FRAME_WINDOW.image(frame) #pintamos la imagen actual del video despues de todas las características que hemos puesto

    else: 
        st.write("Has salido de la app") #si el boton no esta puesto
        



      