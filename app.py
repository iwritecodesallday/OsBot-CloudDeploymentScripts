import os
import configparser
from Classes.DB import DB
import win32gui
import time

# Read important values from the configuration file config.ini
config = configparser.ConfigParser()
config.read("config.ini")
path_to_executable = config['osbot']['path']

DB = DB(config)

account = DB.check_for_available_accounts()

# Put all Account configurations into a dictionary object
command_line_config = {
    "login": config['osbot']['username'],
    "password": config['osbot']['password'],
    "proxy": account[3],
    "bot_id": account[0],
    "bot_login": account[1],
    "bot_password": account[2],
    "script": "Cloudbot:None"
}

try:

    #  Change this to whatever you need to execute, In my case I'm using OSBot
    os.system("java -jar {} -login {}:{} -debug 5005 -proxy {} -bot {}:{}:0000 -script {}".format(
        path_to_executable, 
        command_line_config['login'], 
        command_line_config['password'],
        command_line_config['proxy'],
        command_line_config['bot_login'],
        command_line_config['bot_password'],
        command_line_config['script']
        ))
except:
    print(Exception)