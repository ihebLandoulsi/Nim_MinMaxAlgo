from anytree import Node
from anytree import RenderTree

class Tree:
    def __init__(self, rootValue:int,isAlgoMinMax:bool):
        self.rootNode = Node(str(rootValue), node_value=[rootValue], is_root=True, evaluator_value=None)
        self.nodesVisited: int = 0
        self.generateTree(self.rootNode)
        if isAlgoMinMax:
            self.evaluateTreeMinMax(self.rootNode)
        else:
            self.evaluateTreeAlphaBeta(self.rootNode, None)
    def generateTree(self,currentNode):
        maxValue = max(currentNode.node_value)
        if maxValue <= 2:
            return
        else:
            currentNodeValues = currentNode.node_value.copy()
            for index, value in enumerate(currentNodeValues):
                totalChildren = (int(value/2)-1)if value % 2 == 0 else int(value/2)
                for i in range(1,totalChildren+1):
                    childValue = currentNodeValues.copy()
                    childValue[index] -= i
                    childValue.insert(index+1,i)
                    child = Node(currentNode.name+"-"+str(i),parent=currentNode,node_value=childValue,evaluator_value=None)
                    self.generateTree(child)
    def evaluateTreeMinMax(self,currentNode:Node):
        if currentNode.is_leaf:
            currentNode.evaluator_value = 1 if (currentNode.depth % 2 == 1) else -1
        else:
            childEvaluateValues = []
            for child in currentNode.children:
                self.evaluateTreeMinMax(child)
                childEvaluateValues.append(child.evaluator_value)
            evaluate = max(childEvaluateValues) if (currentNode.depth%2 == 0)else min(childEvaluateValues)
            currentNode.evaluator_value=evaluate
        self.nodesVisited += 1
    def evaluateTreeAlphaBeta(self,currentNode:Node,parentEvaluator:int=None):
        if currentNode.is_leaf:
            currentNode.evaluator_value = 1 if (currentNode.depth % 2 == 1)else -1
        else:
            childEvaluateValues = []
            current_evaluation: int = None
            is_current_max = currentNode.depth % 2 == 0
            for child in currentNode.children:
                self.evaluateTreeAlphaBeta(child,current_evaluation)
                if child.evaluator_value:
                    if parentEvaluator:
                        skipped: bool = (child.evaluator_value >= parentEvaluator)if is_current_max else (
                                    parentEvaluator <= child.evaluator_value)
                        if skipped:
                            return
                    if not(current_evaluation) or (is_current_max == child.evaluator_value>current_evaluation):current_evaluation=child.evaluator_value
                    childEvaluateValues.append(child.evaluator_value)
            evaluate = max(childEvaluateValues) if is_current_max else min(childEvaluateValues)
            currentNode.evaluator_value=evaluate
        self.nodesVisited += 1
    def __str__(self)->str:
        return RenderTree(self.rootNode).by_attr(lambda n: ("-".join(map(str, n.node_value)) +
                                                "  [" + str(n.evaluator_value) + "]"))