#Note: this exercise was completed before learning the functionalities of BioPython
#Function that calculates the GC-Content of a given string
def gc_calc(string):
    cg_count=0
    for base in string:
        if (base=='C' or base=='G'):
            cg_count+=1
    gc_content=100*cg_count/len(string)
    return gc_content
###############################################

# Import the file in a clean list
with open('GC_Input_fasta.txt') as file:
    file_lines=(file.readlines())
    file_lines_clean=[]
    for a in file_lines:
        file_lines_clean.append(a.rstrip())
##############################################

# Creation of dictionary with IDs and strings
dict_string={}
for i in range(0,len(file_lines_clean)):
    if file_lines_clean[i][0]=='>':
        dict_string[file_lines_clean[i]]=''
        n=i+1
        stop=0
        while (file_lines_clean[n][0]!='>') and stop!=1:
            dict_string[file_lines_clean[i]]+=file_lines_clean[n]
            if n!=len(file_lines_clean)-1:
                n+=1
            else:
                stop=1
if len(dict_string)>10:
    raise Exception('max number of strings is 10')
string_check=[]
for d in dict_string:
    string_check.append(len(dict_string[d]))
if max(string_check)>1000:
    raise Exception('max length of string should be 1000')
##############################################
# Creation of dictionary wiht IDs and GC-Contents
dict_gc={}
for d in dict_string:
    result=gc_calc(dict_string[d])
    dict_gc[d[1:]]=result
##############################################
# Getting the max rsult and print it along with this ID
max_gc=round(max(dict_gc.values()),6)
max_id=max(dict_gc, key=dict_gc.get)
print(max_id)
print(max_gc)

 
