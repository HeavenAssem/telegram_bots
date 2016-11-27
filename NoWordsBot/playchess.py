import chess
import chess.uci

engine = chess.uci.popen_engine("/home/user/stockfish-7-linux/Linux/stockfish_7_x64")

engine.uci()

board = chess.Board()

side = raw_input("Choose your side(black/white):")

if side == "white":
  side = True
elif side == "black":
  side = False
else:
  print("Wrong side - go away")

repr_board = str(board)
print(repr_board)

print(board)

try:
  while True:
    if board.turn == side:
      move = raw_input("Your move:")
      try:
        board.push_uci(move)
      except ValueError:
        print("Illegal move! Try once more\n")
    else:
      engine.position(board)
      move = engine.go(movetime=2000)
      board.push_uci(str(move[0]))
    print("================\n")
    print(board)      
    
except KeyboardInterrupt:
  engine.quit()
  print("Good Bye!")
