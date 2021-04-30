import os
from JAVSutil import JAVSExceptions
import sys
# import numpy as np

BASE_DICTIONARY = "a an and variable is then if print display as the of to input output assign initialize variables sum two".split(
    " ")


def checkTheExtension(filename):
    if ".ai" in filename:
        return False
    else:
        return True


def checkEachWord(line):
    for word in line:
        # print(word)
        try:
            int(word)
        except ValueError:
            if "$" in word:
                pass
            elif str(word).lower() not in BASE_DICTIONARY:
                # print(f'UnKnown Word { word }')
                raise JAVSExceptions.WordNotFound(word)
            # elif "$" in word:
            #     pass
        except Exception() as e:
            print(e.message)


def loadFile(filename):

    try:
        with open(filename) as inputSource:
            try:
                lis = []
                for x in inputSource:
                    lis.append(x.strip("\n").strip(".").split(" "))
                # templis=np.array(lis,dtype=np.object)
                # # print(templis.shape)
                # for line in templis:
                #     print(line)
                for line in lis:
                    # print(lines)
                    checkEachWord(line)
            except Exception() as e:
                print(e.message)
    except FileNotFoundError:
        raise JAVSExceptions.FileNotFountError()


if __name__ == '__main__':

    arguments = sys.argv[1:]
    # print(arguments)
    lenOfArgumrnt = len(arguments)
    if lenOfArgumrnt == 0:
        while True:
            try:
                line = input("JAVS >").split(" ")
                checkEachWord(line)
            except JAVSExceptions.JAVSError as error:
                print(error.message)
            except KeyboardInterrupt:
                print("\nJAVS Session Closed")
                break
            except Exception as e:
                print(f'Python Error {e.message}')
    elif lenOfArgumrnt == 1:
        # print("insideif",arguments[0]=="testit")
        if "testit" == arguments[0]:
            # print("test it working")
            arguments[0] = os.path.join(os.path.dirname(
                os.path.abspath(__file__)), "Example_Input", "project.ai")
        if checkTheExtension(arguments[0]):
            raise JAVSExceptions.ExtensionError()
        try:
            loadFile(arguments[0])
        except JAVSExceptions.JAVSError as error:
            print(error.message)
        except Exception as e:
            print(f'Python Error {e.message}')

    # print(BASE_DICTIONARY)

    # # print(exapmle_input_Path)
    # loadFile(exapmle_input_Path)

    # for i in range(1, len(sys.argv)):
    #     print(sys.argv[i], end = " ")
