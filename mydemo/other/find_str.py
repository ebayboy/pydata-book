import re

# 1. 字符串替换
p = re.compile("blue|white|red")
repl = p.sub('color', 'blue socks and red shoes')
print("repl:", repl)

# 2. 正则匹配
logic = "1|2|3&4"
expr = "^\d+[&|](\d+[&|]){0,}\d+$"
regp = re.compile(expr)
res = regp.match(logic)
if res == None:
    print("match failed!")
else:
    print("match success! res:", res)

print("+++++++++++ check match && search ==============")
print(re.match('super', 'superstition'))
print(re.match('super', 'insuperable'))
print(re.search('super', 'superstition'))
print(re.search('super', 'insuperable'))
