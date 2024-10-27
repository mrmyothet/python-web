def binary_array_to_number(arr):
    number = 0
    length = len(arr)
    index = 1
    for item in arr:
        power = length - index
        if item == 1:
            number += 2**power
        index += 1
    return number


print(binary_array_to_number([0, 0, 0, 1]))
print(binary_array_to_number([0, 0, 1, 0]))
print(binary_array_to_number([1, 1, 1, 1]))
print(binary_array_to_number([0, 1, 1, 0]))
