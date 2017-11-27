from __future__ import division

class Word:

    def __init__(self, wave, start, finish):
        self.wave = wave # for comparison
        self.start = start # start timestamp
        self.finish = finish # end timestamp
        self.length = self.finish - self.start # duration of word
        self.bleep = False

    def get_factor(self, comparison_word_length):
        return comparison_word_length  / self.length # multiplication factor
        
