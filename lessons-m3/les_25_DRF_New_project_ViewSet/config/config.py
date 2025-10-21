from dotenv import load_dotenv
import os


load_dotenv()


MAIL_HOST = os.getenv("EMAIL_HOST")
MAIL_PORT = os.getenv("EMAIL_PORT")
MAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
MAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")