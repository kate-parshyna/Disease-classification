#Description
This program classifies skin diseases.
    -Known diseases:
    -couperose;
    -eczema;
    -herpes;
    -ineffective;
    -lichen;
    -normal;
    -pruritus nodular;
    -psoriasis.
#Setup
To run the project you need to set the requirements.

python instatall:    
````
sudo apt-get update

sudo apt-get install python3.6
````
requirements install:
````
sudo pip3 install tensorflow==1.12.0

sudo pip3 install tensorflow-hub

sudo pip3 install Flask==1.0.2

sudo pip3 install Flask-Cors==3.0.7
````


#Training
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
##Usage
````
python3 retrain.py --image_dir path/to/folder/with/dataset/ 
````

##Example
````
python3 retrain.py --image_dir train/
````
#Server start 
For training, you must start the server:

````
python3 desease_detector.py 
````
#Testing
After the server is running, you need to go to the server address, where you can see the interface for testing.


