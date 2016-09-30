#advent of code day 1 puzzle

#Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
#An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
#The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.
#to what floor do the instructions take santa?

def findFloor(directions):
    floor = 0
    for char in directions:
        if char = '(':
            delta = 1
        else:
            delta = -1
        floor + delta

    return floor

print('please input the puzzle')
puzzle = input()
print(findFloor(puzzle))

