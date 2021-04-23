
print("======= test list =============")
list1 = ['fanpf', 786, 2.23, 'runoob', 70.2]
print("list1:", list1)
print("list1[0]:", list1[0])
print("list1[1:3]:", list1[1:3])
print("list1[-1]:", list1[-1])

print("========= test tuple=============")
tuple1 = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')
print("tuple1:", tuple1)
print("tuple1[0]", tuple1[0])
print("tuple[1:3]", tuple1[1:3])
print("tuple[2:]:", tuple1[2:])
tuple3 = tuple1 + tinytuple
print("tuple3:", tuple3)
# test modify tuple , error
tuple1[0] = 'fanpf'
print("mod ok!")
