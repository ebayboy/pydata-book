sites = {'google', 'taobao', 'runoob', 'facebook', 'google'}

if 'google' in sites:
    print("google in sites!")
else:
    print("google not in sites")

sites = sites | {'jd.com'}
print("sites:", sites)

