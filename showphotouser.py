import requests

chat_id = "6755634224 "
urlp = "https://t.me/elhyba"
url = f"https://api.telegram.org/botتوكن بوتك/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
