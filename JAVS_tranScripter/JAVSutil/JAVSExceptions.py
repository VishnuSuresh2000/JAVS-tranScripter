class JAVSError(Exception):
    staticMessage = "JAVS-tranScripter-Error"
    def __init__(self,message="Custom JAVS Error"):
        self.message=self.staticMessage+" "+message
        # print(self.message)
        super().__init__(self.message)
        # pass

class ExtensionError(JAVSError):
    def __init__(self):
        self.message="Extenstion Error"
        # print(self.message)
        super().__init__(self.message)

class FileNotFountError(JAVSError):
    def __init__(self):
        self.message="File Not Found"
        # print(self.message)
        super().__init__(self.message)

class WordNotFound(JAVSError):
    def __init__(self,Word):
        self.message=f"{Word} Word Not Found"
        # print(self.message)
        super().__init__(self.message)