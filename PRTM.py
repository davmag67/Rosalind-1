import mass_table
P='SKADYEK'
if len(P)>1000:
    raise Exception('Protein length cannot be bigger than 1000 aminoacids')
w_p=0
for i in P:
    w_p+=mass_table.mass_tab_dict[i]

print(round(w_p,3))