from anytree import Node


class Tree:
    def __init__(self, rootValue:int, isFirst:bool):
        self.RootNode = Node(str(rootValue),node_value=[rootValue], is_root=True,evaluator_value=None)
        self.isFirst = isFirst
        self.generateTree(self.RootNode)
    def generateTree(self,currentNode):
        maxValue=max(currentNode.node_value)
        if maxValue <= 2:
            currentNode.is_leaf = True
            return
        else:
            currentNodeValues=currentNode.node_value.copy()
            for index,value in enumerate(currentNodeValues):
                totalChildren=(int(value/2)-1)if value%2==0 else int(value/2)
                for i in range(1,totalChildren):
                    childValue = currentNodeValues.copy()
                    childValue[index] -= i
                    childValue.insert(index+1,i)
                    child = Node(currentNode.name+"-"+str(i),parent=currentNode,node_value=childValue,evaluator_value=None)
                    self.generateTree(child)
