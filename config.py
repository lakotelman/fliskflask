import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__name__))

load_dotenv(os.path.join(basedir, ".env"))


class Config:
    FLASKAPP = os.getenv("FLASK_APP")
    FLASKENV = os.getenv("FLASK_ENV")
