from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

def post_mail():
    print(config['DEFAULT']['mail'])
