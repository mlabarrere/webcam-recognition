# Webcam Recognition
A tool for detecting people

[![CodeFactor](https://www.codefactor.io/repository/github/mlabarrere/webcam-recognition/badge)](https://www.codefactor.io/repository/github/mlabarrere/webcam-recognition)  [![BCH compliance](https://bettercodehub.com/edge/badge/mlabarrere/webcam-recognition?branch=master)](https://bettercodehub.com/)

Made with ❤ by Micky

## Download

To get source code, run:
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

```

### Installing

First, let install the required libraries

```shell
cd yourDirectory/webcam-recognition/requirements.txt
```

then

```shell
pip install -r requirements.txt
```

Cool, you got everythong ready to run the program

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

Nice, it seems you are ready to train your model now.

Ok, then you just have to `cd` to the root of the repository, and run:

```shell
python train_reco.py
```

The prompt will tell you things like:

```
Preparing data...
Training for Pepito, Paolo          # Check if this is ok
Pepito is number 0                  # This is just a mapper for the test_reco.py
[ INFO:0] Initialize OpenCL runtime...   # You just don't care about it
Paolo is number 1
Data prepared
Total faces:  35                    # Here, it will tell you how many faces and label the program found
Total labels:  35
```

#### Train your model - Best Practices

The thing is, Haar is not Google's top neural networks, hence you need to help him to do his work.

1. Balance the number of pictures over people to reduce over/under fitting.
  Assume Pépito has 30 pictures to train on, and Paolo only 5, you can be sure the model will say everyone is Pépito.

2. Crop your pictures to avoid loosing training examples
  If the prompt prints this `Impossible to find Paolo`, it means that on a picture, he wasn't able to recognise anyone. Meaning you just lost a training example.




# Down there, everything is false yet

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Mickaël Labarrère** - [mlabarrere](https://github.com/mlabarrere)

See also the list of [contributors](https://github.com/mlabarrere/webcam-recognition/graphs/contributors) who participated in this project.

## License

This project is licensed under the Apache 2 License - see the [LICENSE.md](https://github.com/mlabarrere/webcam-recognition/LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
