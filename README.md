# Webcam Recognition
A tool for detecting people

[![CodeFactor](https://www.codefactor.io/repository/github/mlabarrere/webcam_recognition/badge)](https://www.codefactor.io/repository/github/mlabarrere/webcam_recognition)  [![BCH compliance](https://bettercodehub.com/edge/badge/mlabarrere/Webcam_recognition?branch=master)](https://bettercodehub.com/)

Made with ❤ by Micky

## Download

To get source code, run:
```
https://github.com/mlabarrere/Webcam_recognition.git
```

Vous pouvez suivre le mini tutoriel Git du projet dans Sources/Tutoriels/Tuto_Git.md ( A faire)



## Project Structure

```
Webcam Recognition
│   README.md (A faire)
│   requirements.txt (A faire)
│   setup.py (A faire)
│   LICENSE    
│
└───backend
│   │   __init__.py (A vérifier si nécéssaire et faire)
│   │   README.md (A faire)
│   │   Switch.py (A faire proprement)
│   │
│   └───Modules
│       │   __init__.py (A faire proprement)
│       │   wrapper.py
│       │   module_actu.py
│       │   module_Date_Heure.py
│       │   module_listecourse.py
│       │   module_marmiton.py
│       │   module_meteo.py
│       │   module_wikipedia.py
│       │   module_YouTube.py
│       │   vocal_synthesis.py
│       │
│       └───Rires
│           │   [Fichiers de rires creepy mp3]
│
└───frontend
│   │   README.md (A faire)
│   │	main.py
│   │ 
│   │
│   └───templates
│   │   │   courses.html
│   │   │   meteo.html
│   │   │   news.html
│   │
│   └───static
│	    └───css
│	    │   │   style.css
│	    │
│	    └───img
│	    │   │   [Beaucoup de trucs]
│	    │
│	    └───js
│	    │   │   prefixfree.min.js
│	    │   │   voice_reactor.js
│	    │   │   voice-recognition.js
│	    │
│	    └───polices
│	        │   CaviarDreams.ttf
│	        │   CaviarDreams_Bold.ttf
│	        │   CaviarDreams_BoldItalic.ttf
│	        │   CaviarDreams_Italic.ttf
│	        │   RedVelvet.ttf
│
└───data
│   │   liste_courses.txt
│      
└───test
│   │   README.md (A faire)
│   └───benchmarks
│   │   │   README.md (A faire)
│   │
│   └───integration
│   │   │   README.md (A faire)
│   │
│   └───unit
│       │   README.md (A faire)
│       │   Date_Heure.ipynb
│       │   listecourse_test_U.ipynb
│       │   marmiton_test_U.ipynb
│       │   wiki_Test_U.ipynb
│       │   YouTube_Test_U.ipynb
│
└───tools
    │   README.md (A faire)
     Note : [c'est là ou je stock les codes pas encore utiles]

```



### Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

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

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc
