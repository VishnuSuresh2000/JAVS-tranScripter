class JAVSError(Exception):
    staticMessage = "JAVS-tranScripter-Error"
    def __init__(self,message="Custom JAVS Error"):
        self.message=self.staticMessage+" "+message
        # print(self.message)
        super().__init__(self.message)

class ExtensionError(JAVSError):
    def __init__(self):
        self.message=self.staticMessage+" "+"Extenstion Error"
        # print(self.message)
        super().__init__(self.message)

class FileNotFountError(JAVSError):
    def __init__(self):
        self.message=self.staticMessage+" "+"File Not Found"
        # print(self.message)
        super().__init__(self.message)