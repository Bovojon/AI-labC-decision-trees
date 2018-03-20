def readFile():
    attr_dict = {}
    lines_list = []
    f = open("pets.txt", 'r')
    firstLineStr = f.readline()
    firstline = firstLineStr.split()
    for attribute in firstline:
        attr_dict[attribute] = []
    with open("pets.txt", 'r') as f:
        next(f)
        for line in f:
            fields = line.split('\t')
            for i in range(len(firstline)):
                attr_dict[firstline[i]].append(fields[i])
    return attr_dict


def plurality_value(attribute, attr_dict):
    value_dict = {}
    values_list = attr_dict[attribute]
    for value in values_list:
        if value in value_dict:
            value_dict[value] += 1
        else:
            value_dict[value] = 1
    plurality = max(value_dict,key=value_dict.get)
    return plurality


if __name__ == '__main__':
    attr_dict = readFile()
    plurality = plurality_value("size", attr_dict)
    
