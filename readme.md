# Instructions
Install python 3.7.7

Create a virtual environment 
py -m venv env
- note: A new folder will be created called env if you're successful.

Activate your python environment
env\Scripts\activate
- note: you will see (env) on your cli if you're successful

Install Dependencies 
(env) python -m pip install -r requirements.txt
- Note: if you use more, store them here. get a list by type python -m pip freeze

Create a postgresql database and Create 2 tables, osrs and Activity

In osrs, create these columns:
id (serial), email (varchar 255), password (varchar 255), avilable (boolean), proxy (varchar 255), character (varchar)

in Activity, create these columns:
id (serial), account_id (int), activity (varchar 255), location (varchar 255)

The python script will begin by connecting to the database specified in the config file, and will query an avilable account in the database.

There is also a script inside of the DB Class where you can update the status of your bot. Look into DB.py to understand more
