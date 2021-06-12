import os
import sys
from JAVS_Util.exceptions import JAVSError
from JAVS_Util.preCheckFile import PreCheckFile
from JAVS_Util.tokenize import Tokenize
from JAVS_Util.globalTape import GlobalTape
from JAVS_Util.machine import Machine
from Env.arithmeticEnv import ArithmeticEnv


def main(path, print_log=False, generate_Python_code=False):
    try:
        input_string = PreCheckFile.load(path)
        # Tokenize.initNLTK()
        tokenize = Tokenize.make(input_string)
        if print_log:
            print("Tokenized Input :- ", tokenize)
        word_list = Tokenize.generateWordListFromEnv(ArithmeticEnv)
        # print(" World_list of Env :- ", word_list)
        # word_list=...(ArithmeticEnv.env_Variables)...ArithmeticEnv.env_Words_and_WordAsFunction.keys()
        Tokenize.checkAllWordsInEnv(words_list=tokenize, env_words=word_list)
        tape = GlobalTape.make(tokenize_Input=tokenize,
                               env=ArithmeticEnv, show_logs=print_log)
        # print("Tape :- ", tape)
        pyCode = Machine.generatePythonCode(tape, ArithmeticEnv)
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
