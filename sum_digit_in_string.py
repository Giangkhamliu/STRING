txt = "My position is 1st and my friend come on 4th"
i=0
sum=0
while i<len(txt):
    if txt[i].isdigit():
        sum=sum+int(txt[i])
    i=i+1
print(sum)





txt = "My position is 12 and my friend come on 4"
strng=txt.split()
i=0
sum=0
while i<len(strng):
    if strng[i].isdigit():
        sum=sum+int(strng[i])
    i=i+1
print(sum)