lst = [10,20,"Wacky",-10,35.5]
print(lst)
print(lst[1])
print(lst[:3])
print(lst*4)
print(len(lst))

lst.append(29)
lst.remove('Wacky')
del(lst[1])
print(lst)

print(max(lst))
print(min(lst))
lst.insert(3, 183)
print(lst)

lst.sort(reverse=True)
print(lst)