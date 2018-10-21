def compare(x):
    return x[1]

if __name__ == '__main__':
    
    record = []
    result = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        
        record.append([name,score])
    
    record.sort(key=compare)
    
    prev = record[0][1]
    for i in range(len(record)):
        if prev != record[i][1]:
            prev = record[i][1]
            while i < len(record):
                if prev == record[i][1]:
                    result.append(record[i][0])
                else:
                    break;
                i+=1
            break
    
    result.sort()
    
    for x in result:
        print (x)