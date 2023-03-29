def printAll():
    print('\n')
    data = open('Zfile.txt', 'r')
    for line in data:
        print(line)
    data.close()
    print('\n')

    
