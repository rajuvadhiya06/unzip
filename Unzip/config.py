import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    API_ID = int(os.environ.get("API_ID", "14662552")
    API_HASH = os.environ.get("API_HASH", "cd56687a177fe2355e64c91659facf3e")
    MAX_FILE_SIZE = 2194304000
    
    
