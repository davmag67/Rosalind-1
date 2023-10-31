import Cod_Tab
prot='MA'
if prot=='':
    raise Exception('please insert at least 1 aminoacid')
if len(prot)>1000:
    raise Exception('max length of protein must be 1000 aminoacids')    

# Add the character corresponding to the Stop codon
prot_fin=prot+'*'
####################################################
# Function that returns the number of codons corresponding to an aminoacid
def check_cod(amm):
    count=0
    for i in Cod_Tab.RNA_dictionary:
        if Cod_Tab.RNA_dictionary[i]==amm:
            count+=1
    return count
###################################################
# Creation of a list with number of codons corresponding to each aminoacid
codnum_list=[]
for a in prot_fin:
    codnum_list.append(check_cod(a))
################################################# 
# Calculating the product of all numbers in the list module 1000000
prod=1
for x in range(len(codnum_list)):
       prod=(prod)*(codnum_list[x]) 
       prod=prod%1000000

print(prod)
            