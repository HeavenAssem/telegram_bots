#!/usr/bin/python
# -*- coding: utf-8 -*-

# This is helloworld telegram bot example
# 

import sys
import telepot

def main(token):
    def handle(msg):
        user_id = msg[u'chat'][u'id']
        bot.sendMessage(user_id, "Hello world!")

    bot = telepot.Bot(token)
    print bot.getMe()
    bot.message_loop(handle)
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nGood bye!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You should pass token as cl parameter")
        exit()

    main(sys.argv[1])
