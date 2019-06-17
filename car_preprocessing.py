#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 22:49:03 2019

@author: suman.choudhury
"""

import scipy.io
import numpy as np
import os
import cv2 as cv
import random

#class meta information
from scipy.io import loadmat
class_meta = loadmat('/Users/suman.choudhury/Downloads/grab/cars_meta.mat')
meta_info = class_meta['class_names'][0]

#creating dictionary of  car names for mappinhg
car_names={}
for num , car_name in enumerate(meta_info):
    num=num+1
    name = str(car_name)[2:-2]
    car_names[num]=name

def check_data(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def save_traindata(file_name, label_name, bboxes):
    src_folder = 'cars_train'
    num_samples = len(file_name)

    train_split = 0.8
    num_train = int(round(num_samples * train_split))
    train_indexes = random.sample(range(num_samples), num_train)

    for i in range(num_samples):
        fname = file_name[i]
        label = label_name[i]
        (xmin, ymin, xmax, ymax) = bboxes[i]

        src_path = os.path.join(src_folder, fname)
        src_image = cv.imread(src_path)
        height, width = src_image.shape[:2]
        # margins of 16 pixels
        margin = 16
        xmin = max(0, xmin - margin)
        ymin = max(0, ymin - margin)
        xmax = min(xmax + margin, width)
        ymax = min(ymax + margin, height)

        if i in train_indexes:
            dst_folder = 'data/train'
        else:
            dst_folder = 'data/valid'

        dst_path = os.path.join(dst_folder, label)
        if not os.path.exists(dst_path):
            os.makedirs(dst_path)
        dst_path = os.path.join(dst_path, fname)

        crop_image = src_image[ymin:ymax, xmin:xmax]
        dst_img = cv.resize(src=crop_image, dsize=(img_height, img_width))
        cv.imwrite(dst_path, dst_img)


def process_traindata():
    print("Processing train data...")
    cars_annos = scipy.io.loadmat('devkit/cars_train_annos')
    annotations = cars_annos['annotations']
    annotations = np.transpose(annotations)

    file_name = []
    class_ids = []
    bboxes = []
    label_name = []

    for annotation in annotations:
        bbox_xmin = annotation[0][0][0][0]
        bbox_ymin = annotation[0][1][0][0]
        bbox_xmax = annotation[0][2][0][0]
        bbox_ymax = annotation[0][3][0][0]
        class_id = annotation[0][4][0][0]
#        label_name.append('%04d' % (class_id,))
        fname = annotation[0][5][0]
        bboxes.append((bbox_xmin, bbox_ymin, bbox_xmax, bbox_ymax))
        class_ids.append(class_id)
        file_name.append(fname)

    label_name_count = np.unique(class_ids).shape[0]
    
    class_ids_name=[]    
    for id_count in class_ids:
        class_ids_name.append(car_names[id_count])
        
    
    label_name=class_ids_name
    
    print(np.unique(class_ids))
    print('The number of different cars is %d' % label_name_count)

    save_traindata(file_name, label_name, bboxes)




if __name__ == '__main__':
    
    img_width, img_height = 600, 600

    cars_meta = scipy.io.loadmat('devkit/cars_meta')
    class_names = cars_meta['class_names']  # shape=(1, 196)
    class_names = np.transpose(class_names)
    print('class_names.shape: ' + str(class_names.shape))
    print('Sample class_name: [{}]'.format(class_names[8][0][0]))

    check_data('data/train')
    check_data('data/valid')

    process_traindata()

