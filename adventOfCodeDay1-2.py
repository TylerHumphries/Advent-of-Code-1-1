#advent of code day 1 puzzle part 2

#this time we need to find what position of the character that causes santa to go to floor -1

def findPosition(directions):
    floor = 0
    position = 0
    for char in directions:
        if char == '(':
            delta = 1
        else:
            delta = -1
        floor = floor + delta
        position = position + 1
        if floor == -1:
            break

    return position

print('please input the puzzle')
puzzle = input()
print(findPosition(puzzle))
