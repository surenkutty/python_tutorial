class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]

class Tree:
    def __init__(self):
        self.root=None
    
    def Add(self,data,parentdata=None):
        node=TreeNode(data)
        
        
        if self.root is None:
            self.root=node
            return
        parentNode=self.findNode(parentdata,self.root)
        if not parentNode:
            print("parent not found")
            return
        parentNode.children.append(node)
            
        
    def findNode(self,data,node):
        if node.data==data:
            return node
        for child in node.children:
            nodeFound=self.findNode(data,child)
            if nodeFound is not None:
                return nodeFound
        
        return None
                
tree=Tree()
tree.Add(5)        
tree.Add(5,6)        
tree.Add(5,3)        
print(tree)
        