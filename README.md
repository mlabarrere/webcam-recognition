# Webcam Recognition
A tool for detecting who is in front of your webcam

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

└───src
│       │   __init__.py
│       │   lib.py
│  
└───haar
│       │  haarcascade_eye.xml
│       │  haarcascade_eye_tree_eyeglasses.xml
│       │  haarcascade_frontalcatface.xml
│       │  haarcascade_frontalcatface_extended.xml
│       │  haarcascade_frontalface_alt.xml
│       │  haarcascade_frontalface_alt2.xml
│       │  haarcascade_frontalface_alt_tree.xml
│       │  haarcascade_frontalface_default.xml
│       │  haarcascade_fullbody.xml
│       │  haarcascade_lefteye_2splits.xml
│       │  haarcascade_licence_plate_rus_16stages.xml
│       │  haarcascade_lowerbody.xml
│       │  haarcascade_profileface.xml
│       │  haarcascade_righteye_2splits.xml
│       │  haarcascade_russian_plate_number.xml
│       │  haarcascade_smile.xml
│       │  haarcascade_upperbody.xml
│  
└───data
│       │   You will populate it
│  
└───model
│       │   It will populate on its own
│  
```

### Installing

First, let's install the required libraries

```shell
cd yourDirectory/webcam-recognition/requirements.txt
```

then

```shell
pip install -r requirements.txt
```

Cool, you've got everything ready to run the program

### Train your model

The model is based on [Haar like features](https://en.wikipedia.org/wiki/Haar-like_feature), hence, you need to train your model.

For this, you need to gather pictures of you and your friends (ask them before). Then put all thoses pictures into separated named folders ìnto the `data` folder.

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

* Balance the number of pictures over people to reduce over/under fitting.
  
  Assume Pépito has 30 pictures to train on, and Paolo only 5, you can be sure the model will say everyone is Pépito.


* Crop your pictures to avoid loosing training examples
  
  If the prompt prints this `Impossible to find Paolo`, it means that on a picture, he wasn't able to recognise anyone. Meaning you just lost a training example.


* Turn lights on and show yourself

The model will have hard time recognising you in a middle of the night, or if you have changed drastically from your training pictures. Ex : You just shaved your beloved beard, you have no longer a skater's long hair, etc...


* Avoid twins

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



## Authors

* **Mickaël Labarrère** - [mlabarrere](https://github.com/mlabarrere)

See also the list of [contributors](https://github.com/mlabarrere/webcam-recognition/graphs/contributors) who participated in this project.

## License

This project is licensed under the Apache 2 License - see the [LICENSE.md](https://github.com/mlabarrere/webcam-recognition/LICENSE.md) file for details


Made with ❤ by Micky

## Acknowledgments

* @MAmineA
* Hat tip to anyone who's code was used
* Inspiration
* etc
