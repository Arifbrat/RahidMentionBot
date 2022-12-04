import os


class Config():
    # Get these values from my.telegram.org
    # https://my.telegram.org
    API_ID = int(os.environ.get("API_ID", "18482353"))
    API_HASH = os.environ.get("API_HASH", "9f7840b7015b359a49e142ce42decd71")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5717330127:AAG6alkGkC-nTOBEYLCO3a60Eg4Iw9lKGkM")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "SecreTTaggerBot")
    BOT_NAME = os.environ.get("BOT_NAME", "SECRET TAGGER 🇦🇿")
    BOT_ID = int(os.environ.get("BOT_ID", "5717330127"))
    SUDO_USERS = os.environ.get("SUDO_USERS", "5531642054").split()
    SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "bossbotsazhelp")
    OWNER_ID = int(os.environ.get("OWNER_ID", "5531642054"))
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "@B9SSD7")
