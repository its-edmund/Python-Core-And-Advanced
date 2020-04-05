tpl=(40,50,40,"xyz")
print(type(tpl))
print(tpl[3])
print(tpl*3)
print(tpl.count(40))
print(tpl.index("xyz"))

lst=[45,24,"Stinky"]
print(type(lst))
tpl1=tuple(lst)
print(type(tpl1))