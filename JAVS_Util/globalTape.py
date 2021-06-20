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

import numpy as np
from .rightHandTree import RightHandTree


class JAVSGlobalTape:
    @staticmethod
    def make(tokenize_Input: np.array, env, show_logs: bool = False):
        string_initial_constant="$~"
        global_Tape = []
        iterate_each_word = iter(tokenize_Input)
        catch_variable_value = False
        end_Of_a_Sentence = True
        node = None
        catch_string_variable = False
        string_variable = ""
        try:
            while True:
                current_Word = next(iterate_each_word)
                if "$" == current_Word and not catch_variable_value and not catch_string_variable:
                    catch_variable_value = True

                elif"'" in current_Word:
                    if current_Word == "'":
                        catch_string_variable = not catch_string_variable
                        if not catch_string_variable:
                            current_Word = string_variable
                            string_variable = f'{string_initial_constant}'
                            node.insertNode(current_Word)
                            # print("Current Word :-", current_Word)
                    else:
                        catch_string_variable = not catch_string_variable
                        string_variable = f'{string_initial_constant}{current_Word[1:]}'
                elif catch_string_variable:
                    string_variable = f'{string_variable} {current_Word}'
                elif "." == current_Word and not end_Of_a_Sentence:
                    end_Of_a_Sentence = True
                    if show_logs:
                        print("\nCustom Tree Structure of the current Sentence :- \n")
                    if show_logs:
                        node.PrintTree()
                    tape = node.makeTape()
                    global_Tape.append(tape)
                    if show_logs:
                        print("\nEnd of a sentence",
                              "\nTape :- \n", tape, "\n")
                else:
                    # if str(current_Word).strip():
                    #     print(current_Word)
                    #     print("Numeric value ",current_Word)
                    if end_Of_a_Sentence:
                        if show_logs:
                            print("\nStarting of a sentence\n")
                        end_Of_a_Sentence = False
                        node = RightHandTree()
                    if catch_variable_value:
                        catch_variable_value = False
                        current_Word = "$"+current_Word
                    elif str(current_Word).isnumeric():
                        # print("Numeric value ",current_Word)
                        current_Word = "$"+current_Word
                    elif current_Word in env.env_Variables:
                        current_Word = "$"+current_Word
                    node.insertNode(current_Word)
                #     print("Current Word :-", current_Word)
                #     # node.PrintTree()
                # print("Current Word outWord :-", current_Word)
        except StopIteration:
            if show_logs:
                print("\nEnd of All the lines\n")
            if show_logs:
                print("\nGlobal Tape :-\n", global_Tape)
        return global_Tape
