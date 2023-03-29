def find(text):
    data = open('Zfile.txt', 'r')
    print('\n'*1)
    for line in data:
        if line.split(' ')[0] == text:
            print(line)  
    if line.split(' ')[0] != text:
        print("Не найден!")
    data.close()
    print('\n')
    return
    
    


    
    