def string_to_array(s):
    if s=="":
        return ['']
    else:
        a=s.split()
        return a
s=input("Enter the string:=")
print(string_to_array(s))