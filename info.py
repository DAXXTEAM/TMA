import re
from os import environ
from os import getenv

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# ----------------ʜᴇʀᴇ-ᴄᴏɴғɪɢ------------------#

API_ID = int(environ['API_ID', "24509589"])
API_HASH = environ['API_HASH', "717cf21d94c4934bcbe1eaa1ad86ae75"]
BOT_TOKEN = environ['BOT_TOKEN', "6576720076:AAHqQcXsyuFs9ITDCaD2SBgJX940xGrHRLE"]
OWNER_IDS = list(map(int, getenv("OWNER_IDS", "6691393517").split()))
PREMIUM_IDS = list(map(int, getenv("PREMIUM_IDS", "6691393517").split()))

# ----------------ᴄᴏɴғɪɢ-ᴇɴᴅ------------------#
