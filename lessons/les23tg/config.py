import os
from dotenv import load_dotenv

load_dotenv()

TOKEN_TG = os.getenv('TOKEN_TG')
TOKEN_OPENAI = os.getenv('TOKEN_OPENAI')