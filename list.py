a = [10, 20, 30]

print(a)

a.append(40)
print(a)

a.insert(1, 15)
print(a)

a.remove(20)
print(a)

a.pop()
print(a)

print(len(a))

print(a[0])
print(a[-1])

a.sort()
print(a)

a.reverse()
print(a)

b = [1, 2, 3]
c = [4, 5, 6]

print(b)
print(c)

d = b + c
print(d)

b.extend(c)
print(b)

for x, y in zip(b, c):
    print(x, y)

print(2 in b)

print(b == c)
