from tree import Tree
from anytree import RenderTree
from anytree.exporter import DotExporter



def Game():
    number_of_sticks=int(input("enter number of sticks:"))
    tree = Tree(number_of_sticks,True)
    # print(RenderTree(tree.RootNode).by_attr(lambda n: ("-".join(map(str, n.node_value)) +
    #                                             "  [" + str(n.evaluator_value) + "]")))
    DotExporter(tree.RootNode,nodenamefunc=lambda node: node.node_value).to_picture("test.png")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
