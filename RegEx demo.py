import re

line = "python  perl are languages"

matchObj = (r'(.*) and', line, re.M | re.I)
matchObj=re.match(r'(.*) and', line, re.M | re.I)

if matchObj:
    print("matchObj.group() :", matchObj.group())
    print("matchObj.groups():", matchObj.groups())

else:
    print("No match found!")