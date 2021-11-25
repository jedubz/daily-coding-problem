

def add_two_numbers_in_list(arr, k):

   for i in arr:
       n = k-i
       if (n in arr):
           return [i, n]

result = add_two_numbers_in_list([10, 15, 3, 7], 17)

print(result)