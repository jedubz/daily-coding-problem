def add_two_numbers_in_list(arr, k):

    for i in arr:
        n = k-i
        if (n in arr):
            return True
    return False


test_case_1_arg0 = [10, 15, 3, 7]
test_case_1_arg1 = 17

expected = True

actual = add_two_numbers_in_list(test_case_1_arg0, test_case_1_arg1)

assert actual == expected
print("Passed")
