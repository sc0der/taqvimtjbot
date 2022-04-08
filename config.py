from os import environ as env
from dotenv import load_dotenv
load_dotenv()
TOKEN = env.get('TAQVIM_BOT_TOKEN')
