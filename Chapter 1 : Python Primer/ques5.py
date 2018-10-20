def sumOddSquare(n):
    return sum(i*i for i in range(1, n+1) if i % 2 == 1)

if __name__ == '__main__':
    n = int(input("Enter a value : "))
    
    print 'Sum of Square from 1 to n [only odd] : ',sumOddSquare(n)
    