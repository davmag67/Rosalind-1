k=2
N=1
if k>7:
    raise Exception('k cannot be higher than 7')
if N>2**k:
    raise Exception('N cannot be higher than 2**k')
# Probability that one children organism will have Aa Bb
q=0.25
# Function that calculates the factorial
def fact(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
############################################
# Function to calculate the probability of exactly N organisms at the k-th generation
def P_k(k,N,q):
    N_tot=2**k
    result=(fact(N_tot)/(fact(N)*fact(N_tot-N)))*(q**N)*((1-q)**(N_tot-N))
    return result
#############################################
# Calculation of the probability that at least N organism at the k-th generation
P_k_tot=0
for i in range(N,2**k+1):
    P_k_tot+=P_k(k,i,q)
x=round(P_k_tot,3)
print(x)

