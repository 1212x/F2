from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import asyncio

# Initialize your bot client
Bot = Client(
    "my_filestore_bot",
    api_id="24025974",
    api_hash="2abf0406f41a57b540bdefe8b12d114f",
    bot_token="6750686423:AAFRAvDyvig_d_zcXmBkUGhWOrSRYwflrcQ"
)

# Define the handler function for the /pifchannel command
@Bot.on_message(filters.command('pifchannel') & filters.private)
async def PIFchannels(client, message: Message):
    keyboard = [
        [InlineKeyboardButton("🍁 ʜᴅ ᴛᴇʟᴜɢᴜ ᴍᴏᴠɪᴇs 🎖️", url="https://t.me/+wIa9vb3tRho3N2Q1")],
        [InlineKeyboardButton("🧞‍♀️ ʜɪɴᴅɪ - ᴍᴀʟᴀʏᴀʟᴀᴍ 🧐", url="https://t.me/+97U9EyGMz_s2YzQ1"),
         InlineKeyboardButton("🔔 ᴛᴀᴍɪʟ - ᴋᴀɴɴᴀᴅᴀ 🤖", url="https://t.me/+a3-YTIF0zsFhMDc1")],
        [InlineKeyboardButton("🔥 ʜᴏʟʟʏᴡᴏᴏᴅ - ᴅᴜʙʙᴇᴅ 🎉", url="https://t.me/+9Ks800pBuq9kMmNl"),
         InlineKeyboardButton("🙂 ᴡᴇʙ - sᴇʀɪᴇs ✨", url="https://t.me/+YcesJaZ8gwUyMTc1")],
        [InlineKeyboardButton("🥵 ʀᴀʀᴇ ʜɪᴅᴅᴇɴ ᴍᴏᴠɪᴇꜱ ♥️", url="https://t.me/PIFRareHiddenMovies")],
        [InlineKeyboardButton("☀️ ᴅᴠᴅ - ᴅᴀᴛᴀʙᴀsᴇ 🌚", url="https://t.me/PIFOficials"),
         InlineKeyboardButton("🌿 ʜᴅ - ᴅᴀᴛᴀʙᴀsᴇ 💧", url="https://t.me/PIFOficial")],
        [InlineKeyboardButton("🔗 ʙᴏᴛᴢ ᴀʀᴇᴀ ⚙", url="https://t.me/BoTzUpdates0"),
         InlineKeyboardButton("🥵 ᴏɴʟʏ ᴀᴅᴜʟᴛꜱ 🙈", url="https://t.me/Pakkinte_Anty_Bitlu")],
        [InlineKeyboardButton("⪦ ᴍᴏᴠɪᴇs ʀᴇǫᴜᴇsᴛ ɢʀᴏᴜᴘ ⪧", url="https://t.me/+37-TDCcQqltlOTRl")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    sent_message = await message.reply_text(
        text="""**__🙂 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴍʏ ᴘᴀɴɪɴᴅɪᴀғɪʟᴍᴢ ᴄᴏᴍᴍᴜɴɪᴛʏ!! ᴄʜᴇᴀᴋ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs & ɢʀᴏᴜᴘs ʟɪsᴛ ʙᴇʟᴏᴡ!!__**

**__      ʜᴇ'ʟʟᴏ .. ɪ ᴀᴍ ᴘᴀɴɪɴᴅɪᴀғɪʟᴍᴢ ᴀᴅᴍɪɴ 🤨__**

**__✨  ᴅᴇᴀʟs 𝟸𝟺/𝟽 :- 
@KillerLootDeals __** 

**__✨ ʀᴀʀᴇ ʜɪᴅᴅᴇɴ ᴀᴅᴜʟᴛ ᴍᴏᴠɪᴇs 𝟸.𝟶 
@Telugu_Adults_Rare_Hidden_Movies __**

**__ᴛᴀʀɢᴇᴛ - ʀᴇᴀᴄʜɪɴɢ ᴜʀ sᴇʟғ 🎯__**

**__ғᴏʀ ᴀɴʏ ǫᴜᴇʀɪᴇs - @PIFAdminBot __**

**__ @PanindiaFilmZ 🔥**__""",
        reply_markup=reply_markup
    )

    await asyncio.sleep(10)
    await sent_message.delete()
    await message.delete()

# Start the bot
Bot.run()
