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

import nltk
import numpy as np
from .exceptions import *


class Tokenize:
    @staticmethod
    def initNLTK():
        try:
            nltk.data.find('tokenizers/punkt')
        except Exception as e:
            # print(e)
            if not nltk.download('punkt',quiet=True):
                raise NLTKError()


        

    @staticmethod
    def make(input_string):

        return np.array(nltk.word_tokenize(str(input_string)))

    @staticmethod
    def checkAllWordsInEnv(words_list, env_words):
        string_variable_Flag = False
        variableFlag=False
        for word in words_list:
            # if word not in env_words and "$" not in word and not str(word).isnumeric:
            #     raise WordNotFound(Word=word)
            if "'" in word:
                string_variable_Flag=not string_variable_Flag
            elif '$' in word: 
                variableFlag=True
            elif variableFlag:
                variableFlag=False
            elif (str(word).lower() not in env_words) and (not str(word).isnumeric()) and ("." not in word) and not string_variable_Flag:
                raise WordNotFound(Word=word)

    @staticmethod
    def generateWordListFromEnv(env):
        return env.env_Variables + list(env.env_Words_and_WordAsFunction.keys())
