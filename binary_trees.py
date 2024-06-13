"""
Binary trees:
* Convert a binary tree to a string of brackets and vice versa.
* Find the height of a tree.
* Build all possible binary trees with N nodes.
* Histogram for the height of binary trees with N=10 vertices.
* Number of binary trees with N vertices.
* Build a random binary tree with N vertices.

Author: Vadym Tunik.
"""
from random import randint
from scipy.special import comb
import matplotlib.pyplot as plt


class Tree:
    def __init__(self, key=0):
        self.key = key
        self.left = None
        self.right = None


def tree_to_brackets(tree: Tree) -> str:
    """ Convert a binary tree to a string of brackets. """
    if not tree: return ""

    result = "("
    if tree.left or tree.right:
        result += tree_to_brackets(tree.left)
        result += tree_to_brackets(tree.right)
    result += ")"
    return result


def brackets_to_tree(brackets: str) -> Tree:
    """ Convert a string of brackets to a binary tree. """
    if not brackets: return None

    stack = []
    root = Tree()
    curr = root

    for bracket in brackets:
        if bracket == '(':
            new_tree = Tree()
            if not curr.left:
                curr.left = new_tree
            elif not curr.right:
                curr.right = new_tree
            else:
                raise Exception("Not binary tree.")
            stack.append(curr)
            curr = new_tree
        elif bracket == ')':
            curr = stack.pop()

    result = root.left
    return result


def tree_height(tree: Tree) -> int:
    """ Find the height of a tree. """
    if not tree: return -1 # empty tree

    left_height = tree_height(tree.left)
    right_height = tree_height(tree.right)
    
    return max(left_height, right_height) + 1


def build_all_binary_trees(N: int) -> list:
    """ Build all possible binary trees with N nodes. """
    if N == 0: return [None]
    if N == 1: return [Tree()]

    all_binary_trees = []
    for N_left in range(N):
        N_right = N - N_left - 1

        left_subtrees = build_all_binary_trees(N_left)
        right_subtrees = build_all_binary_trees(N_right)

        for left in left_subtrees:
            for right in right_subtrees:
                tree = Tree()
                tree.left = left
                tree.right = right
                all_binary_trees.append(tree)

    return all_binary_trees


def number_of_binary_trees(N: int) -> int:
    """ Number of binary trees with N vertices. """
    return int(comb(2*N, N) / (N+1))


def build_histogram(N: int = 10) -> None:
    """ Histogram for the height of binary trees with N=10 vertices. """
    
    trees = build_all_binary_trees(N)

    heights = []
    for tree in trees:
        try:
            height = tree_height(tree)
            heights.append(height)
        except AttributeError:
            heights.append(tree)

    plt.hist(heights, bins='auto')
    plt.title(f"total #trees = {number_of_binary_trees(N)}")
    plt.xlabel('height')
    plt.ylabel('#trees')
    plt.show()


def build_random_binary_tree(N: int) -> Tree:
    """ Build a random binary tree with N vertices. """
    if N <= 0: return None
    if N == 1: return Tree()
    
    N_left = randint(0, N-1)
    N_right = N - N_left - 1
    
    left_subtree = build_random_binary_tree(N_left)
    right_subtree = build_random_binary_tree(N_right)
    
    tree = Tree()
    tree.left = left_subtree
    tree.right = right_subtree
    return tree


def test_brackets(exmpls: list) -> None:
    """ list of string brackets -> binary trees -> list of string brackets. """
    trees = []
    for exmpl in exmpls:
        try:
            tree = brackets_to_tree(exmpl)
            trees.append(tree)
        except Exception as e:
            trees.append(e)

    brackets_list = []
    for tree in trees:
        try:
            brackets = tree_to_brackets(tree)
            brackets_list.append(brackets)
        except AttributeError:
            brackets_list.append(tree)

    for index, brackets in enumerate(brackets_list):
        print(f'n.{index}: {brackets}')


def test_height(exmpls: list) -> None:
    """ list of string brackets -> binary trees -> tree heights. """
    trees = []
    for exmpl in exmpls:
        try:
            tree = brackets_to_tree(exmpl)
            trees.append(tree)
        except Exception as e:
            trees.append(e)

    heights = []
    for tree in trees:
        try:
            height = tree_height(tree)
            heights.append(height)
        except AttributeError:
            heights.append(tree)

    for index, height in enumerate(heights):
        print(f'n.{index}: {height}')


def test_build_all_binary_trees(exmpls: list) -> None:
    for N in exmpls:
        
        print(f"{N=}")
        trees = build_all_binary_trees(N)

        brackets_list = []
        for tree in trees:
            brackets = tree_to_brackets(tree)
            brackets_list.append(brackets)

        for index, brackets in enumerate(brackets_list):
            print(f'n.{index}: {brackets}')


def test_build_random_binary_tree(exmpls: list) -> None:
    for N in exmpls:
        tree = build_random_binary_tree(N)
        brackets = tree_to_brackets(tree)
        print(f'{N=}: {brackets}')


if __name__=='__main__':
    exmpl_0 = ''
    exmpl_1 = '(())'
    exmpl_2 = '(()(()))'
    exmpl_3 = '(()()()())' # not binary tree
    exmpl_4 = '(((((((((())))))))))'

    exmpls = [exmpl_0, exmpl_1, exmpl_2, exmpl_3, exmpl_4]

    print(f"\nbrackets:")
    test_brackets(exmpls)

    print(f"\nheights:")
    test_height(exmpls)

    print(f"\nall binary trees:")
    test_build_all_binary_trees([4])

    build_histogram(N=10)

    print(f"\nrandom binary trees:")
    test_build_random_binary_tree([3,33,333])
