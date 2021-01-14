from tree import Tree
from anytree import RenderTree



def Game():
    number_of_sticks=int(input("enter number of sticks:"))
    tree=Tree(number_of_sticks,True)
    print(RenderTree(tree.RootNode).by_attr(lambda n: ("-".join(map(str, n.node_value)) +
                                                "  [" + str(n.evaluator_value) + "]")))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
