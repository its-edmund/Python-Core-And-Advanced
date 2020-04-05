# String Type
s="  You are awesome  "
print(s)

# Multiple Lines

s1="""This String has
multiple lines that run
for at least 3 lines."""
print(s1)

# Indexing

print(s[0])

# Repetition

print(s*2)

# Length

print(len(s))
print(len(s1))

# Slicing

print(s[0:5])
print(s[:])
print(s[:8])
print(s[-3:-1])

print(s[0:9:2])
print(s[15:-1])
print(s[::-1])

# Stripping Whitespace

print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Finding

print(s.find("awe",0,8))
print(s.count("a"))
print(s.replace("awesome", "super"))

# Case manipulation

print(s.upper())
print(s.lower())
print(s.title())