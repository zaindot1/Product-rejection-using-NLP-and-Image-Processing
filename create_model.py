import os

import tensorflow as tf
from tensorflow import keras
from keras import layers
import cv2

def my_model():
    inputs=keras.Input(shape=(150,150,3))
    x=layers.Conv2D(32,3)(inputs)
    x=keras.activations.relu(x)
    x=layers.MaxPool2D()(x)
    x=layers.Conv2D(64,3)(x)
    x=keras.activations.relu(x)
    x=layers.MaxPool2D()(x)
    x=layers.Conv2D(128,3)(x)
    x=keras.activations.relu(x)
    x=layers.MaxPool2D()(x)
    x=layers.Conv2D(128,3)(x)
    x=keras.activations.relu(x)
    x=layers.MaxPool2D()(x)
    x=layers.Flatten()(x)
    x=layers.Dropout(0.5)(x)
    x=layers.Dense(512,activation='relu')(x)
    outputs=layers.Dense(1,activation='sigmoid')(x)
    model=keras.Model(inputs=inputs,outputs=outputs)
    return model

model=my_model()
model.summary()

model.compile(loss='binary_crossentropy',optimizer='Adam',metrics=['acc'])

training_Data=[]
img_size=150
Datadirectory = "Train_Dataset/"
Classes=["4","5"]
def create_training_data():
    for category in Classes:
        path=os.path.join(Datadirectory,category)
        class_num=Classes.index(category)
        for img in os.listdir(path):
            try:
                img_array=cv2.imread(os.path.join(path,img),cv2.IMREAD_GRAYSCALE)
                backtorgb=cv2.cvtColor(img_array,cv2.COLOR_GRAY2RGB)
                new_array=cv2.resize(backtorgb,(img_size,img_size))
                training_Data.append([new_array,class_num])
            except Exception as e:
                pass
create_training_data()
import random
random.shuffle(training_Data)
import numpy as np
X=[]
y=[]

for features,label in training_Data:
    X.append(features)
    y.append(label)

X=np.array(X).reshape(-1,img_size,img_size,3)
X=X/255.0
Y=np.array(y)

model.fit(X,Y,batch_size=64,epochs=10,verbose=2,validation_split=0.1)
model.save('model.h5')