from Bio import SeqIO
# Import records from fasta file and put them in a list
seq_record=SeqIO.parse("LCSM_fasta_file.txt", "fasta")
seq_list=[]
for i in seq_record:
    seq_list.append(i.seq)
##################################
# Identify the shortest list and separate it from the seq_list
sample=min(seq_list)
seq_list.remove(sample)
##################################
n=len(sample)
# Function that return a list of sub-strings all with length n-k
def sub_k(sample,k):
    list_k=[]
    for i in range(k+1):
       list_k.append(sample[i:n-k+i])
    return list_k
k=0 # k indicates how short is the substring compared to the original sample string
stop=0
result=[] # This list will contain the substrings matching the research
while (k<=n-2) and stop!=1:
    list=sub_k(sample,k)
    for l in list:
        ind=0
        halt=0
        while ind<len(seq_list) and halt!=1:
            if l in seq_list[ind]:
                if ind==len(seq_list)-1:
                    result.append(l)
                    ind+=1
                else:
                    ind+=1
            else:
                halt=1
    if len(result)!=0:
        stop=1
    else:
        k+=1
print(f'Result:{result}')

    

    
