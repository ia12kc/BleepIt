import scipy.io.wavfile as read_wav
import matplotlib.pyplot as pp

class Readwav:

    # Constants
    frame_size = 1129 # 44.1 samples/ms, 
    frame_shift = 441

    # Data
    energy = [] #sum of absolute values in range
    zcr = []    #zero-crossing rate 

    def __init__(self, import_file):
        if import_file.endswith('.wav'):
            sampling_rate, self.num_array = read_wav.read(import_file)
            print "Sampling Rate: " + str(sampling_rate)
        else: 
            raise ValueError('Invalid File')
        
    def read(self):
        for i in range(self.num_array.shape[0] / self.frame_shift - (self.frame_size/self.frame_shift)):
            frame_start = self.frame_shift*i
            local_sum = 0
            count = 0
            for j in range(frame_start, frame_start + self.frame_size): 
                local_sum = local_sum + abs(self.num_array[j])
                if((self.num_array[j] >= 0) and (self.num_array[j+1] < 0)) or ((self.num_array[j] < 0) and (self.num_array[j+1] >= 0)):
                    count+= 1

            local_sum = local_sum/self.frame_size
            self.energy.append(local_sum)
            self.zcr.append(count)

        return self.zcr, self.energy # Returning two arrays of data for comparisons
