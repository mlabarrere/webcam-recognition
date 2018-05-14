# Webcam Recognition
A tool for detecting who is in front of your webcam

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

[![CodeFactor](https://www.codefactor.io/repository/github/mlabarrere/webcam-recognition/badge)](https://www.codefactor.io/repository/github/mlabarrere/webcam-recognition)  [![BCH compliance](https://bettercodehub.com/edge/badge/mlabarrere/webcam-recognition?branch=master)](https://bettercodehub.com/)


## Download

To get the source code, run:
```
git clone https://github.com/mlabarrere/webcam-recognition.git
```

## Project Structure

```
Webcam Recognition
│   test_reco.py
│   train_reco.py
│   README.md (To Complete)
│   requirements.txt
│   setup.py (To Do)
│   LICENSE.md
│
└───src
│       │   __init__.py
│       │   lib.py
│  
└───haar
│       │  haarcascade_frontalface_alt.xml
│       │  haarcascade_frontalface_alt2.xml
│       │  haarcascade_frontalface_alt_tree.xml
│       │  haarcascade_frontalface_default.xml
│  
└───data
│       │   You will populate it
│  
└───model
│       │   It will populate on its own
```

### Installing

First, let's install the required libraries, `cd` to the root of the project where `requirements.txt` is :

```shell
cd yourDirectory/webcam-recognition/
```

then

```shell
pip install -r requirements.txt
```

Cool, you've got everything ready to run the program

### Train your model

The model is based on [Haar like features](https://en.wikipedia.org/wiki/Haar-like_feature), hence, you need to train your model.

For this, you need to gather pictures of you and your friends (ask them before). Then put all thoses pictures into separated named folders ìnto the `data` folder. Please, use only common letters (look how I had to remove the `é` from `Pépito`).

To train your model to detect Pépito and Paolo, do something like this:

```
data
└───Pepito
│       │   picture1.jpg
│       │   picture2.png
│       │   picture_with_whatever_name_or_classic_format.jpg
│
└───Paolo
│       │   picture1.jpg
│       │   picture2.png
│       │   picture_with_whatever_name_or_classic_format.jpg
```

Nice, it seems that you are ready to train your model now.

Ok, then you just have to `cd` to the root of the repository, and run:

```shell
python train_reco.py
```

The prompt will show you things like:

```
Preparing data...
Training for Pepito, Paolo               # Check if this is ok
[ INFO:0] Initialize OpenCL runtime...   # You just don't care about it
Data prepared

Training the model...
Training complete

Saving model...
Saving done
```

#### Train your model - Best Practices

The thing is, Haar is not Google's top neural networks, hence you need to help him to do his work.

* Quality over quantity:

  One good picture, like one from a recent ID card, will always be better than ten from your last Project X party.

* Balance the number of pictures over people to reduce over/under fitting:
  
  Assume Pépito has 30 pictures to train on, and Paolo only 5, you can be sure the model will say everyone is Pépito.


* Crop your pictures to avoid loosing training examples:
  
  If the prompt prints this `Impossible to find Paolo`, it means that on a picture, he wasn't able to recognise anyone. 
  So there is three main reason of this : 
    1. There is multiple faces on this picture
    2. The algorithm cannot detect a face from a weird light
    3. The picture has no background, do not crop the face to make the face filling the picture. Let some air. 
  
  
  In any cases: you just lost a training example.


* Turn lights on and show yourself:

  The model will have hard time recognising you in a middle of the night, or if you have changed drastically from your training pictures. Ex : You just shaved your beloved beard, you have no longer a skater's long hair, etc...


* Avoid twins:

  Well, because... They are twins.


#### Test your model

You have now the folder `model` filled with two files:
1. `model.xml` : The model :)
2. `dict.pickle` : The mapper, because the model can associate only faces with numbers, this dictionary will map numbers to faces.

But you don't have to care about it.

Now, let's see how the model recognizes you:

```shell
python test_reco.py
```

You'll see the webcam fire, and see yourself in a window, with a green box around your face.

Does the model recognize you? If not, you need to train it better, with more and better pictures. 



Thanks for reading.



Sorry for the long post, here is a potatoe: 🥔



## Author

* **Mickaël Labarrère** - [mlabarrere](https://github.com/mlabarrere)

See also the list of [contributors](https://github.com/mlabarrere/webcam-recognition/graphs/contributors) who participated in this project.

## License

This project is licensed under the Apache 2 License - see the [LICENSE.md](https://github.com/mlabarrere/webcam-recognition/LICENSE.md) file for details



## Acknowledgments

* [@MAmineA](https://github.com/MAmineA)
* [@benjaminborac](https://github.com/benjaminborac)
