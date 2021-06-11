class Machine:
    @staticmethod
    def generatePythonCode(global_Tape,env):
        pythonCode=[]
        varibleBuffer=[]
        for sentenceTape in global_Tape:
            varibleBuffer=[]
            for word in reversed(sentenceTape):
                if "$" in word :
                    varibleBuffer.append(word)
                else:
                    result=env.env_Words_and_WordAsFunction[word](*varibleBuffer)
                    if result is not None:
                        pythonCode.append(result)
        return pythonCode
    @staticmethod
    def executePyCode(code):
        exec("\n".join(code))
    @staticmethod
    def generatePyFile(filename,code):
        with open(file=f'{filename}.generated.py',mode="w") as f:
            f.writelines("\n".join(code))
            print("Python Code Generted")