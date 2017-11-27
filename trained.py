#!usr/bin/env pytohn

# For training words, the input required is a wav file with the same word repeated any number of times.
# Training words save all provided words as serialized objects, using the name provided by the user
   # for this process to work, the program expects one swear word, repeated
from functions import Readwav, CreateWordsList, Plot
from Word import Word
import pickle
import csv

try:
    #  sample, sampling_rate, zcr, energy = Readwav('VoiceSamples/MattShit.wav')
    sample, sampling_rate, zcr, energy, comparison_energy = Readwav('VoiceSamples/AbeBitch.wav')
except ValueError:
    print "Invalid File"

# User input for name of swear word (for file formating)
while True:
   try:
      swear_word_name = raw_input("Enter name of swear word: ")
   except ValueError:
      print "Error. Please input a valid string"
      continue
   else: break


#  Plot(energy)
#  Plot(zcr)

word_list = CreateWordsList(zcr, energy, comparison_energy)

# Graphing and Serializing words in training input file
with open('graphs/{}.csv'.format(swear_word_name), 'wb') as csvfile:
   writer = csv.writer(csvfile, delimiter=',') # creating csv file
   for sample in range(len(word_list)):
      pickle.dump(word_list[sample], open('words/{}{}.p'.format(swear_word_name, sample + 1), 'wb')) # serializing object to words/ folder
      writer.writerow(word_list[sample].wave) # writing word to csv file
