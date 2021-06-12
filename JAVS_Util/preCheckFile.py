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
                        if "." in line[-2]:
                            final_String.append(line)
                        else:
                            raise DotError(index+1)
                # print("".join(final_String))
                return "".join(final_String)
        except Exception as e:
            # print(e," ",e.message)
            raise e 