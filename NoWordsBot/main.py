import telepot
import time

import chess
import chess.uci


boards = {} # dict for keep boards: {user_id:board}


def get_reply(msg, user_id):
    if msg[0] == "/":
        if len(msg) >= 4:
            command = msg[1:]
            if command[0: == "start":
                boards[user_id] = chess.Board()
            elif command[0:3] == "move":
                if 


def handle(msg):
    print(type(msg))
    content_type, chat_type, chat_id = telepot.glance(msg)
    user_id = msg[u'chat'][u'id']
    user_name = msg[u'chat'][u'first_name']

    print(content_type, chat_type, chat_id) 
    if content_type == 'text':
        text = msg[u'text']
        
        TelegramBot.sendMessage(user_id, get_reply(msg, user_id))
        print("Accepted message from user with id: ", user_id)
        print("Message: ", text)


chessEngine = chess.uci.popen_engine("/home/user/stockfish-7-linux/Linux/stockfish_7_x64")
chessEngine.uci()


token = sys.argv[sys.argc-1]
TelegramBot = telepot.Bot(token)
print TelegramBot.getMe()

TelegramBot.message_loop(handle)
   


try:
    while True:
        pass
except KeyboardInterrupt:
    print("\nAuf wieder sehen!")
