# Tic-Tac-Toe
# Naomi González 

def main():
    player = next_player("") 
    xo = board()
    while not (winner(xo) or draw(xo)):
        design(xo)
        make_move(player, xo)
        player = next_player(player)
    design(xo)
    print("Good game. Thanks for playing!") 

def board():
    xo = []
    for square in range(9):
        xo.append(square + 1)
    return xo

def design(xo):
    print(f"{xo[0]}|{xo[1]}|{xo[2]}")
    print("-+-+-")
    print(f"{xo[3]}|{xo[4]}|{xo[5]}")
    print("-+-+-")
    print(f"{xo[6]}|{xo[7]}|{xo[8]}")
    
def draw(xo):
    for square in range(9):
        if xo[square] == "x" and xo[square] == "o":
            return True
    return False 
    
def winner(xo):
  return (xo[0] == xo[1] == xo[2] or
          xo[3] == xo[4] == xo[5] or
          xo[6] == xo[7] == xo[8] or
          xo[0] == xo[3] == xo[6] or
          xo[1] == xo[4] == xo[7] or
          xo[2] == xo[5] == xo[8] or
          xo[0] == xo[4] == xo[8] or
          xo[2] == xo[4] == xo[6])

def make_move(player, xo):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    xo[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

if __name__ == "__main__":
    main()