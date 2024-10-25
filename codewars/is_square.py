def is_square(n):
    if n < 0:
        return False  # fix me

    if n == 0:
        return True

    half_num = int(n / 2) + 1
    for i in range(1, half_num):
        if i * i == n:
            return True

    return False


print(is_square(25))
