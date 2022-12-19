# Lab Simulator

This lab simulator is a python flask application that simulate endpoint infection for SecureX Demonstrations.

This is actually a tiny web server that listen on http port 4000. This one is supposed to be installer into your laptop.

The simulator exposes a Web GUI that is a network diagram we can interact with. The simulator manages interaction with your SecureX tenant as well.

![](assets/img/0.png)

This GUI simulates an endpoint infection which create incidents and sightings into your SecureX Tenant. Exactly like what happen with real infections. The same alerts are created within SecureX.

The goal is to showcase endpoint infection safely without doing it with real attacks and malwares.

## Installation

A Pre requesit before moving forward on the lab simulator installation is to have a python interpreter installed and running into your laptop.

If you are not sure of this, then open a terminal console and type the following command :

	python -V

We expect to have back the version of your installed python version. This version must be at least 3.7. And we expect no error telling you for example that python was not found as an external application.

If you have an error here. Then you must install python into your laptop and add python files folder into your OS path.

If your python interpreter is correctly working, then you are good to go to next steps.

Next step ...

Create a working directory into your laptop. Open a terminal window into it. Name It **PVT_Lab** for example.

### Copy the code into your laptop

The most easy way for anyone not familiar with git is to copy the **ZIP** package available for you in this page. Click on the **Code** button on the top right of this page. And then click on **Download ZIP**. 

Unzip the zip file into your working directory.

And here under for those of you who are familiar with Github.

You must have a git client installed into your laptop. Then you can type the following command from a terminal console opened into your working directory.

	git clone https://github.com/pcardotatgit/lab_simulator-001.git

Once the code unzipped into your laptop, then Go to the **code** subfolder.

	cd lab_simulator-001-main\code
	
### Create a Python virtual environment

It is still a best practice to create a python virtual environment. Thank to this you will create a dedicated package with requested modules for this application.

For Linux/Mac 

	python3 -m venv venv
	source /bin/activate

For Windows 

	python -m venv venv 
	venv\Scripts\activate

### Install needed modules

you can install them with the following 2 commands one after the other :
	
	python -m pip install --upgrade pip

	pip install -r requirements.txt

### Start the simulator

	python app.py

At this point you should see the flask application starting into the console and then your browser must open on the Lab Portal page.
