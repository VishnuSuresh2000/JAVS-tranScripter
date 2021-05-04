# from JAVSutil import JAVSExceptions

# if __name__ == '__main__':
#     raise  JAVSExceptions.JAVSError()

tempString="add $v1, $v2 and $v3"



def commaRepalce(stringInput):
    return stringInput.replace(","," and")

# print(commaRepalce(tempString))
tempinput=commaRepalce(tempString).split(" ")
# grap=[]
print(tempinput)
# for word in tempinput:
#     if word == "add":
#         grap.append(word)
#     elif word =="and" :
#         if "$" in grap[-1]:
#             pass

class CustomTree():
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    
    def insertNode(self,value):
        if self.right is None:
            # print("right is none ",value)
            self.right=CustomTree(value)
        else:
            if "$" in self.right.data:
                # print("right is not none and $ ",value)
                temp=self.right
                self.right=CustomTree(value)
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

def makeTape(node:CustomTree):
    tape=[]
    while node.data is not None:
        tape.append(node.data)
        if node.left is not None:
            tape.append(node.left.data)
        if node.right is not None:
            node=node.right
        else:
            break
    return tape

            
itrString=iter(tempinput)
node=CustomTree(next(itrString))
try:
    while True:
        node.insertNode(next(itrString))
except StopIteration:
    pass

print("\nPrint Tree\n")



node.PrintTree()
tape =makeTape(node)


print('\nPrint Tape\n\n',tape)

variableload=[]

def addFun(*args):
    # for identifer in args:
    #     print(identifer)
    print(" ".join(["result =", *[f'{x} +' for x in args]]))

def andFun(*args):
    pass

def turingMachine(tape):
    for cell in reversed(tape):
        # print(cell)
        if "$" in cell:
            # print(f'$ detected {cell}')
            variableload.append(cell)
        elif cell == "add":
            addFun(*variableload)
        elif cell == "and":
            andFun(variableload)

turingMachine(tape)

# print("\nLoaded Variables",variableload)



# addFun("a","v")