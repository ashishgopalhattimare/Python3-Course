# https://www.codewars.com/kata/sequence-of-power-digits-sum/train/python

def sum_pow_dig_seq(start, n, k):
    
    pattern = []    # number generated pattern
    numDict = {}    # check if the any generated has occurred again or not
    
    patternFound = False
    
    for i in range(k):
        current = 0
        while start > 0:
            current += pow(start%10, n)
            start = start//10
        
        if current in numDict and patternFound == False:
            
            cyc_patt_arr = [pattern[j] for j in range(numDict[current],i)]
            h, patt_len = numDict[current]+1, i - numDict[current]
            patternFound = True
            
        pattern.append(current)
        numDict[current] = i
        
        start = current
        
    return [h, cyc_patt_arr, patt_len, start]
        
if __name__ == '__main__':
    
    print (sum_pow_dig_seq(420,4,30))
    print (sum_pow_dig_seq(420,3,5))
    print (sum_pow_dig_seq(7108, 9, 1775))