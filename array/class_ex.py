#!/usr/bin/python3

move_zeroes = [1, 0, 1, 2, 0, 1, 3]
print(move_zeroes)

def move(move_zeroes):
    for i in range(len(move_zeroes)):
        if move_zeroes[i] == 0:
            move_zeroes.remove(move_zeroes[i])
            move_zeroes.append(0)
    return move_zeroes

print(move(move_zeroes))

def option_2(move_zeroes):
    """
    Move all zeroes
    """
    i = 0
    for i in range(len(move_zeroes)):
        for j in range(len(move_zeroes)):
            if move_zeroes[i] == 0:
                temp = move_zeroes[i]
                move_zeroes[i] = move_zeroes[i+1]
                move_zeroes[i+1] = temp
    return move_zeroes
print(option_2(move_zeroes))