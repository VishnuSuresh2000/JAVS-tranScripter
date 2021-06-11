import os
import sys
from JAVSutil.exceptions import JAVSError
from JAVSutil.preCheckFile import PreCheckFile
from JAVSutil.tokenize import Tokenize
from JAVSutil.globalTape import GlobalTape
from JAVSutil.machine import Machine
from Env.arithameticEnv import ArithameticEnv


def main(path, print_log=False, generate_Python_code=False):
    try:
        input_string = PreCheckFile.load(path)
        # Tokenize.initNLTK()
        tokenize = Tokenize.make(input_string)
        if print_log:
            print("Tokenized Input :- ", tokenize)
        word_list = Tokenize.generateWordListFromEnv(ArithameticEnv)
        # print(" World_list of Env :- ", word_list)
        # word_list=...(ArithameticEnv.env_Variables)...ArithameticEnv.env_Words_and_WordAsFunction.keys()
        Tokenize.checkAllWordsInEnv(words_list=tokenize, env_words=word_list)
        tape = GlobalTape.make(tokenize_Input=tokenize,
                               env=ArithameticEnv, show_logs=print_log)
        # print("Tape :- ", tape)
        pyCode = Machine.generatePythonCode(tape, ArithameticEnv)
        if print_log:
            print("Python Code :- ", "\n".join(pyCode))
        if generate_Python_code:
            Machine.generatePyFile(os.path.split(
                "main/document/main.ai")[-1][:-3], pyCode)
        Machine.executePyCode(pyCode)
    except JAVSError as jerror:
        print(jerror)
    except Exception as e:
        print("Python Error :- ", e)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    filePath=None
    generatePyCode=False
    show_logs=False
    for argument in arguments:
        
        if ("-lp" in argument) or ("-pl" in argument):
            generatePyCode=True
            show_logs=True
        elif "-p" in argument:
            generatePyCode=True
        elif "-l" in argument:
            show_logs=True
        elif ".ai" in argument:
            filePath=argument

    if filePath:
        main(filePath,print_log=show_logs,generate_Python_code=generatePyCode)
    else:
        print("JAVS Error :- File Path Not Specified, Or check the Extension")
    # print()
    # print("path :- ",os.path.altsep)
