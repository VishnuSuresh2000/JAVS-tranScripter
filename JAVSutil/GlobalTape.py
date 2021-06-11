import numpy as np
from .customTree import CustomTree


class GlobalTape:
    @staticmethod
    def make(tokenize_Input: np.array,env, show_logs: bool = False):
        global_Tape = []
        itreate_each_word = iter(tokenize_Input)
        catch_variable_value = False
        end_Of_a_Sentence = True
        node = None
        try:
            while True:
                current_Word = next(itreate_each_word)
                if "$" == current_Word and not catch_variable_value:
                    catch_variable_value = True
                elif "." == current_Word and not end_Of_a_Sentence:
                    end_Of_a_Sentence = True
                    if show_logs  : print("\nCustom Tree Stracture of the current Sentence :- \n") 
                    if show_logs  : node.PrintTree()
                    tape = node.makeTape()
                    global_Tape.append(tape)
                    if show_logs  : print("\nEnd of a sentence", "\nTape :- \n", tape, "\n")
                else:
                    if end_Of_a_Sentence:
                        if show_logs  : print("\nStarting of a sentence\n")
                        end_Of_a_Sentence = False
                        node = CustomTree()
                    elif catch_variable_value:
                        catch_variable_value = False
                        current_Word = "$"+current_Word
                    elif str(current_Word).isnumeric():
                        current_Word = "$"+current_Word
                    elif current_Word in env.env_Variables:
                        current_Word = "$"+current_Word
                    node.insertNode(current_Word)
                    # print(current_Word)
        except StopIteration:
            if show_logs  : print("\nEnd of All the lines\n")
            if show_logs  : print("\nGlobal Tape :-\n", global_Tape)
        return global_Tape
