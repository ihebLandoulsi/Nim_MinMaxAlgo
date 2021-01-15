from tree import Tree
from anytree import Node
from random import random


class Game:
    def __init__(self):
        self.number_of_sticks: int = None
        self.isPlayerFirst: bool = None
        self.tree: Tree = None
        self.isCurrentPlayer: bool = None
        self.isAlgoMinMax: bool = None
        self.play()

    def play(self):
        self.show_title()
        self.show_insert_number_of_stick()
        self.show_Algorithm_choice()
        self.show_turn_choice()
        self.creating_tree()
        current_node = self.tree.rootNode
        while  self.available_moving_point(current_node):
            if self.isCurrentPlayer:
                current_node = self.get_human_moving_choice(current_node)
            else:
                current_node = self.get_comp_moving_choice(current_node)
            self.isCurrentPlayer = not self.isCurrentPlayer
            print("---------------------------------------------------\n\n")
        print("\n---------------------------------------------------\n\n")
        self.show_winner()
        self.show_rendered_tree()

    def available_moving_point(self, current_node):
        print("---------------------------------------------------")
        print("\t\t\t"+("    (^_^)/ YOUR" if self.isCurrentPlayer else "['-']/ COMPUTER'S") + " TURN")
        print("---------------------------------------------------")
        print("Available Moving Point")
        if current_node.is_leaf:
            print("\nThere are no available moving point T____T", end="")
            return False
        for index, child in enumerate(current_node.children):
            print(str(index + 1) + ". [" + ("-".join(map(str, child.node_value))) + "]")
        print("")
        return True

    def get_comp_moving_choice(self, current_node):
        choice_child = self.check_comp_moving_choice(current_node)
        print("Computer move\t: [" + ("-".join(map(str, choice_child.node_value))) + "]")
        print("---------------------------------------------------")
        return choice_child

    @staticmethod
    def check_comp_moving_choice(current_node) -> Node:
        child_choice = current_node.children[0]
        for child in current_node.children:
            if child.evaluator_value:
                if child.evaluator_value < child_choice.evaluator_value:
                    child_choice = child
        return child_choice

    @staticmethod
    def get_human_moving_choice(current_node):
        while True:
            moving_choice = int(input("Choose your move\t: "))
            if moving_choice - 1 in range(0, len(current_node.children)):
                child = current_node.children[moving_choice - 1]
                print("Your move\t\t: [" + ("-".join(map(str, child.node_value))) + "]")
                return child
            print("Invalid move\n")

    @staticmethod
    def show_title():
        print("\t -------------------------------")
        print("\t|                               |")
        print("\t|           NIM GAME            |")
        print("\t|                               |")
        print("\t -------------------------------\n\n")

    def show_insert_number_of_stick(self):
        print("---------------------------------------------------")
        while True:
            self.number_of_sticks = int(input("Insert number of tokens\t: "))
            if self.number_of_sticks > 0:
                break
            print("Must be positive.\n")
        print("---------------------------------------------------\n\n")

    def show_Algorithm_choice(self):
        print("---------------------------------------------------")
        print("Available Algorithms:")
        print("1. Min Max Algorithm")
        print("2. Alpha Beta Algorithm\n")
        while True:
            choice = int(input("Choose the C O M P U T E R 's Algorithm\t: "))
            if choice in range(1, 3):
                self.isAlgoMinMax = (choice == 1)
                break
            print("Invalid Choice.\n")
        print("---------------------------------------------------\n\n")

    def show_turn_choice(self):
        self.isPlayerFirst = True if random() >= 0.5 else False
        print("---------------------------------------------------")
        print("\t\t\t"+("    Y O U  ARE" if self.isPlayerFirst else "C O M P U T E R  IS") + " FIRST PLAYER")
        print("---------------------------------------------------\n\n")

    def creating_tree(self):
        print("---------------------------------------------------")
        print("Creating tree....")
        self.tree = Tree(self.number_of_sticks, self.isPlayerFirst,self.isAlgoMinMax)
        print("Tree created.")
        self.isCurrentPlayer = self.isPlayerFirst
        print("---------------------------------------------------\n\n")

    def show_rendered_tree(self):
        print("---------------------------------------------------")
        print("Nodes Visited: " + str(self.tree.nodesVisited))
        is_show_tree = input("View rendered tree [y/n]? ")
        print("---------------------------------------------------")
        if is_show_tree.capitalize() == "Y":
            print(str(self.tree))
        print("---------------------------------------------------\n\n")

    def show_winner(self):
        print("---------------------------------------------------")
        print("\t\t\t"+("      Y O U   " if not self.isCurrentPlayer else "C O M P U T E R   ") + "W I N !")
        self.isCurrentPlayer = not self.isCurrentPlayer
        print("\t\t\t"+("    Y O U   " if not self.isCurrentPlayer else "C O M P U T E R   ") + "L O S E !")
        print("---------------------------------------------------\n\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
