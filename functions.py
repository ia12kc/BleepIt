import scipy.io.wavfile as wavfile
import matplotlib.pyplot as pp
from Word import Word

# Reading wave from input into numpy array. 
# Returns original sounds wave numpy array, smapling rate, energy array and zcr array.
def Readwav(import_file):
   if import_file.endswith('.wav'):
      # Values for word splitting
      frame_size = 1800 # 44.1 samples/ms, 
      frame_shift = 700

      # Data
      energy = [] #sum of absolute values in range
      zcr = []    #zero-crossing rate 

      sampling_rate, num_array = wavfile.read(import_file)
      # Calculations for energy and zcr for word seperation
      for i in range(num_array.shape[0] / frame_shift - (frame_size/frame_shift)):
         frame_start = frame_shift*i
         local_sum = 0
         count = 0
         for j in range(frame_start, frame_start + frame_size): 
             local_sum = local_sum + abs(num_array[j]) # * 10
             if((num_array[j] >= 0) and (num_array[j+1] < 0)) or ((num_array[j] < 0) and (num_array[j+1] >= 0)):
                 count+= 1

         local_sum = local_sum/frame_size
         energy.append(local_sum)
         zcr.append(count)
      
      # Calculations for comparison energy
      frame_size = 180
      frame_shift = 70

      comparison_energy = []
      for i in range(num_array.shape[0] / frame_shift - (frame_size/frame_shift)):
         frame_start = frame_shift*i
         local_sum = 0
         for j in range(frame_start, frame_start + frame_size): 
             local_sum = local_sum + abs(num_array[j]) # * 10

         local_sum = local_sum/frame_size
         comparison_energy.append(local_sum)

      return num_array, sampling_rate, zcr, energy, comparison_energy # Returning two arrays of data for comparisons

   else: 
      raise ValueError('Invalid File')

# Using zcr and energy values, individual words will be sepatated into Word obejcts
def CreateWordsList(zcr, energy, comparison_energy):
   # this gives a rough start and end point of each word
   rough_words_list = []
   mark = False
   post_word_counter, pre_word_counter = 0, 0
   for x in range(len(energy)): # iterate through all energy values
       if energy[x] > 300: # looking for large energy values, resembling a word 
           post_word_counter = 0
           pre_word_counter += 1
           if pre_word_counter >= 10:
               if mark == False: # if this is the first of these large energy values, mark the start of the rough word
                   word_start = x
               mark = True

       else: # energy value is below threshold
           pre_word_counter = 0
           if mark == True: # if the energy values drop below threshold, this is the end of a word
               post_word_counter += 1
               if post_word_counter >= 10:
                   print word_start-10, x-10
                   rough_words_list.append([word_start-10, x-10])
                   mark = False # reseting the mark


   # Fixed boundary for where a word occurs
   ste_threshold = 200 
   zcr_threshold = 15
   word_list = []  # List of Word objects (containing: start time, end time, energy values)
   for x in range(len(rough_words_list)):
       cursor_right = (rough_words_list[x][0] + rough_words_list[x][1]) / 2 # Centerpoint of rough words
       cursor_left = cursor_right
   
       val_below_threshold = 0
       # Right Calculations
       while(val_below_threshold < 3): # 3 values in a row below thershold
           cursor_right += 1
           if(energy[cursor_right] < ste_threshold) and (zcr[cursor_right] > zcr_threshold):
               val_below_threshold += 1
           else:
               val_below_threshold = 0
   
       val_below_threshold = 0
       # Left Calculations

       while(val_below_threshold < 3): # 3 values in a row below thershold
           cursor_left -= 1
           if(energy[cursor_left] < ste_threshold) and (zcr[cursor_left] > zcr_threshold):
               val_below_threshold += 1
           else:
               val_below_threshold = 0
       # adding new Word object to word_list array. 

# This may be used to delete any dead sound in the word, until the word starts
       while(energy[cursor_left] < 300):
           cursor_left += 1
       word_list.append(Word(comparison_energy[cursor_left*10:cursor_right*10] , cursor_left * 10, cursor_right * 10))

   return word_list

# Removes sound from file for flagged words, sets sound to zero
def SilentBleep(file_data, sampling_rate, word_list):
	for word in word_list:
		if word.bleep:
			for i in range(word.start * 70, word.finish * 70 + 180):
				file_data[i] = 0
	wavfile.write("newFile.wav", sampling_rate, file_data)

# Plot
def Plot(values, title="", xlabel="", ylabel=""):
   pp.plot(values)
   pp.title(title)
   pp.xlabel(xlabel)
   pp.ylabel(ylabel)
   pp.show()
