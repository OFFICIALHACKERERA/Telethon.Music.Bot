import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "15260804"))
    API_HASH = os.environ.get("API_HASH", "e5ff231de8c0ee33fa7830e766df5b10")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5332418768:AAFObHqPv72dyAG6vdnSPDX5ylclXSuXdpE")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKsBuzRlVHX2kqehclC58cV6aizURdaxHlLk5xdMZ-b2Ewk7nU-7b8qVBrp1txA0fjhNH1bxpG0qluYVy4RWxHARHXeKbRKPG0pnGC2CBJQUIJDx4ya_dv2PK93bZIw4J-qT1ZxtoxTOBUygc-lrEJx9f9M74wTgUxUn-HUSUKXxzIEkSMaVYZR-M86R7plpcMkyomw1JuHCXCtf_3waAxLUdBd3TxVBP5Tj7RXmib32T-IzU8o-jGJg32kS-b6Mo1nqgPOPvszRZPhgJg4H5rtdPAMVr-zknjDTsmHs9ToS6aHFI34VycQe6kx6aT1v4IBFVXTAK0Wr1fDc-tHevJyaFko=")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "LOVE_PRO_VIKAS_OP_bot")
    SUPPORT = os.environ.get("SUPPORT", "LOVE_IS_LIFE_OP")
    CHANNEL = os.environ.get("CHANNEL", "OFFICIALHACKER789")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3b2725c0e95f759e3b444.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/3b2725c0e95f759e3b444.jpg")
