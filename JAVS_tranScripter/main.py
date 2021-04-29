import os
from JAVSutil import JAVSExceptions


BASE_DICTIONARY="a an and variable is then if print display as the of to input output assign initialize".split(" ")

def checkTheExtension(filename):
    if ".ai" in filename:
        return False
    else:
        return True

def loadFile(filename):
    if checkTheExtension(filename): raise JAVSExceptions.ExtensionError()
    try:
        with open(filename) as inputSource:

            try:
                lis=[]
                for x in inputSource:
                    lis.append(x.strip("\n").strip(".").split(" "))
                print(lis)
        
            except Exception() as e: 
                print(e.message)
    except FileNotFoundError:
            raise JAVSExceptions.FileNotFountError()


if __name__ == '__main__':
    print(BASE_DICTIONARY)
    exapmle_input_Path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"Example_Input","project.ai")
    # print(exapmle_input_Path)
    loadFile(exapmle_input_Path)
    
