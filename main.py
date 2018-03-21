from DecisionTree.Tree import DecisionTree
import sys

def main():
    decisionTree = DecisionTree()
    inFile = open(sys.argv[1])
    decisionTree.readFile(inFile)
    decisionTree.display()

if __name__ == "__main__":
    main()
