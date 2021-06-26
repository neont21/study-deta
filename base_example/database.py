from deta import Deta
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)
PROJECT_KEY = os.getenv('PROJECT_KEY')
PROJECT_ID = os.getenv('PROJECT_ID')
BASE_NAME = os.getenv('BASE_NAME')

deta = Deta(PROJECT_KEY)
db = deta.Base(BASE_NAME)
db_url = f'https://database.deta.sh/v1/{PROJECT_ID}/{BASE_NAME}'
