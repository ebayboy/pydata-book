

# 3.1.2.5 slice

seq = [7, 2, 3, 7, 5, 6, 1]
print("seq:{}".format(seq))
b = seq[1:5]
# [2,3,7,5]
print("b:{}".format(b)) 

seq[3:4] = [6,3]
print("seq:{}".format(seq))

print("seq[:5] : {}".format(seq[:5]))

print("seq[3:] : {}".format(seq[3:]))

# - 索引
print("seq[-4]:{}".format(seq[-4]))



