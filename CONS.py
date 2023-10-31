import numpy as np
import pandas as pd
from Bio import SeqIO
# Import the strings of the fasta file in a list
seq_record=SeqIO.parse("CONS_fasta_file.txt", "fasta")
seq_list=[]
for i in seq_record:
    seq_list.append(i.seq)
######################################
# Control on the number of strings
if len(seq_list)>10:
    raise Exception('Max number of strings must be 10')
# Control on max length of strings
n=len(seq_list[0])
if n>1000:
    raise Exception('Max lenght of string must be 1000')
# Control that all strings are the same lenght
flag=0
for c in range(1,len(seq_list)):
    if len(seq_list[c])==n:
       pass 
    else:
        flag=1
if flag==1:
    raise Exception('The strings must have the same lenght')
#######################################
# Create an empty array for the strings
a_dna=np.empty((len(seq_list),n),dtype=str)
# Populate the array with the strings
for i in range(len(seq_list)):
    for j in range(n):
        a_dna[i,j]=seq_list[i][j]
# Create an empty array for the profile matrix
prof_matrix=np.empty((4,n),dtype=int)
######################################
# Populate the profile matrix
dict_base={0:'A',1:'C',2:'G',3:'T'}
for i in range(4):
    prof_matrix[i]=np.count_nonzero(a_dna==dict_base[i],axis=0)
# Create a Pandas dataframe
p_m=pd.DataFrame(prof_matrix,index=['A','C','G','T'])
print(p_m)
# Identify the rows with the max occurences
cons_index=prof_matrix.argmax(axis=0)
cons=''
for i in range(n):
    cons=cons+dict_base[cons_index[i]]
print(cons)
