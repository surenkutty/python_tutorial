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
    def display(self,depth=0,node=None):
        if not node:
            node=self.root
        print(" "*depth,node.data)
        for child in node.children:
            self.display(depth+1,child)
            
    def remove(self,data):
        if not self.remove:
            print("tree is empty")
        if self.root.data==data:
            self.root=None
            return
        
        
                
tree=Tree()
tree.Add(1)        
tree.Add(2,1)        
tree.Add(3,1)        
tree.Add('a',1)        
tree.Add(4,2)        
tree.Add(5,2)        
tree.Add(6,3)        
tree.Add(7,3)        
tree.display(node=tree.root)

        