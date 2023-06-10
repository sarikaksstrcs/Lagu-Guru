import csv
import difflib
import pandas as pd
from tqdm import tqdm
import requests, codecs

def create_matrix(): # 2-mer array only :D
    matrix = []
    entries = ['S','N','J','B','R','Y','T','M','G','L']
    for entry in entries:
        matrix.append([0,0,0,0,0,0,0,0,0,0])
    return matrix

entries = ['S','N','J','B','R','Y','T','M','G','L']
vritham_matrix = create_matrix()

def Compute_maathra(akshara_pattern): # calculate maathra input NJYSBMTRGL string/list
    akshara_pattern=akshara_pattern.upper()
    Maathra_table = {'N':3,'J':4,'Y':5,'S':4,'B':4,
              'M':6,'T':5,'R':5,'G':2,'L':1}
    maathra = 0
    for akshara in akshara_pattern:
        maathra += Maathra_table.get(akshara,0)
    return maathra

class ml_word:
    def __init__(self, word):
        self.word = word
 
    def syllables(self):
        sign = [3330, 3331, 3390, 3391, 3392, 3393, 3394, 3395, 3396,
                3398, 3399, 3400, 3402, 3403, 3404, 3405, 3415]
        output = [];connected = False;word_len = len(self.word)
        for index in range(word_len):
            if ord(self.word[index])<3330 or ord(self.word[index])>3455:connected = False;continue
            if not connected:output.append(self.word[index])
            else:output[-1] += self.word[index]
            if index+1 >= word_len:continue
            elif ord(self.word[index+1]) in sign:connected = True
            elif ord(self.word[index]) in [3405]:
                nonsigncharacters = ""
                for character in output[-1]:
                    if ord(character) not in sign:nonsigncharacters = nonsigncharacters + character
                if output[-1].count(chr(3405))<2:connected = True
                elif (ord(self.word[index+1]) in [i for i in range(3375,3386)]):
                    if len(nonsigncharacters)<3:connected = True
                    else:connected = False
                else:
                    connected = False
                    for character in nonsigncharacters:
                        if (ord(character) in [i for i in range(3375,3386)]):
                            connected = True
                            break
            elif ord(self.word[index]) in [3451]:connected = True if ord(self.word[index+1])==3377 else False
            else:connected = False
        return output
    def laghuguru(self):
      syllable=self.syllables()
      size=len(syllable)
      mathra=[None]*size
      for oneChar in syllable:
          if not oneChar  in ['ആ', 'ഈ', 'ഊ', 'ഏ', 'ഓ', 'ഔ']:
              if not oneChar[-1][-1] in ['ാ', 'ീ', 'ൂ', 'േ', 'ൈ', 'ോ', 'ൌ', 'ൗ', 'ം', 'ഃ']:
                  syindex=syllable.index(oneChar)
                  if (syllable.count(oneChar)>0):
                      for index, value in enumerate(syllable):
                          if (value ==oneChar):
                              mathra[index] = 'L'
      
          if (len(oneChar)>= 1):
              if oneChar[-1][-1] in ['്']:
                  if (syllable.count(oneChar)==1):
                      syindex=syllable.index(oneChar)
                      mathra[syindex]=' '
                      mathra[syindex - 1] = 'G'
                  else:
                      for index, value in enumerate(syllable):
                          if (value ==oneChar):
                              mathra[index]=' '
              if oneChar  in ['ആ', 'ഈ', 'ഊ', 'ഏ', 'ഓ', 'ഔ']:
                  if (syllable.count(oneChar)==1):
                      syindex=syllable.index(oneChar)
                      mathra[syindex]='G'
                  else:
                      if (syllable.count(oneChar)>0):
                          for index, value in enumerate(syllable):
                              if (value ==oneChar):mathra[index] = 'G'
              if oneChar[-1][-1] in ['ാ', 'ീ', 'ൂ', 'േ', 'ൈ', 'ോ', 'ൌ', 'ൗ', 'ം', 'ഃ']:
                  if (syllable.count(oneChar)==1):
                      syindex=syllable.index(oneChar)
                      mathra[syindex]='G'
                  else:
                      if (syllable.count(oneChar)>0):
                          for index, value in enumerate(syllable):
                              if (value ==oneChar):mathra[index] = 'G'
          for oneChar in syllable:
              if (len(oneChar)> 2):
                  if oneChar[1][0] in ['്']:
                      if (syllable.count(oneChar)==1):
                          syindex=syllable.index(oneChar)
                          mathra[syindex-1]='G'
                      else:
                          for index, value in enumerate(syllable):
                              if (value ==oneChar):
                                  mathra[index-1]='G'
                                        
              if (len(oneChar)>= 2):
                  if oneChar[-1][-1] in ['ൈ']:
                      if (syllable.count(oneChar)==1):
                          syindex=syllable.index(oneChar)
                          mathra[syindex-1]='G'
                      else:
                          for index, value in enumerate(syllable):
                              if (value ==oneChar):
                                  mathra[index-1]='G'

      
          for oneChar in syllable:
              if oneChar in ['ൺ', 'ൻ', 'ർ', 'ൽ', 'ൾ']:
                  if (syllable.count(oneChar)==1):
                      syindex=syllable.index(oneChar)
                      mathra[syindex]=' '
                      mathra[syindex-1]='G'
        
                  else:
                      if (syllable.count(oneChar)>0):
                          for index, value in enumerate(syllable):
                              if (value ==oneChar):
                                mathra[index] = ' '
                                mathra[index-1]='G'

      #print(mathra,end='')
      return mathra
    
