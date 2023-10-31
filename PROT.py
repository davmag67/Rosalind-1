# Created a Codon:Aminoacid dictionary in a separate module called Cod_Tab
import Cod_Tab
s='AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
if len(s)>10000:
    raise Exception('max length of the string should be 10000')
# Convert the string s in a list of codons
codon_list=[]
first=s[0::3]
second=s[1::3]
third=s[2::3]
tot_cod=len(first)
for i in range(tot_cod):
    codon_list.append(first[i]+second[i]+third[i])
# Mapping the codons to aminoacids and print the resulting protein
protein=''
for cod in codon_list:
    protein+=Cod_Tab.RNA_dictionary[cod]
protein=protein[:-1]
print(protein)
