input1 = [1, 2, 3, 4, 5]
expected1 = [120, 60, 40, 30, 24]

input2 = [3, 2, 1]
expected2 = [2, 3, 6]

def recurs(newInput):
    if newInput:
        n = newInput.pop()
        return n * recurs(newInput)
    else:
        return 1

def product(input):
    result = []
    for i in range(len(input)):
        iInput = list(input)
        iInput.pop(i)
        val = recurs(iInput)
        result.append(val)
    return result

actual1 = product(input1)
actual2 = product(input2)
print(actual1 == expected1)
print(actual2 == expected2)    