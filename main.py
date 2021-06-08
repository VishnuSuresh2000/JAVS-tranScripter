from .JAVSutil import PreCheckFile
import os

def main(path,print_log=False):
    try:
        input_string=PreCheckFile.load(path)
        print(input_string)
    except Exception as e:
        print(e," ",e.message)




if __name__=="__main__":
    # main("")
    print("path :- ",os.path)