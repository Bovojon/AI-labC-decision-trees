"""
Lam Nguyen and Jon Abdulloev
AI/ML LabC
Part2
"""

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



def decision_tree_learning(examples, attributes, parent_examples):
    if len(examples) == 0:
        return plurality_value(parent_examples)
    elif all_same_classification(examples):
        return get_classification(examples[0])
    elif len(attrs) == 0:
        return plurality_value(examples)
    else:
        attr_to_split = self.importance(attrs, examples)
        tree = createDecisionTree(attr_to_split, attribute_names[attr_to_split])
        for (v, examples_i) in self.split_by(best, examples):
            subtree = decision_tree_learning(examples_i, removeall(best, attrs), plurality_value(examples))
            tree.add(v, subtree)
        return tree


if __name__ == '__main__':
    attr_dict = readFile()
    plurality = plurality_value("size", attr_dict)
