#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:37:46 2019

@author: suman.choudhury
"""

#importing the necessary packages
from flask import request,jsonify,Flask
import time
import utils as ut
import cv2

from src.car_recognition import CarRecognition
car_recog = CarRecognition()


app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Vision Api"

@app.route('/recognise',methods=['POST'])

def recognise():
    
    # the data comes in byte format .
    data = request.get_json()
    encoded_content = data['encodedContent']
    
    #start the timer
    start_time= time.time()
    
    #calling up get_image function to convert encoded content to image array
    image_arr = ut.get_image(encoded_content)

    respCode = None
    
    try:
        
        #image_arr = cv2.cvtColor(image_arr, cv2.COLOR_BGR2RGB)
        response = car_recog.predict(image_arr)
        
        if (response =="###"):
            result = {'recognisedIdentifier': 'Car not identified'}
        else:
            result = {'Recognised Car':str(response['Car Name']),
                      'Probabilty': str(response['Probability'])}

    except Exception as e:
        print(str(e))
        respCode = {"code":415, "description": "Unable to recognize the car"}

    api_response = {'result':result}
    
    print(api_response)
    
    print ("total API time: ", time.time()-start_time)
    return jsonify(api_response)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9790)

