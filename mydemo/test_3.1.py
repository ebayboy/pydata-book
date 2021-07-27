
# 3.1.1.1
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    print("a={},b={},c={}".format(a, b, c))


values = 1, 2, 3, 4, 5
a, b, *rest = values
print("a:{} b:{} rest:{}".format(a,b,rest))

a, b, *_ = values
print("a:{} b:{}".format(a,b))
