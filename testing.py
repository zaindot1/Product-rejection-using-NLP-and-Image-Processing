import tensorflow as tf
import cv2

model = tf.keras.models.load_model('model.h5')
img_size=150
img_array=cv2.imread('281.jpg',cv2.IMREAD_GRAYSCALE)
backtorgb=cv2.cvtColor(img_array,cv2.COLOR_GRAY2RGB)
new_array=cv2.resize(backtorgb,(img_size,img_size))
import numpy as np
X_input=np.array(new_array).reshape(1,img_size,img_size,3)
X_input=X_input/255.0
prediction=model.predict(X_input)
print(prediction)