 n = int(input("This code returns the nth fibonacci number. Entetr n:"))

def fib_loop(n):
    '''
    Returns the nth number in the fibonachi series.
   
    It uses for loop to calculate it.
    '''
    f1 = 1
    f2 = 1
    i=1
    while i<=n-1:
        f2,f1=f1+f2,f2
        i+=1

    return f1
print(fib_loop(n))

def fib_recursion(n):
    '''
    Returns the nth number in the fibonachi series.
   
    It uses for loop to calculate it.
    '''
    f1 = 1
    f2 = 1
    for i in range(1,n):
        f2,f1 = f1 + f2,f2
    return f1
print(fib_recursion(n))

def fib_generator(n):
    '''
    Generator version of fibonacci.
    '''
    f1 = 1
    f2 = 1
    i=1
    while i<=n-1:
        f2,f1=f1+f2,f2
        i+=1

    yield f1
print([i for i in fib_generator(n)])
 
   
print(fib_loop(8)
print(fib_recursion(13))
print([i for i in fib_generator(14)])

