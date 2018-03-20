def readFile():
    value_dict = {}
    lines_list = []
    f = open("pets.txt", 'r')
    firstLineStr = f.readline()
    firstline = firstLineStr.split()
    for attribute in firstline:
        value_dict[attribute] = []
    with open("pets.txt", 'r') as f:
        next(f)
        for line in f:
            fields = line.split('\t')
            for i in range(len(firstline)):
                value_dict[firstline[i]].append(fields[i])
    print(value_dict)

if __name__ == '__main__':
    readFile()
