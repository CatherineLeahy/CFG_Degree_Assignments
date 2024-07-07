# Assignment 4 - APIs :globe_with_meridians:

## Introduction :rocket:
The goal of this assignment was to design and implement an API. I chose to create a scheduling assistant app for equipment in the laboratory I currently work in. 

## Corrosion Laboratory Scheduling Assistant :calendar:
### Background :test_tube:
The Corrosion Laboratory has a number of large environmental chamber's that are used to investigate how various metals,
alloys and coatings corrode in different environments. The chambers have a few key features that are relevant to the app:
- each chamber is a different unique colour
- chambers can accommodate either an acidic or neutral environment
- chambers are calibrated annually
- only one project can be ran in a chamber at any given time
- projects can run for any specified duration

### App Features :bulb:
The technicians that run the chambers require a platform to aid with scheduling projects in the lab. This scheduling 
assistant app enables them to perform three main functions:
1. ***View all chamber specifications*** - technicians can check calibration due dates and chamber environment capabilities
2. ***View the schedule of a specific chamber*** - technicians can search by chamber ID to view the schedule of a specific chamber
3. ***Add new project to the schedule*** - technicians can input a new project's requirements (duration, environment) and be provided with a list of suitable chambers and the soonest available date the project can start.

## Installation :gear:
To run the app, first start MySQL and create the database with provided tables and dummy data by running the create_db.sql file.

If you don't already have Flask installed on your machine, set up a virtual environment and install using the below command in your terminal:
```
python3 -m venv .venv
. .venv/bin/activate
pip install Flask
```

Next, start the server by updating the config.py file with your hostname, username and password before running the app.py file in PyCharm

Now you're ready to use the app, simply run the main.py file and explore the features detailed above!

