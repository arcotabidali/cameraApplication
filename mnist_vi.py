# -*- coding: utf-8 -*-
"""MNIST_VI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OuGGppzB8iqDMM1VOpC2IQllGjM-bzDe
"""

import tensorflow as tf
from tensorflow.keras import layers,models
from tensorflow.keras.datasets import mnist
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
import numpy as np
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split

#division of Testing and Training Data from the MNIST DATASET
(Training_Part, Training_outputs) , (Testing_output, Testing_outputs) = mnist.load_data()

#Normalizing every 28x28 pixel for activation purpose hence dividing by 255
Training_Part = Training_Part / 255
Testing_output = Testing_output / 255

#Reshaping the Training and the Testing Part
Training_Part = Training_Part.reshape(-1,28,28,1)
Testing_output = Testing_output.reshape(-1,28,28,1)

#Metrics for the Convolution neural Network
no_Filters1 = 25
no_Filters2 = 64
Kernel_size = 3
pooling_size = 2

#Building a Convolution Neural Network
MNIST_CNN_MODEL = models.Sequential([
    
    #The Definition for the Input layer with an input shape of (28,28,1)
    layers.Conv2D(filters=no_Filters1, kernel_size=(Kernel_size, Kernel_size), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D((pooling_size, pooling_size)),
    
    #The Definition of the Hidden Layer 1
    layers.Conv2D(filters=no_Filters2, kernel_size=(Kernel_size, Kernel_size), activation='relu'),
    layers.MaxPooling2D((pooling_size, pooling_size)),

    #Definition of the Hidden Layer 2
    layers.Conv2D(filters=no_Filters2, kernel_size=(Kernel_size, Kernel_size), activation='relu'),
    layers.MaxPooling2D((pooling_size, pooling_size)),
])


MNIST_CNN_MODEL.add(layers.Flatten())
MNIST_CNN_MODEL.add(layers.Dense(64, activation='relu'))

#Output Layer with 10 different classes
MNIST_CNN_MODEL.add(layers.Dense(10, activation='softmax'))

MNIST_CNN_MODEL.compile(optimizer='nadam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
MNIST_CNN_MODEL.fit(Training_Part, Training_outputs, epochs=6, batch_size=20)

MNIST_CNN_MODEL.evaluate(Testing_output, Testing_outputs)

MNIST_CNN_MODEL.save('model')

import pickle
pickle.dump(MNIST_CNN_MODEL, open('model_cnn.pkl', 'wb'))

tf.keras.models.save_model(MNIST_CNN_MODEL,'model_cnn.h5')

import cv2
img_alt = cv2.imread('/content/sample_data/mnist1.png', cv2.IMREAD_GRAYSCALE)
plt.imshow(img_alt)
img_alt = cv2.resize(img_alt,(28,28))
img_alt = np.resize(img_alt,(28,28))
img_alt = img_alt.reshape(-1,28,28,1)
pred = MNIST_CNN_MODEL.predict(img_alt)
print(pred)
pred

