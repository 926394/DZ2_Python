def Delet():
    print('\n')
    data = open('Zfile.txt', 'w')
    data.truncate()
    print('Все данные удалены!!!')
    data.close()
    print('\n')

def Delet1(text):
    with open('Zfile.txt', 'r') as data:
        lines = data.readlines()
        print(lines)
    with open('Zfile.txt', 'w') as data:
        for line in lines:
            if line.split(' ')[0] != text:
                print(line)
                data.write(line)
                print(line) 
        print('Удалено!')
        print('\n')    
 
