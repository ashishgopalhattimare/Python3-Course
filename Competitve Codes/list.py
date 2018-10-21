if __name__ == '__main__':
    
    result = []
    for _ in range(int(input())):
        statement = input().split(" ")
        
        if statement[0] == "insert":
            result.insert(int(statement[1]), int(statement[2]))
        
        elif statement[0] == "print":
            print (result)
        
        elif statement[0] == "append":
            result.append(int(statement[1]))
        
        elif statement[0] == "sort":
            result.sort()
        
        elif statement[0] == "pop":
            if len(result) != 0:
                result.pop()
        
        elif statement[0] == "reverse":
            result.reverse()
            
        elif statement[0] == "remove":
            if len(result) != 0:
                result.remove(int(statement[1]))