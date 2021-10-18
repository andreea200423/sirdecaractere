s1,s2='ASN ZNL HPO',''
for i in s1:
    if i==' ':
        s2+='-'
    if i=='Z':
        s2+='A'
    if i!='Z' and i!=' ': s2+=chr(ord(i)+1)
print(s2)
