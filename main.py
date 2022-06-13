from configparser import ConfigParser
from src.extract_data_from_api import extract_data_from_api
from src.send_mail import post_mail


config = ConfigParser()
config.read("config.ini")


def main():
    extract_data_from_api(config)
    post_mail(config)


if __name__ == "__main__":
    main()
