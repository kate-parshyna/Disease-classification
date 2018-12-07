# Disease-classification
## Overview
This program classifies skin diseases. This program use TensorFlow Hub to ingest pre-trained pieces of models, or modules as they are called. For starters, we will use the image feature extraction module with the Inception V3 architecture trained on ImageNet
    The model classifies the following diseases:
    
    -couperose;
    -eczema;
    -herpes;
    -ineffective;
    -lichen;
    -normal;
    -pruritus nodular;
    -psoriasis.
## Installation
Before starting the classification, it is necessary to install the modules that are used in this program.

Python instatall:    
````
sudo apt-get update

sudo apt-get install python3.6
````
Requirements install:
````
sudo pip3 install tensorflow==1.12.0

sudo pip3 install tensorflow-hub

sudo pip3 install Flask==1.0.2

sudo pip3 install Flask-Cors==3.0.7
````
## Usage

### Training

For classification used Tensorflow inception v3 model. At the entrance is a folder with dataset.

Folder structure:
````
dataset/
    couperose/
        couperose_1.jpg
        couperose_2.jpg
        .
        .
        .
        couperose_n.jpg
    eczema/
        eczema_1.jpg
        eczema_2.jpg
        .
        .
        .
        eczema_n.jpg
    herpes/
    ineffective/
    lichen/
    normal/
    pruritus nodular/
    psoriasis/
````
This command is used for training:

````
python3 retrain.py --image_dir path/to/folder/with/dataset/ 
````

### Testing
In order to start testing, you need to start the server where the testing will be conducted.

The server is started by the following command:

````
python3 desease_detector.py 
````
After the server is running, you need to go to the server address, where you can see the interface for testing.


