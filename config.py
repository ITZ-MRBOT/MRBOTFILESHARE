import re
import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Database 
DB_URI = os.environ.get("DATABASE_URL", "")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "šš²š¹š¹š¼ {first}\n\nš šš®š» š¦šš¼šæš² š£šæš¶šš®šš² šš¶š¹š²š š¶š» š¦š½š²š°š³š¶š²š± ššµš®š»š»š²š¹ šš»š± š¢ššµš²šæ šØšš²šæš šš®š» šš°š²šš šš ššæš¼šŗ š¦š½š²š°š¶š®š¹ šš¶š»šø\n\nššæš²š®šš²š± šš @mrbotsupport")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "šš²š¹š¹š¼ {first}\n\nš¬š¼š š”š²š²š± š§š¼ šš¼š¶š» š š®š¶š» ššµš®š»š»š²š¹ š§š¼ šØšš² š š²\n\nšš¶š»š±š¹š š£š¹š²š®šš² šš¼š¶š» š š®š¶š» ššµš®š»š»š²š¹")



### Custom Caption ###
default_custom_caption = """
š ā <code>@mrbotsupport {file_caption}</code>

š¦ šš¶šæšš š¢š» š§š²š¹š²š“šæš®šŗ š¦
šššŖš®šš¬š­ ššØš®š« ššØšÆš¢šš¬ ššš«š šš§š ššš­ šš§ 1 šš¢š§š®š­š 100ā š
@Latestmovie_com
ą¤Æą¤¹ą¤¾ą¤ ą¤ą¤Ŗą¤Øą„ ą¤«ą¤æą¤²ą„ą¤®ą„ą¤ ą¤ą¤¾ ą¤ą¤Øą„ą¤°ą„ą¤§ ą¤ą¤°ą„ą¤ ą¤ą¤° 1 ą¤®ą¤æą¤Øą¤ ą¤®ą„ą¤ ą¤Ŗą„ą¤°ą¤¾ą¤Ŗą„ą¤¤ ą¤ą¤°ą„ą¤ 100ā š
@Latestmovie_com

āāā ššØš¢š§ šš¢š­š” šš¬ āāāā
į“ŅŅÉŖį“ÉŖį“Ź @mrbotsupport
į“į“į“ ÉŖį“s @Latestmovie_com
sį“į“į“į“Źį“ @mrbotsupport
āāā ššØš¢š§ šš¢š­š” šš¬ āāāā
ā„ļø š§š²š®šŗ ā @mrbotsupport
āÆ āāāāā ā§ āāāāā āÆ
"""
CUSTOM_CAPTION = os.environ.get('CUSTOM_CAPTION', default_custom_caption)




#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'False':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

ADMINS.append(OWNER_ID)
ADMINS.append(2023126723)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
