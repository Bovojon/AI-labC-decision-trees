from .Helpers import *

class Example:
    def __init__(self):
        self.attributes = {}
        self.classification = None

    def addAttribute(self, attribute, value):
        self.attributes[attribute] = value

    def setClassification(self, classification):
        self.classification = classification

class DecisionTree:
    def __init__(self):
        self.examples = []
        self.attributesNames = []
        self.visitedAttributes = []
        self.valueDict = {}
        self.tree = None

    def readFile(self, fileHandle):
        firstLine = fileHandle.readline().split()
        for attrib in firstLine[:-1]:
            self.attributesNames.append(attrib)
        for line in fileHandle:
            example = Example()
            fields = line.strip().split('\t')
            for i, attribute in enumerate(self.attributesNames):
                example.addAttribute(attribute, fields[i])
                if attribute not in self.valueDict:
                    self.valueDict[attribute] = [fields[i]]
                else:
                    if fields[i] not in self.valueDict[attribute]:
                        self.valueDict[attribute].append(fields[i])
            if fields[-1] == "yes":
                example.setClassification(True)
            else:
                example.setClassification(False)
            self.examples.append(example)
        self.tree = self.train()

    def train(self):
        resultTree = DecisionTreeLearning(self.examples, self.attributesNames, self.examples, self.valueDict)
        return resultTree

    def display(self):
        printTree(self.tree, 0)
