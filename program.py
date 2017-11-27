#!usr/bin/env python

from __future__ import division
import numpy as np
import math
import os, glob, pickle
from Word import Word # created word class
from functions import Readwav, CreateWordsList, Plot, SilentBleep


try:
    sample, sampling_rate, zcr, energy, compare_energy = Readwav('Sentences/MattSentence.wav')
except ValueError:
    print "Invalid File"

# Plotting whole wav file
#Plot(energy, "Short-time Energy", "time", "energy")
#Plot(zcr, "Zero-crossing Rate", "time", "number of crosses")

word_list = CreateWordsList(zcr, energy, compare_energy)

# Retrieving serialized trained words from Words/ folder
trained_list = [] # list of trained Word objects
for f in os.listdir("words/Matt"):
   if f.endswith(".p"):
      trained_list.append(pickle.load(open("words/Matt/{}".format(f), "rb")))

# Comparisons of words
threshold = 8
for word in word_list:
   print "~" 
   number_of_matches = 0
   for trained in trained_list:
      trained_factor = trained.get_factor(word.length) # multiplication factor of trained word
      #  print "Word Length: " , len(word.wave)
      #  print "Trained Word Length: " , len(trained.wave)
      comparison_values = []
      print "~" 
      for index in range(word.length): # looks at each sample in the word
         comparison_values.append(word.wave[index]/trained.wave[int(index * trained_factor)]) # quotient of word / trained   
         #  factor = index * trained_factor
         #  #  print [int(math.floor(factor))]
         #  if int(math.floor(factor)) < (len(trained.wave) - 1):
         #      start_value = trained.wave[int(math.floor(factor))]
         #  else: start_value = len(trained.wave) - 1
         #  if int(math.ceil(factor)) < (len(trained.wave) - 1):
         #      end_value = trained.wave[int(math.ceil(factor))]
         #  else: end_value = len(trained.wave) - 1
         #  print start_value, end_value
         #  comparison_values.append(word.wave[index] / ((end_value - start_value) * factor + start_value))
      #  print np.var(comparison_values)   

      # New way, mean of comparison values, then finding what percentage of words are within a k*std_devation range 
      mean = np.mean(comparison_values)
      std_dev = np.std(comparison_values)
      counter = 0
      for value in comparison_values:
         if value < mean + std_dev/4 and value > mean - std_dev/4:
             counter += 1
      if counter / len(comparison_values) > 0.8:
          number_of_matches += 1

      # Old way of doing things, variance calulations
      #  if np.var(comparison_values) < threshold: # Marks words to be bleeped if it is below a threshold
      #     number_of_matches += 1
   if number_of_matches >= 3:
      word.bleep = True
   else:
      word.bleep = False

SilentBleep(sample, sampling_rate, word_list) # Bleep all marked words 
