#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:40:15 2019

@author: suman.choudhury
"""

import os
import datetime
import numpy as np
import base64
import io
from PIL import Image
import cv2
    
def get_image(encoded_content):
    #byte_string = base64.decodebytes(encoded_content)
    content_bytes = encoded_content.encode('utf-8')
    byte_string = base64.decodebytes(content_bytes)
    image = Image.open(io.BytesIO(byte_string))
    w,h = image.size
    num_channels=3
    byte_image = image.tobytes()
    image_arr = np.frombuffer(byte_image, dtype=np.uint8)
    image_arr = image_arr.reshape(h, w, num_channels)
    image_arr = image_arr.astype(dtype='float32')
    
    return image_arr

def debug_image(image, result, num_faces):
    debug_dir = "/tmp/debug_images"
    if not os.path.exists(debug_dir):
        os.mkdir(debug_dir)  
    
    if result is not None:
        tag = result["recognisedIdentifier"]
    else:
        tag = str(result)

    tag = str(num_faces)+"_"+str(tag)

    filename = str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + "_" + str(tag) + ".jpg"
    filePath = os.path.join(debug_dir,filename)
    cv2.imwrite(filePath, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
    
    
    

