class ArithameticEnv:
    def __init__(self):
        pass
    '''
    Word As Function :- In here each word is assigned to an python function, which returns an python code as a string.
    In some senarous some words have no functionalites in that case return "None"

    '''
    @staticmethod
    def addFun(*args):
        result = " ".join(
            ["result =", *[f'{x if "$" not in x else x[1:]} +' for x in args]])
        result = result[:-1]
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
            ["result =", *[f'{x if "$" not in x else x[1:]} /' for x in reversed(args)]])
        result = result[:-1]
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
        ArithameticEnv.andFun(*args)

    @staticmethod
    def byFun(*args):
        return None

    @staticmethod
    def printfun(*args):
        result = " ".join(
            ["print(", *[f'{x if "$" not in x else x[1:]}' for x in args], ")"])
        return result

    '''
    env_variables :- is a list of variables which act a variables with out '$' in the programe

    '''
    env_Variables = ["result"]

    '''
    env_Words_and_WordAsFunction :- is a key value paired Dictonary which each key corresponds to word that accepeted by the ENV
    and the value is the function that defined 

    '''
    env_Words_and_WordAsFunction = {"add": addFun.__func__, "and": andFun.__func__, ",": commaFun.__func__, "print": printfun.__func__,
                                    "multiply": multiplyFun.__func__, "store": storeFun.__func__, "to": toFun.__func__, "in": inFun.__func__, "divide": divideFun.__func__, "by": byFun.__func__}
