def traverse(start, money, coins, sums):
    
    if money == sums:
        return 1
    elif money < sums:
        return 0
    
    sub_count = 0
    for i in range(start, len(coins)):
        sub_count+=traverse(i, money, coins, sums + coins[i])
    return sub_count

def count_change(money, coins):
    
    count = 0
    for i in range(0, len(coins)):
        count+=traverse(i, money, coins, coins[i])
        
    return count

if __name__ == '__main__':
    
    print (count_change(4, [1,2]))
    print (count_change(10, [5,2,3]))
    print (count_change(11, [5,7]))