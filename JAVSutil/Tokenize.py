import nltk
import numpy as np
from . import JAVSExceptions
class Tokenize:
    @staticmethod
    def initNLTK():
        if not nltk.download('punkt') : raise JAVSExceptions.NLTKError()
    
    @staticmethod
    def make(input_string):
        return np.array(nltk.word_tokenize(input_string))

    @staticmethod 
    def checkAllWordsInEnv(words_list,env_words):
        for word in words_list:
            if word not in env_words:
                raise JAVSExceptions.WordNotFound(Word=word)
                
