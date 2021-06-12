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
                    result=env.env_Words_and_WordAsFunction[word](*variableBuffer)
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