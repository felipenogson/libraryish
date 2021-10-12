import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
	SECRET_KEY = os.getenv('SECRET_KEY') or 'never never never gonna guess it'