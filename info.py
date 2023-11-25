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

API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
OWNER_IDS = list(map(int, getenv("OWNER_IDS", "6691393517").split()))
PREMIUM_IDS = list(map(int, getenv("PREMIUM_IDS", "6691393517").split()))

# ----------------ᴄᴏɴғɪɢ-ᴇɴᴅ------------------#
