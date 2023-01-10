
# Q7. Write a function that takes a list of numbers and returns the sum of the numbers that are
# divisible by 3 or 5. The function should use a generator expression to accomplish this.


# Input: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: 33

# Input: [0, 15, 30, 45, 60, 75, 90, 105]
# Output: 330

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list1 = [0, 15, 30, 45, 60, 75, 90, 105]


def sum_of_num(lst):
    return sum([i for i in lst if (i % 3 == 0 or i % 5 == 0)])


print(sum_of_num(list1))

