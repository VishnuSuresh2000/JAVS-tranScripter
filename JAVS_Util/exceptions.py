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

class JAVSError(Exception):
    staticMessage = "JAVS Error :- "
    def __init__(self,message="Custom JAVS Error"):
        self.message=self.staticMessage+" "+message
        # print(self.message)
        super().__init__(self.message)
        # pass

class ExtensionError(JAVSError):
    def __init__(self):
        self.message="Extension Error, Check the Extension as .ai"
        # print(self.message)
        super().__init__(self.message)

class FileNotFountError(JAVSError):
    def __init__(self):
        self.message="File Not Found"
        # print(self.message)
        super().__init__(self.message)

class WordNotFound(JAVSError):
    def __init__(self,Word):
        self.message=f"{Word} Word Not Found In Environment"
        # print(self.message)
        super().__init__(self.message)

class FilePathError(JAVSError):
    def __init__(self):
         self.message=f"Error With the File Path or Name"
         super().__init__(self.message)

class NLTKError(JAVSError):
    def __init__(self):
         self.message=f"NLTK Module Error, Please Check the internet Connection"
         super().__init__(self.message)

class DotError(JAVSError):
    def __init__(self,line):
         self.message=f"End of the Line or '.' not Present in the Line - {line}"
         super().__init__(self.message)