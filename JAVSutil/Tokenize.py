import nltk
import numpy as np
from .exceptions import *


class Tokenize:
    @staticmethod
    def initNLTK():
        if not nltk.download('punkt'):
            raise NLTKError()

    @staticmethod
    def make(input_string):
        return np.array(nltk.word_tokenize(input_string))

    @staticmethod
    def checkAllWordsInEnv(words_list, env_words):
        variableFlag=False
        for word in words_list:
            # if word not in env_words and "$" not in word and not str(word).isnumeric:
            #     raise WordNotFound(Word=word)
            if '$' in word: 
                variableFlag=True
            elif variableFlag:
                variableFlag=False
            elif (word not in env_words) and (not str(word).isnumeric()) and ("." not in word):
                raise WordNotFound(Word=word)

    @staticmethod
    def generateWordListFromEnv(env):
        return env.env_Variables + list(env.env_Words_and_WordAsFunction.keys())
