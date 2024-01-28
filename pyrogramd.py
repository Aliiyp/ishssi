from pyrogram import Client, filters

bot_token = "6986030644:AAEOtcKtaw_z2WPPPv2mN_8emzC5j3W1RyU"

api_id = 22127557
api_hash = "348f141a89ba55603d4c9360de9c5625"
app = Client("nb", api_id, api_hash, bot_token=bot_token)


app.start()


@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text(f"Hello")


app.run()

