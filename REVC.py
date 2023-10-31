s='AAAACCCGGT'
#conversion of the string to its complement
map={'A':'T','T':'A','C':'G','G':'C' }
s_conv=''
for i in s:
    s_conv+=map[i]
#reverse the complement string
s_comp=s_conv[::-1]
print(s_comp)

