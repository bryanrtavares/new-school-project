#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1664850827
    OWNER = config("OWNER")
    ffmpegcode = ["-preset faster -c:v libx265 -crf 30 -vf scale=-4:480 -c:a libopus -b:a 32k"]
    THUMBNAIL = config("THUMBNAIL", default="https://telegra.ph/file/cd8c82f28c79b8dcd341e.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
