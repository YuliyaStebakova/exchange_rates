a = [4,6,'py','tell',78]
b = [44,'hello',56,'exept',['world',5.7],3,6]
d = a + b
print(d)
a.extend(b)
print(a)
a.insert(3,6)
print(a.count(6))
print(len(a))
print(b[4][0])
#c = b[4][0]
#print(c)
print(a)