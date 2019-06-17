#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 19:56:47 2019

@author: suman.choudhury
"""

# import necessary models 

import numpy as np
import cv2 as cv
import tensorflow as tf
from src.resnet152 import resnet152_model
#from config import config

#class meta information
from scipy.io import loadmat
class_meta = loadmat('meta_info/cars_meta.mat')
meta_info = class_meta['class_names'][0]

#creating dictionary of  car names for mappinhg
car_names=[]
for num , car_name in enumerate(meta_info):
    num=num
    name = str(car_name)[2:-2]
    car_names.append(name)

global graph
graph =  tf.get_default_graph()

class CarRecognition(object):
    def __init__(self):
        print("Car Recogniser initialised")
        self.model_path = 'models/model.35-0.90.hdf5'
        self.label_name = car_names
        self.img_width= 224
        self.img_height = 224
        self.num_channels = 3
        self.num_classes = 196
        self.ERROR_VALUE = "###"
        self.threshold = 0.5
        self.model = resnet152_model(self.img_height, self.img_width, self.num_channels, self.num_classes)
        self.model.load_weights(self.model_path, by_name=True)
    def predict(self,img_arr):
        
        #bgr_img = cv.imread(file_name)
        bgr_img = cv.resize(img_arr, (self.img_width, self.img_height), cv.INTER_CUBIC)
        rgb_img = cv.cvtColor(bgr_img, cv.COLOR_BGR2RGB)
        rgb_img = np.expand_dims(rgb_img, 0)
        with graph.as_default():
            preds = self.model.predict(rgb_img)
        prob = np.max(preds)
        class_id = np.argmax(preds)
        name = self.label_name[class_id]
        result = {"Car Name":name,
                  "Probability": prob}
        
        if(prob >= self.threshold):
            return result
        else:
            return self.ERROR_VALUE
        

        
        
        
        
        
        