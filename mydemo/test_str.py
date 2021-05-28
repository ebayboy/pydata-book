s = 'hello world llo llo.'

print("capitalize:", s.capitalize())

# count of 'llo'
print("count:", s.count('llo'))

enc = s.encode(encoding='utf-8', errors='strict')
print("s:", type(s))
print("enc:", type(enc))

dec = enc.decode()
print("decode:", dec)

# endswith
ends = s.endswith('llo.')
print("ends:", ends)

# startwith
st = s.startswith('hello')
print("s.startwith:", st)

# find
f = s.find('world')
f2 = s.find('1111')
print("f:%d, f2:%d" % (f, f2))

# is alnum
print("s.ialnum('12345'):", str.isalnum('12345'))
print("s.ialnum('123a45'):", str.isalnum('123a45'))
print("s.ialnum('123a45'):", str.isalnum(''))

# isdigit
print("str.isdigit('12345'):", str.isdigit('12345'))
print("str.isdigit('11.11'):", str.isdigit('11.11'))
print("str.isdigit('a123'):", str.isdigit('a123'))
print("str.isdigit(''):", str.isdigit(''))

# isnumric
print("str.isnumeric(11.11):", str.isnumeric("11.11"))

# join
seq = ['111', '222', '333']
sep = '-'
j = str.join('-', seq)
print("str.join():", j)
