from Yumeko import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import CallbackContext, run_async, CommandHandler

PHOTO = "https://telegra.ph/file/f9b0895ae78578fda9202.jpg"

@run_async
def void(update: Update, context: CallbackContext):

    TEXT = f"Welcome to **[【V๏ɪ፝֟𝔡】 ✧Network✧](https://t.me/voidxnetwork)** \n\n◈ Void is an anime based Community with a motive to spread love and peace around telegram. Go through the channel and join the Community if it draws your attention. ◈"

    update.effective_message.reply_photo(
        PHOTO, caption= TEXT,
        parse_mode=ParseMode.MARKDOWN,

            reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(text="【Usertag】", url="https://t.me/void_network/103"),
                InlineKeyboardButton(text="【Owner Sama】", url="https://t.me/voidxtoxic")
                ],
                [InlineKeyboardButton(text="【V๏ɪ፝֟𝔡】Network", url="https://t.me/voidxnetwork")]
            ]
        ),
    )


void_handler = CommandHandler("void", void)
dispatcher.add_handler(void_handler)

__help__ = """
 ──「Void Network」──                         
 
❂ /void: Get information about our community! using it in groups may create promotion so we don't support using it in groups."""
   
__mod_name__ = "【ᴠᴏɪᴅ】"
