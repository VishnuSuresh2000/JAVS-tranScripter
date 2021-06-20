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

import os
import sys
from JAVS_Util.exceptions import JAVSError, StringNotCompleteError
from JAVS_Util.preCheckFile import PreCheckFile
from JAVS_Util.tokenize import Tokenize
from JAVS_Util.globalTape import JAVSGlobalTape
from JAVS_Util.machine import Machine
from Env.arithmeticEnv import ArithmeticEnv

# def betaCheckString(tokens):
#     stringFlag=False
#     stringVariable=""
#     for word in tokens:
#         if "'" == word:
#             print("got ' ")
#             stringFlag=not stringFlag
#         elif "'" in word:
#             print("got a word with ' ",word[1:])
#             stringFlag=not stringFlag
#             if stringFlag:
#                 stringVariable=word[1:]
#             else:
#                 print("String Variable :- ",stringVariable)
#         else:
#             if stringFlag:
#                 stringVariable=f'{stringVariable} {word}'
#             else:
#                 print("String Variable :- ",stringVariable)
#             print(word)
#     if stringFlag:
#         raise StringNotCompleteError()

def main(path, print_log=False, generate_Python_code=False):
    try:
        input_string = PreCheckFile.load(path)
        Tokenize.initNLTK()
        tokenize = Tokenize.make(input_string)
        if print_log:
            print("Tokenized Input :- ", tokenize)
        # betaCheckString(tokenize)
        word_list = Tokenize.generateWordListFromEnv(ArithmeticEnv)
        # print(" World_list of Env :- ", word_list)
        # word_list=...(ArithmeticEnv.env_Variables)...ArithmeticEnv.env_Words_and_WordAsFunction.keys()
        Tokenize.checkAllWordsInEnv(words_list=tokenize, env_words=word_list)
        tape = JAVSGlobalTape.make(tokenize_Input=tokenize,
                               env=ArithmeticEnv, show_logs=print_log)
        # print("Tape :- ", tape)
        pyCode = Machine.generatePythonCode(tape, ArithmeticEnv)
        if print_log:
            print("Python Code :- ", "\n".join(pyCode))

        Machine.executePyCode(pyCode)
        if generate_Python_code:
            Machine.generatePyFile(os.path.split(
                "main/document/main.ai")[-1][:-3], pyCode)
    except JAVSError as jerror:
        print(jerror)
    except Exception as e:
        print("Python Error :- ", e)


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print('''JAVS-tranScripter for Achu's Programming Langauge, a branch which Support Artificial language.
**** Research based project, Not For Production in line Product. ****
Four more documention https://github.com/VishnuSuresh2000/JAVS-tranScripter
\n.ai file not found.\n
Command  :- 
        javs [file_name.ai] -[flag]

        example :- javs main.ai

        if using python use the commaned :- python javs.py [file_name.ai] -[flag]

        flag :- 
                p := To generate Python code

                l := To generate Log in command Line
        ''')
        
    filePath = None
    generatePyCode = False
    show_logs = False
    for argument in arguments:

        if ("-lp" in argument) or ("-pl" in argument):
            generatePyCode = True
            show_logs = True
        elif "-p" in argument:
            generatePyCode = True
        elif "-l" in argument:
            show_logs = True
        elif ".ai" in argument:
            filePath = argument

    if filePath:
        main(filePath, print_log=show_logs, generate_Python_code=generatePyCode)
    else:
        print("JAVS Error :- File Path Not Specified, Or check the Extension")
    # print()
    # print("path :- ",os.path.altsep)
