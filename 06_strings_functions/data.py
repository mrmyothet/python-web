name = "technortal"
result = name.count('t')
print("no of occurrences - ", result)

name = "good bad bad this product is bad,"
result = name.endswith(",")
print("is ends with ',' : ", result)

result = name.index('b')
print(result)

name = '   Kyaw Kyaw   345  '
result = name.strip()
print(":", result, ":")