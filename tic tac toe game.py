Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def ConstBoard(board):  # this function will display the current state of the board
...     print("Current state of the board: \n\n")
...     for i in range(9):
...         if (i > 0) and (i % 3 == 0):
...             print("\n")
...         if (board[i] == 0):
...             print("_", end=" ")  # _ _ _
...         elif (board[i] == -1):  # _ _ _
...             print("X", end=" ")  # _ _ _
...         elif (board[i] == 1):
...             print("O", end=" ")
...     print("\n\n")
... 
... 
... def User1Turn(board):
...     pos = int(input("Enter X's position from [1, 2, 3, ..., 9]: "))  # as User1 is human not an AI, he will start the counting from 1
...     if (board[pos-1] != 0):  # to make it readable for computer we will use pos-1
...         print("Wrong Move")
...         exit(0)  # we cannot use the break statement here because it will only end the if statement not the entire code
...     board[pos-1] = -1  # as the user1 will only be able to put its move at the position which is empty
... 
... 
... def User2Turn(board):
...     pos = int(input("Enter O's position from [1, 2, 3, ..., 9]: "))
...     if board[pos-1] != 0:
...         print("Wrong Move")
...         exit(0)
...     board[pos-1] = 1
... 
... 
... def minmax(board, player):
...     x = analyzeboard(board)
...     if x != 0:
...         return x * player
...     pos = -1
...     value = -2
...     for i in range(9):
...         if board[i] == 0:
...             board[i] = player
...             score = -minmax(board, player * -1)  # - minmax is used because if the comp. also wins then also it will represent that user has won to do the reverse of it
            board[i] = 0
            if score > value:
                value = score
                pos = i
    if pos == -1:
        return 0
    return value


def ComTurn(board):
    pos = -1
    value = -2  # it is the lowest value that does not exist as -1, 1, 0
    for i in range(9):
        if board[i] == 0:  # the comp can only put its O only when the board is empty
            board[i] = 1  # now calculating if comp put its O over pos 1 what will be the score using min max algo.
            score = -minmax(board, -1)
            board[i] = 0
            if score > value:  # if score>value then
                value = score  # update the value with the new score then the best chance of winning is
                pos = i  # at the i
    board[pos] = 1


def analyzeboard(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for i in range(8):
        if board[cb[i][0]] != 0 and board[cb[i][0]] == board[cb[i][1]] and board[cb[i][0]] == board[cb[i][2]]:
            return board[cb[i][0]]

    return 0


def main():
    choice = int(input("Enter 1 for single player, 2 for multiplayer: "))
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # numeric representation of board
    if choice == 1:
        print("Computer: O vs You: X")
        player = int(input("Enter to play 1 (st) or 2 (nd): "))
        for i in range(9):  # we use this for loop to check whether someone has won or not 9 times
            if analyzeboard(board) != 0:
                break
            if (i + player) % 2 == 0:  # if player has pressed 1 to play with AI
                ComTurn(board)
            else:
                ConstBoard(board)
                User1Turn(board)

    else:
        for i in range(9):
            if analyzeboard(board) != 0:
                break
            if i % 2 == 0:  # if player has pressed 2 and wants to play multiplayer in this formula player doesn't need
                User1Turn(board)
            else:
                ConstBoard(board)
                User2Turn(board)

    x = analyzeboard(board)
    if x == 0:  # game is draw as there will be no empty block left
        ConstBoard(board)
        print("Draw")
    elif x == -1:
        ConstBoard(board)
        print("Player X Wins!!!! O looses!")
    elif x == 1:
        ConstBoard(board)
        print("Player O Wins!!!! X looses!")


if _name_ == "_main_":
