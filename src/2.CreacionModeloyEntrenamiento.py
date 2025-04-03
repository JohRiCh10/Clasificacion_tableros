import os
import pandas
import cv2
from sklearn.model_selection import train_test_split
import numpy
from keras.models import Sequential
import tensorflow as tf
from tensorflow.keras import layers, models


fotos=pandas.read_excel('data.xlsx')


size=500
images=[]
image_size=(size,size)
for i in range(len(fotos)):
    foto=fotos['Foto'][i]
    ruta=fotos['Ruta'][i]
    # print(rf'{ruta}\{foto}')
    foto=cv2.imread(rf'{ruta}/{foto}')
    foto=cv2.resize(foto,image_size)
    # cv2.imshow('foto',foto)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    foto=numpy.array(foto)/255
    images.append(foto)
tipo=fotos[['Tipo_1','Tipo_2','Tipo_3','Tipo_4','Tipo_5']]
X=numpy.array(images)
Y=numpy.array(tipo)
print(f'Forma de X: {X.shape}')
print(f'Forma de Y: {Y.shape}')


input_shape=(size,size,3)
model = Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

model.add(layers.Flatten())

model.add(layers.Dense(100, activation='relu'))
model.add(layers.Dense(100, activation='relu'))

model.add(layers.Dense(5, activation='softmax'))
model.summary()


learning_rate = 0.001
optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])


history = model.fit(X, Y, epochs=20, batch_size=5, validation_split=0.2)

model.save('model.h5')

import matplotlib.pyplot as plt

# Graficar la pérdida (loss)
plt.figure(figsize=(12, 6))

# Pérdida en el conjunto de entrenamiento
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# Error Absoluto Medio (MAE) en el conjunto de entrenamiento
plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Training accuracy')
plt.plot(history.history['val_accuracy'], label='Validation accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

plt.show()