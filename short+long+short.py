def solution(a, b):
    if len(a)>len(b):
        return b+a+b
    elif len(a)<len(b):
        return a+b+a
    else:
        pass
a=input("Enter the first string:-")
b=input("Enter the second string:-")
print(solution(a, b))