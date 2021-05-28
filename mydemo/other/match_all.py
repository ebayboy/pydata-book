import re

# 贪婪匹配
s = '<html><head><title>Title</title>'
print(re.match('<.*>', s))
# <re.Match object; span=(0, 32), match='<html><head><title>Title</title>'>

# 非贪婪匹配
s2 = '<html><head><title>Title</title>'
print(re.match('<.*?>', s2))
# <re.Match object; span=(0, 6), match='<html>'>
