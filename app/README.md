## Pitch.
Pitch It is a web application that is meant for users to add pitches on 7 different categories
September 20th, 2019
By Hulian Juba.
## Description.
The Pitch It web application is meant for users to post pitches on any of the 7 different categories. These categories are:

1. Interview Pitch
2. Product Pitch
3. Promotion Pitch
4. Business
5. Academic
6. Political
7. Technology
8. Health
#### Users can select any of the categories from the navbar to view the pitches on these categories.

Other users can give feedback on the pitch posts by commenting, liking or not liking the pitch.

## Specifications.
Get the specs here

## Set-up and Installation
. Prerequiites
-Python 3.6
-Ubuntu software
Clone the Repository.
Run the following command on the terminal: git clone 
Install Postgress

## Create a Virtual Environment:
Run the following commands in the same terminal: sudo apt-get install python3.6-venv python3.6 -m venv virtual source virtual/bin/activate

Install dependancies
Install dependancies that will create an environment for the app to run pip3 install -r requirements

Prepare environment variables
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/pitchit'
export SECRET_KEY='Your secret key'
Run Database Migrations
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
Running the app in development
In the same terminal type: python3 manage.py server

Open the browser on https://pitchapplet.herokuapp.com/

Known bugs
SQLAlchemy errors, automatic sign out has a short time span

Technologies used
-Python 3.6
-HTML
-Bootstrap 4
-JavaScript
-Heroku
-Postgresql
Support and contact details
Contact me on developer.hulian.ashraf703@yahoo.com for any comments, reviews or advice.

License MTN 2019.
Copyright (c) .Hulian Juba.