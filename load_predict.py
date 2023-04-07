import tensorflow as tf
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

load_predict = load_model('/home/windows/Desktop/Blure_image_detection/ZAF056_CV_BlurredImage-detection/model.h5')

def predictImage(filename, model):
    img = image.load_img(filename,target_size=(96, 96))
    plt.imshow(img)
    Y = image.img_to_array(img)
    X = np.expand_dims(Y,axis=0)
    val = model.predict(X)
    if val == 1:
        plt.xlabel("Not a Blurred",fontsize=30)
    elif val == 0:
        plt.xlabel("Blurred",fontsize=30)


path = "/home/windows/Desktop/Blure_image_detection/ZAF056_CV_BlurredImage-detection/test/test/test/agsxpjnxlikqtitjyivk.jpg"
predictImage(path, load_predict)