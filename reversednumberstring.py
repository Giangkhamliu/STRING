num=int(input("Enter the number:-"))
a=str(num)
s=""
i=-1
while i>=-len(a):
    b=a[i]
    s+=b
    i-=1
print(int(s))

