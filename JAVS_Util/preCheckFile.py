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

from .exceptions import *
class PreCheckFile:
    @staticmethod
    def load(file_path):
        if not str(file_path).isnumeric: raise FileNotFountError()
        if ".ai" not in file_path: raise ExtensionError()
        try:
            with open(file_path) as file:
                final_String=[]
                for index,line in enumerate(file.readlines()):
                    if line != "\n":
                        if "." in line[-2] or "." in line[-1]:
                            final_String.append(line)
                        else:
                            raise DotError(index+1)
                # print("".join(final_String))
                return "".join(final_String)
        except Exception as e:
            # print(e," ",e.message)
            raise e 