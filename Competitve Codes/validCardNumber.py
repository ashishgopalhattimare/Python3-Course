def validCard(cardNumber):
    count = 0
    digitCount = 0
    prev = '#'
    repeat = 0
    
    if cardNumber[0] not in ['4','5','6']:
        return "Invalid"
    
    for i in range(len(cardNumber)):
        if cardNumber[i] == '-':
            if count % 4 != 0 or cardNumber[i-1] == '-':
                return "Invalid"
            count = 0
            
        elif cardNumber[i].isnumeric():
            digitCount+=1
            count+=1
            
            if prev == cardNumber[i]:
                if repeat == 3:
                    return "Invalid"
                repeat+=1
            else:
                prev = cardNumber[i]
                repeat = 1
            
        else:
            return "Invalid"
        
        if digitCount > 16:
            return "Invalid"

    if digitCount == 16:
        return "Valid"
    return "Invalid"

if __name__ == '__main__':
    
    for _ in range(int(input())):
        cardNumber  = input()
        
        print (validCard(cardNumber))