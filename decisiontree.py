"""
Lam Nguyen and Jon Abdulloev
AI/ML LabC
Part2
"""


def decision_tree_learning(examples, attributes, parent_examples):
    if len(examples) == 0:
        return plurality(parent_examples)
    elif all_same_classification(examples):
        return get_classification(examples[0])
    elif len(attrs) == 0:
        return plurality(examples)
    else:
        attr_to_split = self.choose_attribute(attrs, examples)
        tree = createDecisionTree(attr_to_split, attribute_names[attr_to_split])
        for (v, examples_i) in self.split_by(best, examples):
            subtree = decision_tree_learning(examples_i, removeall(best, attrs), plurality(examples))
            tree.add(v, subtree)
        return tree


"""
References

https://stackoverflow.com/questions/4796764/read-file-from-line-2-or-skip-header-row

http://aima.cs.berkeley.edu/python/learning.html

https://stackoverflow.com/questions/16989647/importing-large-tab-delimited-txt-file-into-python

https://www.quora.com/How-do-I-find-the-most-repeated-integer-in-a-list-in-python

"""
