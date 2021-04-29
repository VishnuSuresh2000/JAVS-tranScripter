# from JAVSutil import JAVSExceptions

# if __name__ == '__main__':
#     raise  JAVSExceptions.JAVSError()

tempString="add $v1, $v2"

def addFun(*args):
    for identifer in args:
        print(identifer)
# tempinput=tempString.strip(" ")

def commaRepalce(stringInput):
    return stringInput.replace(","," and")

print(commaRepalce(tempString))

# addFun("a","v")