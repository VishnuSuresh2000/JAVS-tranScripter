# from JAVSutil import JAVSExceptions

# if __name__ == '__main__':
#     raise  JAVSExceptions.JAVSError()

tempString="add $v1, $v2"

def addFun(*args):
    # for identifer in args:
    #     print(identifer)
    print(" ".join([f'{x} +' for x in args]))


def commaRepalce(stringInput):
    return stringInput.replace(","," and")

# print(commaRepalce(tempString))
tempinput=commaRepalce(tempString).split(" ")
grap=[]
print(tempinput)
for word in tempinput:
    if word == "add":
        grap.append(word)
    elif word =="and" :
        if "$" in grap[-1]:
            pass




# addFun("a","v")