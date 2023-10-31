n=6
m=3
if n>100:
    raise Exception('n cannot be higher than 100')
if m>20:
    raise Exception('m cannot be higher than 20')
# Function that calculate the Fibonacci number
def fib(n):
    tab = {0:0, 1:1}
    if not n in tab:
        tab[n] = fib(n-1) + fib(n-2)
    return tab[n]
############################################
''' For 0 <= n <= m, the sequence is the same as Fibonacci.
for n>m we have to consider the sequence of different sub-types of population:
    - A: Adults (which include young and old population able to generate children)
    - O: Old (population that will die by the following month. Part of the Adults)
    - Y: Young (population that is not children and not old. Part of Adults)
    - D: Deaths (population dead in the current month)
    - C: Children (new born in the current month, not able to generate children)
    - P: entire population on a given month.
In a given month n the population P will be:
    P(n) = P(n-1) + C(n) - D(n)
In a given month n the other population types are:
    C(n) = Y(n-1) + O(n-1)
    D(n) = O(n-1)
Therefore:
    P(n) = P(n-1) + Y(n-1)
We also know that the olds in a given month are the ones that were children m-1 months before:
    O(n) = C(n-m+1) 
And we also know that the youngs in a given month n are:
    Y(n) = Y(n-1) + C(n-1) - O(n)
With some algebra manipulations we reach the following two equations:
    - P(n) = P(n-1) + C(n) - C(n-m)
    - C(n) = C(n-1) + C(n-2) - C(n-m-1)
'''
################################################
# Function that creates a dictionary with C(n) from 0 to n
def child(n,m):
# Creation of a dictionary with first C(n) results up to m
    tab_c={0:0,1:1}
    for i in range(2,m+1):
        tab_c[i]=fib(i-2) 
# Calculation of C(n) from m up to n and put in dictionary
    for i in range(m+1,n+1):
        tab_c[i]=tab_c[i-1]+tab_c[i-2]-tab_c[i-m-1]
    return tab_c    
##############################################
# Function that calculates P(n)
def Pop(n,m):
    if n<=m:
        p=fib(n)
    else:
        p=Pop(n-1,m) + tab_c[n] - tab_c[n-m]
    return p
##############################################
if n<=m:
    pop_rab=fib(n)
else:
    tab_c=child(n,m)
    pop_rab=Pop(n,m)

print(pop_rab)
