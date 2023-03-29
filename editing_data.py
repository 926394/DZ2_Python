def findZ(text):
    print('\n'*1)
    data = open('Zfile.txt', 'r+')
    for index, line in enumerate(data):
        if line.split(' ')[0] == text:
            index0 = index
            print(index0)
            print(index0, line)
            new_list = line.split()
            data = open('Zfile.txt', 'a')
            print("1.Изм. фамилию")
            print("2.Изм. имя")
            print("3.Изм. отчество")
            print("4.Изм. № тел.")
            print('\n')
            userInput = int(input("Выберите действие: "))
            if userInput == 1:
                new_list[0] = input("Изм. фамилию: ")
            if userInput == 2:
                new_list[1] = input("Изм. имя: ")
            if userInput == 3:
                new_list[2] = input("Изм. отчество: ")
            if userInput == 4:
                new_list[3] = input("Изм. № тел.: ")
            s = ' '
            data.writelines(s.join(new_list) + '\n')
            data.close()
            print('\n')
            with open('Zfile.txt', 'r') as data:
                lines = data.readlines()
                print(lines)
            data.close()
            print('\n')
            return     
    if line.split(' ')[0] != text:
        print("Не найден!")
    data.close()
    print('\n')
    return
