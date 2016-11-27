# -*- coding: utf-8 -*-

# This is helloworld telegram bot example
# 

import sys
import telepot

def handle(msg):
    user_id = msg[u'chat'][u'id']
    TelegramBot.sendMessage(user_id, "Hello world!")

def main(token):
    bot = telepot.Bot(token)
    print TelegramBot.getMe()
    bot.message_loop(handle)
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nGood bye!")






if __name__ == "__main_":
    if sys.argc != 2:
        print("You should pass token as cl parameter")
        exit()

    main(token)
