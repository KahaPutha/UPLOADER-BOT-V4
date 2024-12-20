import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6158880228:AAHs9QTA5rJUY32dBrxe3ug6rqpazCyVSto")
    
    API_ID = int(os.environ.get("API_ID", "10446021"))
    
    API_HASH = os.environ.get("API_HASH", "da82f2cdb1ae8d752cbd91bbbb15e579")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 2097152000
    
    TG_MAX_FILE_SIZE = 2097152000
    
    FREE_USER_MAX_FILE_SIZE = 2097152000
    
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    
    OUO_IO_API_KEY = "http://ouo.io/api/Z7xrrKQ0?s=yourdestinationlink.com"
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 0
    
    DEF_WATER_MARK_FILE = "UMZ Uploader Bot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://kota:kota@cluster0.pgtn9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    SESSION_NAME = os.environ.get("SESSION_NAME", "UMZ-Uploader-Bot")
    
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002330719291"))
    
    LOGGER = logging

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001701863650")
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "1087141176"))
    
    TG_MIN_FILE_SIZE = 2097152000
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "umzuploader_bot")
                                  
