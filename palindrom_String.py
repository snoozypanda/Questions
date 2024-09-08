import re
s = "A man, a plan, a canal: Panama"
str1=re.sub(r'[^a-zA-Z0-9]','',s).lower()
str2=list(str1)
str3=str2[::-1]
a=str3==str2
print(a)