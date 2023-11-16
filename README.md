# Lab Simulator ( v_20230930 )

This lab simulator is a python flask application that simulate endpoint infection for Cisco XDR ( or SecureX) Demos.

This is actually a tiny web server that listen on http port 4000. This one is supposed to be installed into your laptop.

The simulator exposes a Web GUI that is a network diagram you can interact with. The simulator manages interaction with your Cisco XDR tenant as well.

![](assets/img/0.png)

The web GUI simulates an endpoint infection which creates incidents and sightings into your Cisco XDR Tenant. Exactly like what happen with real infections.

We simulate an infection but we create a real Cisco XDR Incident. And we do this this way because we don't want to use real attacks or malwares.

## Installation

A Pre requisit before moving forward on the lab simulator installation is to have a python interpreter installed and running into your laptop.

If you are not sure of this, then open a terminal console and type the following command :

	python -V

The result of this command is the version of your installed python interpreter. This version must be at least 3.7. 

If you don't have any python interpreter then you have to install one.

If your laptop is a windows machine the install **Python for Windows** package. This one install everything you need ( and don't forget to click on the [ add python to path] checkbox in the installer GUI ). Python 3.7 was the version used for creating this app. And it will work with 3.11 with no problems.

If your python interpreter is correctly working, then you are good to go to next steps.

Next step ...

### Step 1. Create a working directory

Create a working directory into your laptop. Open a terminal CMD window into it. Name It **PVT_Lab** for example.

### Step 2. Copy the code into your laptop

**The Download ZIP Method**

The most easy way for anyone not familiar with git is to copy the **ZIP** package available for you in this page. Click on the **Code** button on the top right of this page. And then click on **Download ZIP**. 

Unzip the zip file into your working directory.

**The "git clone" method with git client**

And here under for those of you who are familiar with Github.

You must have a git client installed into your laptop. Then you can type the following command from a terminal console opened into your working directory.

	git clone https://github.com/pcardotatgit/lab_simulator-001.git

### Step 3. Go to the code subfolder

Once the code unzipped into your laptop, then Go to the **code** subfolder.

	cd lab_simulator-001-main\code
    
### Step 4a. Quick Start only for Windows Users

This section is only for windows users. In order to make installation steps easier some batch files had been prepared for you.  You just have to run them one after the other.
    
You must have a CMD console openned into your code folder :

    c:\path_to_working_directory\working_directory\lab_simulator-001-main\code
    
Then type one after the other the batch files

    install1
    install2
    install3
    install4

And then you can start the simulator by typing the letter **b** and **Enter**:

You should see the application starting. 

All depencies are installed then. Later when you will run again the simulator you will just have to type first the letter **a** + **Enter**, letter **b** + **Enter**

### Step 4b. If you don't go to the Quick Start Method, then go to the step by step installation method here under

### step by step installation : 1 Create a Python virtual environment

It is still a best practice to create a python virtual environment. Thank to this you will create a dedicated package with requested modules for this application.

**Create a virtual environment on Windows**

	python -m venv venv 
    

**Create a virtual environment on Linux or Mac**

	python3 -m venv venv

    Depending on the python version you installed into your Mac you might have to type either 

    - python -m venv venv

    or maybe

    - python3 -m venv venv    : python3 for python version 3.x  

    or maybe 

    - python3.9 -m venv venv  : if you use the 3.9 python version

And then type :

**Activate the virtual environment on Windows**

	venv\Scripts\activate
    
**Activate the virtual environment on Linux or Mac**

	source venv/bin/activate    

### step by step installation : 2 Install needed python modules

You can install them with the following 2 commands one after the other ( Windows / Mac / Linux ):
	
	python -m pip install --upgrade pip

Then install required python modules

	pip install -r requirements.txt

### step by step installation : 3 Start the simulator

Just run the flask application as a python script ( Windows / Mac / Linux ) :

	python app.py

For windows ( only ) users you can type :

	b  This is a bat file which start the simulator

At this point you should see the flask application starting into the console and then your browser must open on the Lab Portal page.

This web server listens to port 4000. At anytime you can open the index page at **http[://]localhost:4000**.


![](assets/img/1.png)

![](assets/img/2.png)

You can **stop the flask application** by typing Ctrl+C into the application console.

### Navigate into the network

Instructions for SecureX / Cisco XDR interaction are given into the [Detect, Alert and Block Threat Use Case](https://github.com/pcardotatgit/SecureX_Workflows_and_Stuffs/tree/master/100-SecureX_automation_lab) lab.

If you click into the hacker icon, then you will see a CMD console opens.

You can type anything into the edit field.

## Start the simulator when python package and modules are already installed :

Open a CMD console into the code folder and type :

Type the letter **a** to start the python virtual environment

And then the letter **b** to start the simulator  

Ready to go !