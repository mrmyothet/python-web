t1 = [("k1", 1), ("k2", 2), ("k3", 3)]

d1 = dict(t1)
print(type(d1))
print(d1)

person_info = {"name": "Myo Thet", "age": 38, "nationality": "Myanmar", "weight": 60.2}

# items
for item in person_info.items():
    print(type(item))
    print(item)

# values
for value in person_info.values():
    print(type(value))
    print(value)

# keys
for key in person_info.keys():
    print(type(key))
    print(key)

# pop
result = person_info.pop("weight")
print(result)
print(person_info)

# popitem
result = person_info.popitem()
print(result)
print(person_info)

# copy
mt_info = person_info.copy()
print(mt_info)

# clear
mt_info.clear()
print(mt_info)
print(person_info)

# get
result = person_info.get("name")
print(result)

# adding new items
person_info["weight"] = 60.2
print(person_info)
