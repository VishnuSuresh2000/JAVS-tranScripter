from . import JAVSExceptions
class PreCheckFile:
    @staticmethod
    def load(file_path):
        if not str(file_path).isnumeric: raise JAVSExceptions.FileNotFountError()
        if ".ai" not in file_path: raise JAVSExceptions.ExtensionError()
        try:
            with open(file_path) as file:
                return file.read()
        except Exception as e:
            # print(e," ",e.message)
            raise e 