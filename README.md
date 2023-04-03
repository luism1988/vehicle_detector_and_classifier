<p align="center">
  <img src="https://github.com/luism1988/vehicle_detector_and_classifier/blob/main/streamlit/img/baner.jpg?raw=true" width="400">
</p>

# VEHICLE DETECTOR AND CLASSIFIER 

## Descripción:  
Detección y clasificación de vehículos es un proyecto académico, el cual consiste en detectar vehículos utilizando OpenCv para luego ser clasificados por un modelo de redes neuronales previamente entrenado con un dataset de creación propia. 
En su desarrollo se emplearon diferentes stacks tecnológicos como Python, OpenCV, Keras y Tensorflow y Streamlit (entre otros).

## Objetivo:
- Utilizar openCV para detectar vehículos.
- Creación de un datasaet partiendo de videos grabados en un avenida con tres clases: coche, bus y camión.
- Utilizar el dataset para entrenar varios modelos de clasificación de vehiculos.
- Crear una plicacion para clasificar los vehículos detectados entre coche, bus y camión.
- Presentar los resutados en una interfaz creada con Streamlit.

## Cómo utilizarlo:
-	1-Acceder al directorio:

		 ../vehicle_detector_and_classifier

-   2-Instalar de los requerimientos del sistema:

        $ pip install -r requirements.txt

-   3-Acceder al directorio:

        ../ vehicle_detector_and_classifier/streamlit

-   4-Ejecutar main.py:

        streamlit run main.py

## Dataset:
El dataset fue creado partiendo de videos grabados desde la parte superior de una avenida, luego estos videos fueron procesados por un código en Python con OpenCV. Este script utiliza un modelo de detección “haarcascade_car.xml” para localizar los vehículos y luego guardarlos en imágenes que luego fueron clasificadas manualmente en tres clases: “bus”, “car” y “truck.

El dataset tiene 1109 imágenes distribuidas de la siguiente forma: 
<p align="center">
  <img src="https://github.com/luism1988/vehicle_detector_and_classifier/blob/main/streamlit/img/dataset.png?raw=true" width="400">
</p>
Utilizando el 75% para entrenamiento y el 25% para test.

## Modelo:
El utilizado para realizar la clasificación de vehículos fue entrenado con los datos explicados anteriormente. Para realizar este proyecto se entrenaron tres modelos diferentes:
-	Una red neuronal convolucional customizada.
-	Una red neuronal basada en una red pre entrenada VGG-19.
-	Una red neuronal basada en una red pre entrenada MobileNet.

La red que obtuvo los mejores resultados (y utilizada para clasificar los vehículos detectados) fue la red basada en MobileNet, la cual se no se incluyó la última capa y se le añadieron dos capas densas de 128 neuronas y una capa de salida de 3 neuronas (una para cada clase).a continuación, se pueden ver las curvas y métricas de los modelos de clasificación entrenados:


- ### Curvas y métricas del modelo basado en MobileNet:
<p align="center">
  <img src="https://github.com/luism1988/vehicle_detector_and_classifier/blob/main/streamlit/img/metricas.png?raw=true" width="800">

- ### Curvas y métricas del modelo basado en VGG-19:
<p align="center">
  <img src="https://github.com/luism1988/vehicle_detector_and_classifier/blob/main/streamlit/img/metricas2.png?raw=true" width="800">

- ### Curvas y métricas del modelo basado en una red neuronal convolucional customizada:
<p align="center">
  <img src="https://github.com/luism1988/vehicle_detector_and_classifier/blob/main/streamlit/img/metricas3.png?raw=true" width="800">


