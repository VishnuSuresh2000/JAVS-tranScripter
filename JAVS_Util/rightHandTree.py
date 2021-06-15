#
# Created on Mon Jun 14 2021
#
# The MIT License (MIT)
# Copyright (c) 2021 Vishnu Suresh
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

class RightHandTree():
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

    def insertNode(self, value):
        # print("need to add value ",value)
        if self.data == None:
            # print("Value added when None ", value)
            self.data = value
        elif "$" in self.data:
            # print("node contain variable need to change ",self.data)
            temp = self.data
            self.data=value
            self.right=None
            self.left = RightHandTree()
            self.left.insertNode(temp)
        elif self.right == None:
            # print("Add to right value :- ",value, " Current parent :- ",self.data )
            # print("Current tree :- ")
            # self.PrintTree()
            self.right = RightHandTree()
            self.right.insertNode(value=value)
        else:
            self.right.insertNode(value=value)
        # else:
        #     self.right.insertNode(value=value)
        # else:
        #     if "$" in self.right.data:
        #         # print("right is not none and $ ",value)
        #         temp = self.right
        #         self.right = RightHandTree()
        #         self.right.insertNode(value=value)
        #         self.right.left = temp
        #     else:
        #         # print("right is not none ",value)
        #         self.right.insertNode(value)

    def PrintTree(self, nodePostion="root", height=0):
        print(f'{self.data} : {nodePostion}, Height : {height}'),
        if self.left:
            self.left.PrintTree(nodePostion="left", height=height+1)
        if self.right:
            self.right.PrintTree(nodePostion="right", height=height+1)

    def makeTape(self):
        tape = []
        while self.data is not None:
            tape.append(self.data)
            if self.left is not None:
                tape.append(self.left.data)
            if self.right is not None:
                self = self.right
            else:
                break
        return tape
