import numpy as np
import bisect

# 3.1.1 tuple
tup = tuple(['root', ['foo', 1, 2], True])
print("obj_1:{}".format(tup[1]))
tup[1].append(3)
print("obj_1:{}".format(tup[1]))
print("tup*4:{}".format(tup*4))

# 3.1.1.1 tuple拆包
tup = (4, 5, 6)
a, b, c = tup
print(f"{a}:{b}:{c}")


tup = (4, 5, (6, 7))
a, b, (c, d) = tup
print(f"{a}-{b}-{c}-{d}")

a, b = 1, 2
print("a:{} b:{}".format(a, b))
b, a = a, b
print("swap a:{} b:{}".format(a, b))

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for k1, k2, k3 in seq:
    print("{},{},{}".format(k1, k2, k3))


# test rest-value
values = 1, 2, 3, 4, 5
a, b, *rest = values
print("a:{} b:{} rest:{}".format(a, b, rest))

a, b, *_ = values
print("a:{} b:{}".format(a, b))

# 3.1.2 tuple method
a = (1, 2, 2, 2, 3, 4, 2)
print("a.count:{}".format(a.count(2)))

gen = list(range(8))
print("gen:{}".format(gen))

if 8 in gen:
    print("in")
else:
    print("not in")


lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = lst1 + lst2

print("lst3:{}".format(lst3))

lst4= []
for it in lst2:
    lst4.append(it)
print(f"lst4:{lst4}")

# 3.1.2.3 sort
a = np.random.randint(1, 100, 10)
print(f"a:{a}")
a.sort()
print("after a.sort():{}".format(a))

a = ['bb', 'ccc', 'a']
a.sort(key=len)
print(f"a:{a}")


c = [1,2,2,2,3,4,7]
pos = bisect.bisect(c,2)
print("2 pos:{}".format(pos))

pos = bisect.bisect(c,5)
print("5 pos:{}".format(pos))

bisect.insort(c,6)
print("c:{}".format(c))


