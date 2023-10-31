n=5
k=3
if (n>40 or n<0):
    raise Exception('n must be between 0 and 40')
if(k>5 or k<0):
    raise Exception('k must be between 0 and 5')

def fib(n,k):
    if n==0:
        return 0
    else:
        if (n==1 or n==2):
            f=1
        else:
            f=fib(n-1,k) + k*fib(n-2,k)
    return f
x=fib(n,k)
print(x)