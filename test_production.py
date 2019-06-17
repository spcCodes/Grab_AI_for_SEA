#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:41:15 2019

@author: suman.choudhury
"""

from PIL import Image
from io import BytesIO        
import base64
import unittest
import requests
class TestVisionServer(unittest.TestCase):

    def get_base64_string(self,cropped):
        pil_img = cropped
        buff = BytesIO()
        pil_img.save(buff, format="JPEG")
        base64_string = base64.b64encode(buff.getvalue()).decode("utf-8") 
        return base64_string
        
    def get_base64(self , cropped):
        base = base64.b64encode(cropped.read())
        return base

    def get_inputs(self):
        #img = open("test/Ridomil Gold_test1.jpg", "rb")
        image_path = "cars_test/00020.jpg"
        #aa=image_path.split(os.path.sep)[1].split("_")
        img = Image.open(image_path)
        #testoutput = aa[0] + ' ' + aa[1]
        return img

    def test_vision_server(self):
        testimage = self.get_inputs() 
        encodedString = self.get_base64_string(testimage)
        payload = {'encodedContent' : encodedString}
        r = requests.post("http://0.0.0.0:9790/recognise" , json = payload)
        print(r.text)
        #j = json.loads(r.text)
        print(r.text)
        #ri = j['result']['recognisedIdentifier']
        #self.assertEqual(ri.lower() , testoutput.lower())

if __name__ == '__main__':
    unittest.main()  
