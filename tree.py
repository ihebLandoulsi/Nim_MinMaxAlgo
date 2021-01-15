from anytree import Node
from anytree import RenderTree


class Tree:
    def __init__(self, rootValue: int, is_player_first: bool, isAlgoMinMax: bool):
        self.rootNode = Node(str(rootValue), node_value=[rootValue], is_root=True, evaluator_value=None)
        self.nodesVisited: int = 0
        self.is_player_first = is_player_first
        self.generate_tree(self.rootNode)
        if isAlgoMinMax:
            self.evaluate_tree_min_max(self.rootNode)
        else:
            self.evaluate_tree_alpha_beta(self.rootNode)

    def generate_tree(self, currentNode) -> None:
        max_value = max(currentNode.node_value)
        if max_value <= 2:
            return
        else:
            current_node_values = currentNode.node_value.copy()
            for index, value in enumerate(current_node_values):
                total_children = (int(value / 2) - 1) if value % 2 == 0 else int(value / 2)
                for i in range(1, total_children + 1):
                    child_value = current_node_values.copy()
                    child_value[index] -= i
                    child_value.insert(index + 1, i)
                    child = Node(currentNode.name + "-" + str(i), parent=currentNode, node_value=child_value,
                                 evaluator_value=None)
                    self.generate_tree(child)

    def evaluate_tree_min_max(self, currentNode: Node) -> None:
        if currentNode.is_leaf:
            currentNode.evaluator_value = 1 if self.is_player_first == (currentNode.depth % 2 == 1) else -1
        else:
            child_evaluate_values = []
            for child in currentNode.children:
                self.evaluate_tree_min_max(child)
                child_evaluate_values.append(child.evaluator_value)
            evaluate = max(child_evaluate_values) if (currentNode.depth % 2 == 0) else min(child_evaluate_values)
            currentNode.evaluator_value = evaluate
        self.nodesVisited += 1

    def evaluate_tree_alpha_beta(self, currentNode: Node, parentEvaluator: int = None) -> None:
        if currentNode.is_leaf:
            currentNode.evaluator_value = 1 if self.is_player_first == (currentNode.depth % 2 == 1) else -1
        else:
            child_evaluate_values = []
            current_evaluation: int = None
            is_current_max = currentNode.depth % 2 == 0
            for child in currentNode.children:
                self.evaluate_tree_alpha_beta(child, current_evaluation)
                if child.evaluator_value:
                    if parentEvaluator:
                        skipped: bool = (child.evaluator_value >= parentEvaluator) if is_current_max else (
                                parentEvaluator <= child.evaluator_value)
                        if skipped:
                            return
                    if not current_evaluation or (
                            is_current_max == child.evaluator_value > current_evaluation): current_evaluation = child.evaluator_value
                    child_evaluate_values.append(child.evaluator_value)
            evaluate = max(child_evaluate_values) if is_current_max else min(child_evaluate_values)
            currentNode.evaluator_value = evaluate
        self.nodesVisited += 1

    def __str__(self) -> str:
        return RenderTree(self.rootNode).by_attr(lambda n: ("-".join(map(str, n.node_value)) +
                                                            "  [" + str(n.evaluator_value) + "]"))
