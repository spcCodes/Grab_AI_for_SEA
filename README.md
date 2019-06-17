# Grab_AI_for_SEA
This project focusses on automatic car recognition which was build using pretrained models

## Table of contents
* [General info](#general-info)
* [Project Structure](#technologies)
* [Setup](#setup)

## General info
The objective of this project is to develop a working model that can automatically identify cars given an image. It is targeted to serve as an automatic car recognition api.

The dataset used for this model was the [cars dataset](https://ai.stanford.edu/~jkrause/cars/car_dataset.html)

ResNet152 was used as a pretrained model which was further fine tuned for our custom image recognition engine.

The codes for the project is kept in the src folder and the common scripts are kept in the scripts folder.

Current validation accuracy for the cars dataset stands at 90% which can be further improved if trained for a larger period of time. Due to time constraints , further hyper-parameter optimisation for the network could not be done.

## Project Structure

