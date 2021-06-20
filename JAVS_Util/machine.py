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

class Machine:
    @staticmethod
    def generatePythonCode(global_Tape,env):
        pythonCode=[]
        variableBuffer=[]
        for sentenceTape in global_Tape:
            variableBuffer=[]
            pythonCodeSentence=[]
            for word in reversed(sentenceTape):
                if "$" in word :
                    variableBuffer.append(word)
                else:
                    result=env.env_Words_and_WordAsFunction[str(word).lower()](*variableBuffer)
                    if result is not None:
                        pythonCodeSentence=[result,*pythonCodeSentence]
                        variableBuffer=[]
            pythonCode=[*pythonCode,*pythonCodeSentence]
        return pythonCode
    @staticmethod
    def executePyCode(code):
        exec("\n".join(code))
    @staticmethod
    def generatePyFile(filename,code):
        with open(file=f'{filename}.generated.py',mode="w") as f:
            f.writelines("\n".join(code))
            print("**** Python Code Generated ****")