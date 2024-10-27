def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i)  # Remove the element from the array
            array.append(i)  # Append the element to the end
    return array


print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros([0, 0]))
print(move_zeros([0]))
print(move_zeros([]))
