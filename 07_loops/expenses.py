expenses = [20, 32, 34, 43, 56, 67, 23]

total_expense = 0

for daily_expense in expenses:
    total_expense += daily_expense

print(total_expense)

# built-in function - sum
total_expense = sum(expenses)
print(total_expense)


def add(container):
    result = 0
    for item in container:
        result += item

    return result


total_expense = add(expenses)
print(total_expense)
