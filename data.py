from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ğ¥ Start Generating Session ğ¥", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="Return Home", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("Bot Status And More Bots", url="https://t.me/+hbc28odEPwU4MDk9")],
        [
            InlineKeyboardButton("How to Use", callback_data="help"),
            InlineKeyboardButton("About", callback_data="about")
        ],
        [InlineKeyboardButton("Bots Channel", url="https://t.me/MaximXBots")],
    ]

    START = """
Hey Bro {}

Welcome To IğÏÉ±i åæ³ {} 

If You Don't Trust This Bot ğ, 
â¶ Stop Reading This Message ğ«
â· Delete This Chat Bro ğï¸

ğ«µ Still Reading!? 
You Can Use Me To Generate Pyrogram New V2 And Telethon String Session. Use Below Buttons To Learn More !

ğ§âğ» By @MaximXRobot 
    """

    HELP = """
â ğğ¯ğğ¢ğ¥ğğğ¥ğ ğğ¨ğ¦ğ¦ğğ§ğğ¬
â£ /about - About The Bot ğ¤
â£ /help - This Message ğï¸
â£ /start - Start the Bot ğ´
â£ /generate - Generate Session âï¸
â£ /cancel - Cancel The process ğ«
â /restart - Cancel The process ğ
"""

    ABOUT = """
**About This Bot** 

Telegram Bot To Generate Pyrogram And Telethon String Session By @MaximXRobot

â ğğğ±ğ¢ğ¦ ğ ğğ¨ğ­ğ¬
â£ âï¸ Source Code : [Click Here](https://t.me/+vBu5aXlocTkwNGM1)
â£ ğ¥ Framework : [Pyrogram](https://docs.pyrogram.org)
â ğ£ï¸ Language : [Python](https://www.python.org)

â ğ§âğ» ğğğ¯ğğ¥ğ¨ğ©ğğ« ââ
â @MaximXRobot
    """
