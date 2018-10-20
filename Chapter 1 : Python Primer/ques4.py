def sumSquare(n):
    
    # Using traditional technique
    # sumTotal = 0
    # for i in range(1, n+1):
    #     sumTotal += i*i;
    # return sumTotal
    
    # Using generation technique
    # [ expression for value in iterable if condition ]
    return sum(i*i for i in range(1, n+1))

if __name__ == '__main__':
    n = int(input("Enter a value : "))
    
    print 'Sum of square from 1 to',n,':', sumSquare(n)