# Grab_AI_for_SEA
This project focusses on automatic car recognition which was build using pretrained models

## Table of contents
* [General info](#general-info)
* [Project Structure](#technologies)
* [Setup](#setup)
* [Project Execution Steps](#project)

## General info
The objective of this project is to develop a working model that can automatically identify cars given an image. It is targeted to serve as an automatic car recognition api.

The dataset used for this model was the [cars dataset](https://ai.stanford.edu/~jkrause/cars/car_dataset.html)

ResNet152 was used as a pretrained model which was further fine tuned for our custom image recognition engine.

The codes for the project is kept in the src folder and the common scripts are kept in the scripts folder.

Current validation accuracy for the cars dataset stands at 90% which can be further improved if trained for a larger period of time. Due to time constraints , further hyper-parameter optimisation for the network could not be done.

## Project Structure

The entire project structure is as follows:

## Dataset

The dataset for this challenge was taken from [cars dataset](https://ai.stanford.edu/~jkrause/cars/car_dataset.html)

The Cars dataset contains 16,185 images of 196 classes of cars. The data is split into 8,144 training images and 8,041 testing images. As the GRAB AI challenge clearly stated just to take the training dataset for preparing the model , only the [training set](http://imagenet.stanford.edu/internal/car196/cars_train.tgz) containing 8144 inages were taken for training our model.
The [meta data](https://ai.stanford.edu/~jkrause/cars/car_devkit.tgz) was used to crop out the images.


## Project Execution Steps

These were the steps in brief taken to carry out the project

1. Step 1: Analysing the dataset and Data preprocessing

*We looked at some of the samples of the data and found that apart from the images of car, there were reduntant information like person , various background etc. So we used the meta data provided in the dataset and preprocessed the data and saved it in corresponding train and valid folders inside the dataset directory.

