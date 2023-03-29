
def index_string(st):
    with open('Zfile.txt', 'r') as data:
        lines = data.readlines()
        print(lines)
        data = open('Zfile.txt', 'rt')
        for index, line in enumerate(data):
            if line.split(' ')[0] == st:
                print(index+1, line)
        data.close()
        