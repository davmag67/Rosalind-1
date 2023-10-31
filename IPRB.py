input=[2,2,2]

if (input[0]<0 or input[1]<0 or input[2]<0):
      raise Exception('input numbers cannot be negative')
if(input[0]+input[1]+input[2])<2:
     raise Exception('The population must have at least two individuals')

k=input[0]
m=input[1]
n=input[2]

#Case 1: Total probability if first selected is AA
#In this case, the probability of individual with dominant allele will not change independently of the second selection
def p_AA(k,m,n):
    prob_AA=k/(k+m+n)
    return prob_AA

#Case 2: Total probability if first selected is aA
def p_aA(k,m,n):
    prob_aA=m/(k+m+n)
    prob_aA_AA=k/(k+m+n-1)
    prob_aA_aA=(m-1)/(k+m+n-1)
    prob_aA_aa=n/(k+m+n-1)
    prob_aA_tot=prob_aA*(prob_aA_AA+prob_aA_aA*3/4+prob_aA_aa*1/2)
    return prob_aA_tot

#Case 3: Total probability if first selected is aa
def p_aa(k,m,n):
    prob_aa=n/(k+m+n)
    prob_aa_AA=k/(k+m+n-1)
    prob_aa_aA=m/(k+m+n-1)
    prob_aa_tot=prob_aa*(prob_aa_AA+prob_aa_aA*1/2)
    return prob_aa_tot

#The total probability of dominant allele is the sum of the 3 cases
prob_dominant=p_AA(k,m,n)+p_aA(k,m,n)+p_aa(k,m,n)
print(prob_dominant)


