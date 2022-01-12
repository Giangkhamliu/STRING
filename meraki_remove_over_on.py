mainstr="the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
str=mainstr.split()
i=0
while i<len(str):
    if str[i]=="over":
        del str[i]
    else:
        print(str[i],end=" ")
    i+=1
#REPLACE OVER ON
mainstr="the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
x=mainstr.replace("over", "on")
print(x)