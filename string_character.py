#  [7,13,4,10]
def solve(s):
    uc, lc, num, sp = 0, 0, 0, 0
    for ch in s:
        if ch.isupper(): uc += 1
        elif ch.islower(): lc += 1
        elif ch.isdigit(): num += 1
        else: sp += 1
    return [uc, lc, num, sp]
print(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"))


# or
s="@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"
upper=0
lower=0
num=0
special=0
l=[]
i=0
while i<len(s):
    if s[i].isupper():
        upper+=1
    elif s[i].islower():
        lower+=1
    elif s[i].isnumeric():
        num+=1
    else:
        special+=1
    i+=1
l.append(upper)
l.append(lower)
l.append(num)
l.append(special)
print(l)