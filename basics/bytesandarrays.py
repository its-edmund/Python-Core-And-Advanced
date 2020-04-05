lst=[20,30,24,244]
print(type(lst))
b=bytes(lst)
print(type(b))

# Will produce error, cannot modify bytes

# b[3]=2

b1=bytearray(lst)
print(type(b1))
b1[2]=13