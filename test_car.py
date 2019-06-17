#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 18:26:50 2019

@author: suman.choudhury
"""



import cv2 as cv
from src.car_recognition import CarRecognition
car_recog = CarRecognition()


#check for test images
file_name = "tests/00016.jpg"
img_arr = cv.imread(file_name)
result=car_recog.predict(img_arr)
print(result)
    
    

    
