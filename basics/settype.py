s={42,23,23.2,"Wow!",23,23,13}
print(s)
print(type(s))

s.update([88,99])
print(s)

# Will produce error, cannot index a set

# print(s[1])
# print(s[0:5])
# print(s*5)

s.remove(23)
print(s)

f=frozenset(s)

# Will produce error, frozenset cannot be modified

# f.update(13)
# f.remove(42)