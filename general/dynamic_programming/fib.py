
## Recursive
def fibRecursiveWithoutMemoization(n):
    if n <=1 :
        return n
    return fibRecursiveWithoutMemoization(n-1) + fibRecursiveWithoutMemoization(n-2)

## Recursive with memoization
def fibRecursiveWithMemoization(n, lookup):
    if (lookup[n] != None):
        return lookup[n]
    
    lookup[n] = fibRecursiveWithMemoization(n-1, lookup) + fibRecursiveWithMemoization(n-2, lookup)    
    return lookup[n]

## Iterative
def fibIterative(n):
    lookup = [0] * (n+1)
    lookup[1] = 1
    for i in xrange(2, n+1):
        lookup[i] = lookup[i-1] + lookup[i-2]
    return lookup[n]    

if __name__ == '__main__':
    input = 9
    print "Fib value for number", input
    print fibRecursiveWithoutMemoization(input)
    
    lookup = [None] * (input + 1)
    lookup[0] = 0
    lookup[1] = 1
    print fibRecursiveWithMemoization(input, lookup)
    
    print fibIterative(input)