# Lab Simulator

This lab simulator is a python flask application that simulate endpoint infection for SecureX Demonstrations.

This is actually a tiny web server that listen on http port 4000.

## Installation

Create a working directory into your laptop. Open a terminal window into it.

### Create a Python virtual environment

For Linux/Mac 

	python3 -m venv venv
	source bin activate

For Windows 
	
We assume that you already have installed git-bash.  If so open a git-bash console and type the 2 following commands :

	python -m venv venv 
	venv/Scripts/activate

### clone the scripts

	git https://github.com/pcardotatgit/lab_simulator-001.git
	cd lab_simulator-001
	
### install needed modules

The scripts need the following python modules

- requests
- flask
- crayons
	
you can install them with the following  :
	
	python -m pip install --upgrade pip
	pip install -r requirements.txt

## Start the simulator

	python app.py


