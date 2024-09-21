def grow(arr):
    grow = 1
    for value in arr:
        grow *= value
    return grow


product = grow([1, 2, 3, 4])
print(product)
