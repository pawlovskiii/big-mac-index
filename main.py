from src.extract_data_from_api import extract_data_from_api
from src.send_mail import post_mail


def main():
    extract_data_from_api()
    post_mail()


if __name__ == "__main__":
    main()
