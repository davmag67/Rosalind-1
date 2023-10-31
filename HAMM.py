s='GAGCCTACTAACGGGAT'
t='CATCGTAATGACGGCCT'
if len(s)!=len(t):
    raise Exception('the two strings must have equal lenght')
if len(s)>1000 or len(t)>1000:
    raise Exception('max length of the strings should be 1000')
# Definition of the function calculating the Hamming distance
def d_h(s,t):
    count=0
    for i in range(len(s)):
        if s[i]!=t[i]:
            count+=1
    return count

x=d_h(s,t)
print(x)
