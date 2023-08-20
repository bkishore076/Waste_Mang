import cv2
import numpy as np
import glob
import random
import tensorflow as tf
from django.templatetags.static import static

model_path = 'saved_models/MobileNetV2'
model = tf.keras.models.load_model(model_path)

def prediction(img):
    print(img)
	#rescaling image
    img = img/255

	#converting to tensor
    tensor_img = tf.convert_to_tensor(img,dtype=tf.float32)

	#resizing image
    tensor_img = tf.image.resize(tensor_img,[224,224])
    tensor_img = tensor_img[tf.newaxis,...,]
    
    class_names = ['cardboard','metal','paper','plastic','trash']

	#predicting image
    return class_names[model.predict(tensor_img).argmax()]

def detect1(img_path):    
	img = cv2.imread(img_path)
	print('prediction for {} is :'.format(img_path.split('/')[-1]),end=' ')
	return prediction(img)
	
print(detect1("/home/suraj/Desktop/web/Project/New Folder/Webapp/PID_app/static/Wastes/04_05_2023_03_12_44.jpg"))