import cv2
import numpy as np
from keras.applications.imagenet_utils import preprocess_input

def roi_detection(frame,car_classifier, roi, x1,x2,y1,y2):

    # Dibuja un rectángulo sobre la imagen original
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, ), 2)

    # Convert the ROI to grayscale
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        
    # Detect cars in the frame
    cars = car_classifier.detectMultiScale(gray_roi, scaleFactor=1.05, minNeighbors=5, minSize=(50, 50))
    return cars


def vehicle_classifier_and_labeler(x, y, x1, y1, w, h, model, frame, roi):

    #Dibujar el rectangulo de l deteccion
    cv2.rectangle(frame, (x+x1, y+y1), (x+x1+w, y+y1+h), (0, 255, 255), 2)

    vehicle_image_to_classifier = roi[y:y+h, x:x+w]#Imagen a clasificar

    #vehicle_image_to_classifier = frame[y:y+h, x:x+w]#Imagen a clasificar

    #clasificar la seleccion:
    imaget=cv2.resize(vehicle_image_to_classifier, (224, 224), interpolation = cv2.INTER_AREA)
        
    xt = np.asarray(imaget)
    xt = preprocess_input(xt)
    xt = np.expand_dims(xt,axis=0)
    preds = model.predict(xt)
    return preds
