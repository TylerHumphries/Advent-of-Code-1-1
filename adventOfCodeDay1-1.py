#advent of code day 1 puzzle

#Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.
#An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.
#The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.
#to what floor do the instructions take santa?

def map(directions):
    steps = int(len(directions))
    floor = 0
    for i in range(0, steps):
        if directions[i] == '(':
            floor = floor + 1
        elif directions [i] == ')':
            floor = floor - 1

    return floor

print('please input the puzzle')
puzzle = input()
print(map(puzzle))
