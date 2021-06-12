from .exceptions import *
class PreCheckFile:
    @staticmethod
    def load(file_path):
        if not str(file_path).isnumeric: raise FileNotFountError()
        if ".ai" not in file_path: raise ExtensionError()
        try:
            with open(file_path) as file:
                return file.read()
        except Exception as e:
            # print(e," ",e.message)
            raise e 