class ArithmeticEnv:
    def __init__(self):
        pass
    '''
    Word As Function :- In here each word is assigned to an python function, which returns an python code as a string.
    In some sonorous some words have no functionalities in that case return "None"

    '''
    @staticmethod
    def addFun(*args):
        result = " ".join(
            [*[f'{x if "$" not in x else x[1:]} +' for x in args]])
        result = f'result =int({result[:-1]})'
        return result

    @staticmethod
    def multiplyFun(*args):
        result = " ".join(
            ["result =", *[f'{x if "$" not in x else x[1:]} *' for x in args]])
        result = result[:-1]
        return result

    @staticmethod
    def divideFun(*args):
        result = " ".join(
            [*[f'{x if "$" not in x else x[1:]} /' for x in reversed(args)]])
        result = f'result =int({result[:-1]})'
        return result

    @staticmethod
    def storeFun(*args):
        if len(args) == 2:
            # if str(args[1]).isnumeric():
            result = f'{args[0] if "$" not in args[0] else args[0][1:]}={args[1] if "$" not in args[1] else args[1][1:]}'
            # else:
            # raise Exception("Second argument must be integer")
            return result
        else:
            raise Exception("Only One variable and one Integer is support")


    


    @staticmethod
    def toFun(*args):
        return None

    @staticmethod
    def inFun(*args):
        return None

    @staticmethod
    def andFun(*args):
        return None

    @staticmethod
    def commaFun(*args):
        return ArithmeticEnv.andFun(*args)

    @staticmethod
    def byFun(*args):
        return None

    @staticmethod
    def printFun(*args):
        result = " ".join(
            ["print(", *[f'{x if "$" not in x else x[1:]}' for x in args], ")"])
        return result

    @staticmethod
    def displayFun(*args):
        return ArithmeticEnv.printFun(*args)

    '''
    env_variables :- is a list of variables which act a variables with out '$' in the program

    '''
    env_Variables = ["result"]

    '''
    env_Words_and_WordAsFunction :- is a key value paired Dictionary which each key corresponds to word that accepted by the ENV
    and the value is the function that defined 

    '''
    env_Words_and_WordAsFunction = {"add": addFun.__func__, "and": andFun.__func__, ",": commaFun.__func__, "print": printFun.__func__,
                                    "multiply": multiplyFun.__func__, "store": storeFun.__func__, "to": toFun.__func__, "in": inFun.__func__, "divide": divideFun.__func__, "by": byFun.__func__,
                                    "display":displayFun.__func__}
