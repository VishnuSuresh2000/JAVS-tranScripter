class JAVSError(Exception):
    staticMessage = "JAVS Error :- "
    def __init__(self,message="Custom JAVS Error"):
        self.message=self.staticMessage+" "+message
        # print(self.message)
        super().__init__(self.message)
        # pass

class ExtensionError(JAVSError):
    def __init__(self):
        self.message="Extenstion Error, Check the Extension as .ai"
        # print(self.message)
        super().__init__(self.message)

class FileNotFountError(JAVSError):
    def __init__(self):
        self.message="File Not Found"
        # print(self.message)
        super().__init__(self.message)

class WordNotFound(JAVSError):
    def __init__(self,Word):
        self.message=f"{Word} Word Not Found In Env"
        # print(self.message)
        super().__init__(self.message)

class FilePathError(JAVSError):
    def __init__(self):
         self.message=f"Error With the File Path or Name"
         super().__init__(self.message)

class NLTKError(JAVSError):
    def __init__(self):
         self.message=f"NLTK Module Error, Plese Check the internet Connection"
         super().__init__(self.message)

class DotError(JAVSError):
    def __init__(self,line):
         self.message=f"End of the Line or Dot not Present at Line {line}"
         super().__init__(self.message)