s='GATATATGCATATACTT'
t='ATAT'
if len(s)>1000:
    raise Exception('max length of the string should be 1000')
if len(t)>1000:
    raise Exception('max length of the sub-string should be 1000')
# Creation of the list that will include the locations of the sub-string
loc_list=[]
# Iteration on the string s
for i in range(len(s)):
    if len(s)-i >= len(t): # Verification if the remaining of the string is still longer than t
        if t[0]==s[i]:
            stop=0
            n=1
            while (n in range(1,len(t))) and stop!=1:
                if t[n]==s[i+n]:
                    n+=1
                    if n==len(t):
                        loc_list.append(i+1)
                else:
                    stop=1
print(loc_list)