dict1={1:"John",2:"Bob",3:"Bill"}
print(dict1)

print(dict1.items())

k=dict1.keys()

for key in k:
    print(key)

v=dict1.values()

for value in v:
    print(value)

print(dict1[3])

del dict1[2]

print(dict1)