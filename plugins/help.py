from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"""Just Send Youtube Url And Select A Quality
For Download (it can download both audio & video Format)
    
Queries [rizadッ🕊](https://telegram.me/riz4d)"""
    await message.reply_text(helptxt)
