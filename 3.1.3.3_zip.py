

#zip 将列表、元祖或者其他序列元素配对， 组成一个元组构成的列表

seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'tow', 'tree', 'four']

zipped = zip(seq1, seq2)
print(f"zipped:{zipped}")

lst_zipped = list(zipped)
print(f"lst_zipped:{lst_zipped}")

seq3 = [False, True]
zip3 = zip(seq1, seq2, seq3)
lst_zip3 = list(zip3)
print(f"lst_zip3:{lst_zip3}")

# for i, (a,b) in enumerate(zip(seq1, seq2)):
for i, (a,b) in enumerate(lst_zipped):
    print("{}: {},{}".format(i, a, b))

# 行的列表转换为列的列表
pitchers = [('fan', 'pengfei'), ('lv', 'shijuan'), ('wang', 'hongbin')]
first_names, last_names = zip(*pitchers)
print(f"first_names:{first_names}")
print(f"last_names:{last_names}")
