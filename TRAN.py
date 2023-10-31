from Bio import SeqIO
# Import records from fasta file and put the sequences in 2 variables s1 and s2
seq_record=SeqIO.parse("TRAN_fasta_file.txt", "fasta")
s1=next(seq_record).seq
s2=next(seq_record).seq
####################################
# Check if they have the same lenght and less than 1000 elements
if len(s1)!=len(s2):
    raise Exception('The two strings must have equal lenght')
if len(s1)>1000 or len(s2)>1000:
    raise Exception('String must be max 1000 lenght')
####################################
# Define 2 tuples of Transition and Transversion combinations
set_transit=('AG','GA','CT','TC')
set_transve=('AC','CA','AT','TA','GC','CG','GT','TG')
###################################
# Compare the elements of the 2 strings
n_transition=0
n_transversion=0
for i in range(len(s1)):
    if s1[i]!=s2[i]:
        if s1[i]+s2[i] in set_transit:
            n_transition+=1
        else:
            n_transversion+=1
##################################
# Calculation of the ratio
R_s1_s2=n_transition/n_transversion
print(round(R_s1_s2,11))


         