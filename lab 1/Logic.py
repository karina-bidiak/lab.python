print(3.1)
a = True
b = False
c = False
print(a or b)
print(a and b)
print(b or c)

print(3.2)
x = False
y = True
z = False
print(x and z)
print(x and y)
print(x and z)

print(3.3)
a = True
b = False
c = False
print(not a and b)
print(a and not b)
print(a and b or c)

print(3.4)
x = True
y = True
z = False
print(not x and y)
print(x or not y)
print(x or y and z)

print(3.5)
a = True
b = False
c = False
print(a or b and not c)
print(not a and not b)
print(not (a and c) or b)
print(a and not b or c)
print(a and (not b or c))
print(a or (not (b and c)))

print(3.6)
x = False
y = False
z = True
print(x or y and not z)
print(not x and not y)
print(not (x and z) or y)
print(x and not y or z)
print(x or (not y or z))
print(x or(not(y and z)))

print(3.7)
a = True
b = False
c = False
print(a or not(a and b) or c)
print(not a or a and (b or c))
print((a or b and not c) and c)

print(3.8)
x = False
y = True
z = False
print(x and not(z or y) or not z)
print(not x or x and (y and z))
print((x or y and not z) and z)

print(3.9)
x = True
y = False
z = False
print(not x or not y or not z)
print((not x or not y) and (x or y))
print(x and y or x and z or not z)

print ("3.10")
a = False
b = False
c = True
print((not a or not b) and not c)
print((not a or not b) and (a or b))
print(a and b or a and c or not c)

print("3.11")
x = 1
y = -1
print((x**2 + y**2 <= 4))
x = 1
y = 2
print((x >= 0) or (y**2 != 4))
x = 1
y = 2
print((x >= 0) and (y**2 != 4))
x = 2
y = 1
print((x * y != 0) and (y > x))
x = 2
y = 1
print((x * y <0) or (y < x))
x = 2
y = 1
print((not(x * y <0)) and (y > x))
x = 1
y = 2
print((not(x * y < 0)) or (y > x))

print("3.12")
x = 1
y = -1
print(x**2 - y**2 <= 0)
x = 2
y = -2
print((x >= 2) or (y**2 != 4))
x = 2
y = 2
print((x >= 0) and (y**2 > 4))
x = 1
y = 2
print((x * y != 4) and (y > x))
x = 2
y = 1
print((x * y != 0) or (y < x))
x = 1
y = 2
print((not(x * y < 1)) and (y > x))
x = 2
y = 1
print((not(x * y < 0)) or (y > x))

print("3.13")
a = True
b = False
print(not(a and b))
print(not a or b)
print(a or not b)
a = False
b = True
print(not(a and b))
print(not a or b)
print(a or not b)
a = False
b = False
print(not(a and b))
print(not a or b)
print(a or not b)
a = True
b = True
print(not(a and b))
print(not a or b)
print(a or not b)

print("3.14")
x = True
y = False
print(not(x or y))
print(not x and y)
print(x and not y)
x = False
y = True
print(not(x or y))
print(not x and y)
print(x and not y)
x = True
y = True
print(not(x or y))
print(not x and y)
print(x and not y)
x = False
y = False
print(not(x or y))
print(not x and y)
print(x and not y)

print("3.15")
a = True
b = False
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)
a = False
b = True
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)
a = True
b = True
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)
a = False
b = False
print(not a or not b)
print(a and (a or not b))
print((not a or b) and b)

print("3.16")
x = True
y = False
print(not x and not y)
print(x or(not x and y))
print((not x and y) or y)
x = False
y = True
print(not x and not y)
print(x or(not x and y))
print((not x and y) or y)
x = True
y = True
print(not x and not y)
print(x or(not x and y))
print((not x and y) or y)
x = False
y = False
print(not x and not y)
print(x or(not x and y))
print((not x and y) or y)

print("3.17")
a = True
b = False
print(not a and not b or a)
print(b or not a and not b)
print(b and not(a and not b))
a = False
b = True
print(not a and not b or a)
print(b or not a and not b)
print(b and not(a and not b))
a = True
b = True
print(not a and not b or a)
print(b or not a and not b)
print(b and not(a and not b))
a = False
b = False
print(not a and not b or a)
print(b or not a and not b)
print(b and not(a and not b))

print("3.18")
x = True
y = False
print(not(x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)
x = False
y = True
print(not(x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)
x = True
y = True
print(not(x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)
x = False
y = False
print(not(x and not y) or x)
print(y and not x or not y)
print(not y and not x or y)

print("3.19")
a = True
b = False
print(not (not a and not b) and a)
print(not(not a or not b) or a)
print(not(not a or not b) and b)
a = False
b = True
print(not (not a and not b) and a)
print(not(not a or not b) or a)
print(not(not a or not b) and b)
a = True
y = True
print(not (not a and not b) and a)
print(not(not a or not b) or a)
print(not(not a or not b) and b)
a = False
y = False
print(not (not a and not b) and a)
print(not(not a or not b) or a)
print(not(not a or not b) and b)

print("3.20")
x = True
y = False
print(not(not x or y) or not x)
print(not(not x and not y) and x)
print(not(x or not y) or not y)
x = False
y = True
print(not(not x or y) or not x)
print(not(not x and not y) and x)
print(not(x or not y) or not y)
x = True
y = True
print(not(not x or y) or not x)
print(not(not x and not y) and x)
print(not(x or not y) or not y)
x = False
y = False
print(not(not x or y) or not x)
print(not(not x and not y) and x)
print(not(x or not y) or not y)

print("3.21")
a = True
b = True
c = True
print(not(a or not b and c))
print(a and not (b and not c))
print(not(not a or b and c))
a = False
b = False
c = False
print(not(a or not b and c))
print(a and not (b and not c))
print(not(not a or b and c))
a = True
b = False
c = False
print(not(a or not b and c))
print(a and not (b and not c))
print(not(not a or b and c))
a = False
b = True
c = False
print(not(a or not b and c))
print(a and not (b and not c))
print(not(not a or b and c))
a = False
b = False
c = True
print(not(a or not b and c))
print(a and not (b and not c))
print(not(not a or b and c))
a = False
b = True
c = True
print(not(a or not b and c))
print(a and not (b and not c))
print(not(not a or b and c))
a = True
b = False
c = True
print(not(a or not b and c))
print(a and not (b and not c))
print(not(not a or b and c))
a = True
b = True
c = False
print(not(a or not b and c))
print(a and not (b and not c))
print(not(not a or b and c))

print("3.22")
x = True
y = True
z = True
print(not(x or not y and z))
print(y or (x and not y or z))
print(not(not x and y or z))
x = False
y = False
z = False
print(not(x or not y and z))
print(y or (x and not y or z))
print(not(not x and y or z))
x = True
y = False
z = False
print(not(x or not y and z))
print(y or (x and not y or z))
print(not(not x and y or z))
x = False
y = True
z = False
print(not(x or not y and z))
print(y or (x and not y or z))
print(not(not x and y or z))
x = False
y = False
z = True
print(not(x or not y and z))
print(y or (x and not y or z))
print(not(not x and y or z))
x = False
y = True
z = True
print(not(x or not y and z))
print(y or (x and not y or z))
print(not(not x and y or z))
x = True
y = False
z = True
print(not(x or not y and z))
print(y or (x and not y or z))
print(not(not x and y or z))
a = True
b = True
c = False
print(not(x or not y and z))
print(y or (x and not y or z))
print(not(not x and y or z))

print("3.23")
a = True
b = True
c = True
print(not (a or not b and c) or c)
print(not (a and not b or c) and b )
print(not (not a or b and c) or a)

a = False
b = False
c = False
print(not (a or not b and c) or c)
print(not (a and not b or c) and b )
print(not (not a or b and c) or a)
a = True
b = False
c = False
print(not (a or not b and c) or c)
print(not (a and not b or c) and b )
print(not (not a or b and c) or a)
a = False
b = True
c = False
print(not (a or not b and c) or c)
print(not (a and not b or c) and b )
print(not (not a or b and c) or a)
a = False
b = False
c = True
print(not (a or not b and c) or c)
print(not (a and not b or c) and b )
print(not (not a or b and c) or a)
a = False
b = True
c = True
print(not (a or not b and c) or c)
print(not (a and not b or c) and b )
print(not (not a or b and c) or a)
a = True
b = False
c = True
print(not (a or not b and c) or c)
print(not (a and not b or c) and b )
print(not (not a or b and c) or a)
a = True
b = True
c = False
print(not (a or not b and c) or c)
print(not (a and not b or c) and b)
print(not (not a or b and c) or a)

print("3.24")
x = True
y = True
z = True
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not(x or y and z) or not x)
x = False
y = False
z = False
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not(x or y and z) or not x)
x = True
y = False
z = False
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not(x or y and z) or not x)
x = False
y = True
z = False
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not(x or y and z) or not x)
x = False
y = False
z = True
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not(x or y and z) or not x)
x = False
y = True
z = True
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not(x or y and z) or not x)
x = True
y = False
z = True
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not(x or y and z) or not x)
x = True
y = True
z = False
print(not(y or not x and z) or z)
print(x and not (not y or z) or y)
print(not(x or y and z) or not x)

print("3.25")
a = True
b = True
c = True
print(not (a and b) and (not a or not c))
print(not(a and not b) or(a or not c))
print(a and not b or not(a or not c))
a = False
b = False
c = False
print(not (a and b) and (not a or not c))
print(not(a and not b) or(a or not c))
print(a and not b or not(a or not c))
a = True
b = False
c = False
print(not (a and b) and (not a or not c))
print(not(a and not b) or(a or not c))
print(a and not b or not(a or not c))
a = False
b = True
c = False
print(not (a and b) and (not a or not c))
print(not(a and not b) or(a or not c))
print(a and not b or not(a or not c))
a = False
b = False
c = True
print(not (a and b) and (not a or not c))
print(not(a and not b) or(a or not c))
print(a and not b or not(a or not c))
a = False
b = True
c = True
print(not (a and b) and (not a or not c))
print(not(a and not b) or(a or not c))
print(a and not b or not(a or not c))
a = True
b = False
c = True
print(not (a and b) and (not a or not c))
print(not(a and not b) or(a or not c))
print(a and not b or not(a or not c))
a = True
b = True
c = False
print(not (a and b) and (not a or not c))
print(not(a and not b) or(a or not c))
print(a and not b or not(a or not c))

print("3.26")
x = True
y = True
z = True
print(not(x or y) and (not x or not z))
print(not(not x and y) or (x and not z))
print(x or not y and not(x or not z))
x = False
y = False
z = False
print(not(x or y) and (not x or not z))
print(not(not x and y) or (x and not z))
print(x or not y and not(x or not z))
x = True
y = False
z = False
print(not(x or y) and (not x or not z))
print(not(not x and y) or (x and not z))
print(x or not y and not(x or not z))
x = False
y = True
z = False
print(not(x or y) and (not x or not z))
print(not(not x and y) or (x and not z))
print(x or not y and not(x or not z))
x = False
y = False
z = True
print(not(x or y) and (not x or not z))
print(not(not x and y) or (x and not z))
print(x or not y and not(x or not z))
x = False
y = True
z = True
print(not(x or y) and (not x or not z))
print(not(not x and y) or (x and not z))
print(x or not y and not(x or not z))
x = True
y = False
z = True
print(not(x or y) and (not x or not z))
print(not(not x and y) or (x and not z))
print(x or not y and not(x or not z))
x = True
y = True
z = False
print(not(x or y) and (not x or not z))
print(not(not x and y) or (x and not z))
print(x or not y and not(x or not z))


