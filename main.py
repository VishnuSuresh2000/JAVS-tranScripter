from JAVSutil.preCheckFile import PreCheckFile
from JAVSutil.tokenize import Tokenize
from Env.arithameticEnv import ArithameticEnv
# import os

def main(path,print_log=False):
    try:
        input_string=PreCheckFile.load(path)
        Tokenize.initNLTK()
        tokenize=Tokenize.make(input_string)
        # print(tokenize)
        
        # word_list=...(ArithameticEnv.env_Variables)...ArithameticEnv.env_Words_and_WordAsFunction.keys()
        Tokenize.checkAllWordsInEnv(tokenize,ArithameticEnv)
    except Exception as e:
        print(e," ",e.message)




if __name__=="__main__":
    main("main.ai")
    # print("path :- ",os.path.altsep)