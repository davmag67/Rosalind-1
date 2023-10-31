s='AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
s_A=0
s_C=0
s_G=0
s_T=0

for i in s:
    if i=='A':
        s_A+=1
    elif i=='C':
        s_C+=1
    elif i=='G':
        s_G+=1
    else:
        s_T+=1
print(s_A,s_C,s_G,s_T)





