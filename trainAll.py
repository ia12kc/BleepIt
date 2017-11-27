#!usr/bin/env pytohn


# For training words, the input required is a wav file with the same word repeated any number of times.
# Training words save all provided words as serialized objects, using the name provided by the user
   # for this process to work, the program expects one swear word, repeated
from functions import Readwav, CreateWordsList, Plot
from Word import Word
import pickle
import csv
import os
import numpy as np


trained_list = []
word_name_list = []
for f in os.listdir("VoiceSamples"):
   if f.endswith(".wav"):
      trained_list.append(Readwav("VoiceSamples/{}".format(f)))
      word_name_list.append(f[:-4])


for trained_word, word_name in zip(trained_list, word_name_list):
   print word_name
   word_list = CreateWordsList(trained_word[2], trained_word[3], trained_word[4])
   with open('graphs/{}.csv'.format(word_name), 'wb') as csvfile:
      writer = csv.writer(csvfile, delimiter=',') # creating csv file
      for sample in range(len(word_list)):
         pickle.dump(word_list[sample], open('words/{}{}.p'.format(word_name, sample + 1), 'wb')) # serializing object to words/ folder
         writer.writerow(word_list[sample].wave) # writing word to csv file
   

