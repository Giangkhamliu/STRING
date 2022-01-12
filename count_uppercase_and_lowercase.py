string=input("Enter the string:")
count1=0
count2=0
for i in string:
    if (i.islower()):
        count1+=1
    elif(i.isupper()):
        count2+=1
print("The no. of lowercase characters is:",count1)    
print("The no. of uppercase characters is:",count2)