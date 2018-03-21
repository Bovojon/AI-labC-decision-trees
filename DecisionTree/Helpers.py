import math, copy

class Node:
    def __init__(self, root):
        self.root = root
        self.children = []

    def addChild(self, child):
        self.children.append(child)

def PlurarityValue(examples):
    classifications = {}
    for example in examples:
        if example.classification in classifications:
            classifications[example.classification] += 1
        else:
            classifications[example.classification] = 1
    return max(classifications,key=classifications.get)

def EntropyValue(examples):
    # Assuming only classifications
    positive = 0
    negative = 0
    total = 0
    for example in examples:
        if example.classification == True:
            positive += 1
        else:
            negative += 1
        total += 1
    if positive == 0 or negative == 0:
        return 0
    entropyValue = -(positive/total * math.log2(positive/total)) - (negative/total * math.log2(negative/total))
    return entropyValue

def ImportanceScore(attribute, possibleValues, examples):
    splitedValues = {}
    importanceScore = 0
    for value in possibleValues:
        exampleSet = []
        for example in examples:
            if example.attributes[attribute] == value:
                exampleSet.append(example)
        splitedValues[value] = exampleSet

    for value in splitedValues:
        importanceScore += EntropyValue(splitedValues[value]) * len(splitedValues[value])/len(examples)
    return importanceScore

def DecisionTreeLearning(examples, attributes, parent_examples, valueDict):
    if len(examples) == 0:
        return PlurarityValue(parent_examples)
    elif len(set([example.classification for example in examples])) == 1:
        return examples[0].classification
    elif len(attributes) == 0:
        return PlurarityValue(examples)
    else:
        bestAttribute = attributes[0]
        bestScore = ImportanceScore(attributes[0], valueDict[attributes[0]], examples)
        for attribute in attributes:
            score = ImportanceScore(attribute, valueDict[attribute], examples)
            if score < bestScore:
                bestScore = score
                bestAttribute = attribute
        tree = Node(bestAttribute)
        for value in valueDict[bestAttribute]:
            newExamples = []
            for example in examples:
                if example.attributes[bestAttribute] == value:
                    newExamples.append(example)
            newAttribute = copy.deepcopy(attributes)
            newAttribute.remove(bestAttribute)
            tree.addChild((value, DecisionTreeLearning(newExamples, newAttribute, examples, valueDict)))
        return tree

def printTree(node, level):
    for child in node.children:
        if level > 0:
            print("|", end="")
        for i in range(level):
            print("\t", end="")

        if type(child[1]) == bool:
            print(node.root, "=", child[0] + ":", str(child[1]))
        else:
            print(node.root, "=", child[0])
            printTree(child[1], level + 1)