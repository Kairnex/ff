import re
import os
from os import getenv

from Script import script

id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    try:
        val = value.lower()
    except AttributeError:
        return default
    if val in ["true", "yes", "1", "enable", "y"]:
        return True
    elif val in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION     = os.environ.get('SESSION', 'Media_search')
API_ID      = int(os.environ.get('API_ID', '9696783'))
API_HASH    = os.environ.get('API_HASH', '3e74a9830493e9261410a947428dbb34')
BOT_TOKEN   = os.environ.get('BOT_TOKEN', "7770072777:AAHcXrIxHfBjKVvlKs1x7-r5qeBjBGDO5r4")

# Bot settings
CACHE_TIME         = int(os.environ.get('CACHE_TIME', '300'))
USE_CAPTION_FILTER = is_enabled(os.environ.get('USE_CAPTION_FILTER', 'True'), True)

PICS         = os.environ.get('PICS', 'https://files.catbox.moe/q9a07c.jpg').split()
NOR_IMG      = os.environ.get('NOR_IMG', "https://files.catbox.moe/q9a07c.jpg")
MELCOW_VID   = os.environ.get('MELCOW_VID', "https://files.catbox.moe/q9a07c.jpg")
SPELL_IMG    = os.environ.get('SPELL_IMG', "https://files.catbox.moe/q9a07c.jpg")
SUBSCRIPTION = os.environ.get('SUBSCRIPTION', 'https://files.catbox.moe/q9a07c.jpg')
CODE         = os.environ.get('CODE', 'https://files.catbox.moe/q9a07c.jpg')

# Stream link shortener (you can now safely ignore these if unused)
STREAM_SITE = os.environ.get('STREAM_SITE', '')
STREAM_API  = os.environ.get('STREAM_API', '')
STREAMHTO   = os.environ.get('STREAMHTO', '')

# Admins, Channels & Users
ADMINS        = [int(x) if id_pattern.search(x) else x for x in os.environ.get('ADMINS', '').split()]
CHANNELS      = [int(x) if id_pattern.search(x) else x for x in os.environ.get('CHANNELS', '').split()]
auth_users    = [int(x) if id_pattern.search(x) else x for x in os.environ.get('AUTH_USERS', '').split()]
AUTH_USERS    = auth_users + ADMINS if auth_users else []
PREMIUM_USER  = [int(x) if id_pattern.search(x) else x for x in os.environ.get('PREMIUM_USER', '').split()]

auth_channel  = os.environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL  = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
auth_grp      = os.environ.get('AUTH_GROUP', '')
AUTH_GROUPS   = [int(x) for x in auth_grp.split()] if auth_grp else []

support_chat_id = os.environ.get('SUPPORT_CHAT_ID', '')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

reqst_channel = os.environ.get('REQST_CHANNEL_ID', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None

NO_RESULTS_MSG = is_enabled(os.environ.get("NO_RESULTS_MSG", "False"), False)

# MongoDB information
DATABASE_URI    = os.environ.get('DATABASE_URI', "mongodb+srv://codexkairnex:gm6xSxXfRkusMIug@cluster0.bplk1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME   = os.environ.get('DATABASE_NAME', "mbot")
COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Telegram_files')

# Verification
VERIFY      = is_enabled(os.environ.get('VERIFY', 'False'), False)
HOWTOVERIFY = os.environ.get('HOWTOVERIFY', 'https://t.me/kairnex')

# Miscellaneous
DELETE_CHANNELS = [int(x) if id_pattern.search(x) else x for x in os.environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN        = int(os.environ.get("MAX_B_TN", '5'))
MAX_BTN         = is_enabled(os.environ.get('MAX_BTN', "True"), True)
PORT            = os.environ.get("PORT", "8080")
GRP_LNK         = os.environ.get('GRP_LNK', 'https://t.me/kairnex')
CHNL_LNK        = os.environ.get('CHNL_LNK', 'https://t.me/kairnex')
TUTORIAL        = os.environ.get('TUTORIAL', 'https://t.me/kairnex')
IS_TUTORIAL     = is_enabled(os.environ.get('IS_TUTORIAL', 'True'), True)
MSG_ALRT        = os.environ.get('MSG_ALRT', 'ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : ᴋᴀɪʀɴᴇx')
LOG_CHANNEL     = int(os.environ.get('LOG_CHANNEL', '-1002083345153'))
SUPPORT_CHAT    = os.environ.get('SUPPORT_CHAT', 'https://t.me/kairnex')

P_TTI_SHOW_OFF     = is_enabled(os.environ.get('P_TTI_SHOW_OFF', "False"), False)
IMDB               = is_enabled(os.environ.get('IMDB', "False"), False)
AUTO_FFILTER       = is_enabled(os.environ.get('AUTO_FFILTER', "True"), True)
AUTO_DELETE        = is_enabled(os.environ.get('AUTO_DELETE', "True"), True)
SINGLE_BUTTON      = is_enabled(os.environ.get('SINGLE_BUTTON', "True"), True)
CUSTOM_FILE_CAPTION= os.environ.get("CUSTOM_FILE_CAPTION", script.CAPTION)
BATCH_FILE_CAPTION = os.environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE      = os.environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE_TXT)
LONG_IMDB_DESCRIPTION = is_enabled(os.environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY     = is_enabled(os.environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM          = int(os.environ.get("MAX_LIST_ELM", 0)) if os.environ.get("MAX_LIST_ELM") else None
INDEX_REQ_CHANNEL     = int(os.environ.get('INDEX_REQ_CHANNEL', str(LOG_CHANNEL)))
FILE_STORE_CHANNEL    = [int(x) for x in os.environ.get('FILE_STORE_CHANNEL', '').split() if x]
MELCOW_NEW_USERS      = is_enabled(os.environ.get('MELCOW_NEW_USERS', "True"), True)
PROTECT_CONTENT       = is_enabled(os.environ.get('PROTECT_CONTENT', "True"), True)
PUBLIC_FILE_STORE     = is_enabled(os.environ.get('PUBLIC_FILE_STORE', "True"), True)

LANGUAGES = ["malayalam", "", "tamil", "", "english", "", "hindi", "", "telugu", "", "kannada", "", "gujarati", "", "marathi", "", "punjabi", ""]
SEASONS   = [f"season {i}" for i in range(1, 11)]
QUALITIES = ["360P", "", "480P", "", "720P", "", "1080P", "", "1440P", "", "2160P", ""]

# Online stream & download
NO_PORT     = is_enabled(os.environ.get('NO_PORT', 'False'), False)
ON_HEROKU   = 'DYNO' in os.environ
APP_NAME    = os.environ.get('APP_NAME') if ON_HEROKU else None
BIND_ADDRESS= getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0')

# Build FQDN & URL
if not ON_HEROKU or getenv('FQDN'):
    FQDN = getenv('FQDN', BIND_ADDRESS)
else:
    FQDN = f"{APP_NAME}.herokuapp.com"

if ON_HEROKU or NO_PORT:
    URL = f"https://{FQDN}/"
else:
    URL = f"https://{FQDN}:{PORT}/"

SLEEP_THRESHOLD = int(os.environ.get('SLEEP_THRESHOLD', '60'))
WORKERS         = int(os.environ.get('WORKERS', '4'))
SESSION_NAME    = os.environ.get('SESSION_NAME', 'Kairnexbot')
MULTI_CLIENT    = False
name            = os.environ.get('name', 'kairnex')
PING_INTERVAL   = int(getenv("PING_INTERVAL", "1200"))
HAS_SSL         = is_enabled(getenv('HAS_SSL', 'True'), True)

if HAS_SSL:
    URL = f"https://{FQDN}/"
else:
    URL = f"http://{FQDN}/"

PREMIUM_LOGS = int(os.environ.get('PREMIUM_LOGS', '-1002083345153'))

# Final log string
LOG_STR  = "Current Customized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled; the bot will show IMDB details for your queries.\n" if IMDB else "IMDB Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF is enabled; users will be redirected to send /start to the bot's PM instead of sending files directly.\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled; files will be sent in PM without redirection.\n")
LOG_STR += ("SINGLE_BUTTON is enabled; filename and file size will be shown in a single button.\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled; filename and file size will be shown as separate buttons.\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION is enabled with value: {CUSTOM_FILE_CAPTION}\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION found; default captions will be used.\n")
LOG_STR += ("Long IMDB storyline is enabled.\n" if LONG_IMDB_DESCRIPTION else "Long IMDB storyline is disabled.\n")
LOG_STR += ("Spell Check mode is enabled; the bot will suggest related movies if none are found.\n" if SPELL_CHECK_REPLY else "Spell Check mode is disabled.\n")
LOG_STR += (f"MAX_LIST_ELM is set; lists will be shortened to the first {MAX_LIST_ELM} elements.\n" if MAX_LIST_ELM else "Full cast and crew lists will be shown; set MAX_LIST_ELM to limit.\n")
LOG_STR += f"Your current IMDB template is: {IMDB_TEMPLATE}\n"
