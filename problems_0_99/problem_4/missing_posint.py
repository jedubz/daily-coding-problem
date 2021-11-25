testcase1 = [3, 4, -1, 1]
testcase2 = [1, 2, 0]
testcase3 = [3, 5, 6]

expected1 = 2
expected2 = 3
expected3 = 1


def find_missing_pos_int(arr):
    lowest_pos_int = 1
    for i in arr:
        if (int_is_pos(i)):
            if (i < lowest_pos_int+1):
                lowest_pos_int = lowest_pos_int+1

    return lowest_pos_int


def int_is_pos(number):
    return number > 0


actual1 = find_missing_pos_int(testcase1)
actual2 = find_missing_pos_int(testcase2)
actual3 = find_missing_pos_int(testcase3)

print("Actual1: " + str(actual1))
print("Actual2: " + str(actual2))
print("Actual3: " + str(actual3))

assert actual1 == expected1
print("Passed")
assert actual2 == expected2
print("Passed")
assert actual3 == expected3
print("Passed")
