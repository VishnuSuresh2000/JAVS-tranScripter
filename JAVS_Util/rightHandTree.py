class RightHandTree():
    def __init__(self):
        self.left=None
        self.right=None
        self.data=None
    
    def insertNode(self,value):
        if self.data is None:
            self.data=value
        elif self.right is None:
            # print("right is none ",value)
            self.right=RightHandTree()
            self.right.insertNode(value=value)
        else:
            if "$" in self.right.data:
                # print("right is not none and $ ",value)
                temp=self.right
                self.right=RightHandTree()
                self.right.insertNode(value=value)
                self.right.left=temp
            else:
                # print("right is not none ",value)
                self.right.insertNode(value)
    def PrintTree(self,nodePostion="root",height=0):
        print(f'{self.data} : {nodePostion}, Height : {height}'),
        if self.left:
            self.left.PrintTree(nodePostion="left",height=height+1)
        if self.right:
            self.right.PrintTree(nodePostion="right",height=height+1)

    def makeTape(self):
        tape=[]
        while self.data is not None:
            tape.append(self.data)
            if self.left is not None:
                tape.append(self.left.data)
            if self.right is not None:
                self=self.right
            else:
                break
        return tape

