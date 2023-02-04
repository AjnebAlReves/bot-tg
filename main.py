import configparser, json
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import (
    Client, 
    filters
)

# Main Class
class LimitatiBot_app(Client):

    config = configparser.ConfigParser()
    config.read('config.ini')

    app = Client(
        "main",
        api_id = config['Credentials']['API_ID'],
        api_hash = config['Credentials']['API_HASH'],
        bot_token = config['Credentials']['TOKEN'],
        plugins=dict(root=f"LimitatiBot"),
        sleep_threshold=180
    )

    ADMIN = [881096405, 1947847356]
    ALIAS = config['Variables']['ALIAS']
    CMDB = ["start", "bc", "broadcast", "help"]
    prefixes = config['Variables']['ALIAS']

    lang = json.load(open(f"LimitatiBot/lang/" + config['Language']['LANGUAGE'] + ".json", encoding = 'utf-8'))

    if __name__ == "__main__":
        app.run()
        