from pystyle import *
import requests
import random
import string
import time
from termcolor import cprint


image = """
                                            .         .                                            
8 888888888o.      8 8888888888            ,8.       ,8.           ,o888888o.     b.             8 
8 8888    `^888.   8 8888                 ,888.     ,888.       . 8888     `88.   888o.          8 
8 8888        `88. 8 8888                .`8888.   .`8888.     ,8 8888       `8b  Y88888o.       8 
8 8888         `88 8 8888               ,8.`8888. ,8.`8888.    88 8888        `8b .`Y888888o.    8 
8 8888          88 8 888888888888      ,8'8.`8888,8^8.`8888.   88 8888         88 8o. `Y888888o. 8 
8 8888          88 8 8888             ,8' `8.`8888' `8.`8888.  88 8888         88 8`Y8o. `Y88888o8 
8 8888         ,88 8 8888            ,8'   `8.`88'   `8.`8888. 88 8888        ,8P 8   `Y8o. `Y8888 
8 8888        ,88' 8 8888           ,8'     `8.`'     `8.`8888.`8 8888       ,8P  8      `Y8o. `Y8 
8 8888    ,o88P'   8 8888          ,8'       `8        `8.`8888.` 8888     ,88'   8         `Y8o.` 
8 888888888P'      8 888888888888 ,8'         `         `8.`8888.  `8888888P'     8            `Yo 


Made by scooby#0001                                                                      Dont skid.

            ─═══════════════════════════════════☆☆═══════════════════════════════════─
                             Demon Nirto Gen || The fastest's nirto gen
                                    (Press enter to run.)               
            ─═══════════════════════════════════☆☆═══════════════════════════════════─

"""


count = 0

Anime.Fade(Center.Center(image), Colors.purple_to_blue, Colorate.Vertical, interval=0.75, enter=True)

print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter(image)))

def webhookpost():
    post = {
    "content": '',
    "embeds": [
     {
          "title": "Nirto Gen , Logging in...",
          "description": f"**Dev's : **\nscooby#0001 , \n#8k.HITTAS\nhttps://discord.gg/2u8Gv3T4w4\n\nUser's webhook :\n```fix\n{webhook}\n```",
      "color": 15656164,
          "footer": {
        "text": "#8k.HITTAS | shi was made by scooby"
          },
          "thumbnail": {
            "url": "https://media.discordapp.net/attachments/818895366740115466/1006291408375795773/gif44.gif"
          }
        }
      ],
      "username": "Angel",
      "avatar_url": "https://media.discordapp.net/attachments/818904599448125540/980250171336171600/IMG_3993.jpg",
      "attachments": []
    }
    requests.post(webhook, json=post)

def post():
    post = {
  "content": null,
  "embeds": [
    {
      "title": "Found a vaild Nirto Code !",
      "description": "Gift code below >\n```fix\n{vcode}\n```\n**Dev's : **\nscooby#0001 , \n#8k.HITTAS\nhttps://discord.gg/2u8Gv3T4w4",
      "color": 15656164,
      "footer": {
        "text": "#8k.HITTAS | shi was made by scooby"
      },
      "thumbnail": {
        "url": "https://media.discordapp.net/attachments/818895366740115466/1006291408375795773/gif44.gif"
      }
    }
  ],
  "username": "Angel",
  "avatar_url": "https://media.discordapp.net/attachments/818904599448125540/980250171336171600/IMG_3993.jpg",
  "attachments": []
    }
    requests.post(webhook, json=input)
print("[", end="")
cprint(" Demon ", "red", end="")
print("] ", end="")
cprint(" Enter Your Webhook below:", 'red')
webhook = input('>')
webhookpost()
print("[", end="")
cprint(" Demon ", "red", end="")
print("] ", end="")
cprint(" Enter how many codes you want to check", 'red')
num = int(input('>'))


with open("gen.txt", "w", encoding='utf-8') as file:
    print("[", end="")
    cprint(" Demon ", "red", end="")
    print("] ", end="")
    cprint("Please wait as the codes are being generated, High number = More time", 'red')

    start = time.time()

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k = 16
        ))

        file.write(f"https://discord.gift/{code}\n")

    print("[", end="")
    cprint(" Demon ", "red", end="")
    print("] ", end="")
    cprint(" Enter how many codes you want to check", 'red')

with open("gen.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            count += 1 
            cprint(f" Valid | {nitro} ( {count} / {num} )", 'green')
            vcode = nirto
            post()
            break
        else:
            count += 1 
            cprint(f" Invalid | {nitro} ( {count} / {num} )", 'red')