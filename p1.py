def sum_list(numbers):
    sum = 1
    for x in numbers:
        sum *= x
    return sum
print(sum_list([1,2,3]))