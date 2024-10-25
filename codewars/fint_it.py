def find_it(seq):

    result = {}

    for item in seq:
        if item in result.keys():
            result[item] = result[item] + 1
        else:
            result[item] = 1
    # return result

    for item in result.keys():
        if result[item] % 2 != 0:
            return item


print(find_it([1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]))
