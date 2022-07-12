def vowel_indices(word):
    words=word.lower()
    l=[]
    v="aeiouy"
    i=0
    while i<len(words):
        j=0
        while j<len(v):
            if v[j]==words[i]:
                l.append(i+1)
            j+=1
        i+=1
    return l   
print(vowel_indices("apple"))

