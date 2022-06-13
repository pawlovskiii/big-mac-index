from configparser import ConfigParser
from src.extract_data_from_api import extract_data_from_api
from src.send_mail import post_mail


def main() -> None:
    config = ConfigParser()
    config.read("config.ini")

    API_KEY = config["DEFAULT"]["api_key"]
    PATH = config["DEFAULT"]["path"]
    MAIL = config["DEFAULT"]["mail"]

    extract_data_from_api(API_KEY, PATH)
    post_mail(MAIL)


if __name__ == "__main__":
    main()
