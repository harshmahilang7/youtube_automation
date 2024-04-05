# -*- coding: utf-8 -*-
# @Author: Dastan_Alam
# @Date:   22-03-2024 07:07:08 PM       19:07:08
# @Last Modified by:   Dastan_Alam
# @Last Modified time: 23-03-2024 12:35:30 AM       00:35:30
import numpy as np
from scipy.io import wavfile

class BinauralBeat():

    def __init__(self, parameters):
        self.sample_rate = 44100
        self.file_name = parameters['output_file_name']
        self.duration = parameters['duration']
        self.frequency_left = parameters['left']
        self.frequency_right = parameters['right']
        self.bb_frequency = abs(self.frequency_left - self.frequency_right)
        self.__beat = self.__generate_beat()

    def export(self):
        wavfile.write(self.file_name, self.sample_rate, self.__beat)
        
        print("""* Binaural beat created:
            - file name: {}
            - duration: {} s
            - binaural beat frequency (difference between frequencies): {} Hz
            - left channel frequency: {} Hz
            - right channel frequency: {} Hz
            """.format(
                self.file_name,
                self.duration,
                self.bb_frequency,
                self.frequency_left,
                self.frequency_right
            ))        
    def export2(self):
        wavfile.write(self.file_name, self.sample_rate, self.__beat)
        
        print("""* Binaural beat created:
            - file name: {}
            - duration: {} s
            - binaural beat frequency (difference between frequencies): {} Hz
            - left channel frequency: {} Hz
            - right channel frequency: {} Hz
            """.format(
                self.file_name,
                self.duration,
                self.bb_frequency,
                self.frequency_left,
                self.frequency_right
            ))        
        
    

    def __generate_beat(self):
        left = self.__generate_sine_wave(self.frequency_left)
        right = self.__generate_sine_wave(self.frequency_right)
        return np.array([left, right]).T

    def __generate_sine_wave(self, frequency):
        max_amplitude = np.iinfo(np.int16).max
        samples = np.linspace(
            0,
            self.duration,
            int(self.sample_rate * self.duration),
            endpoint=False
        )
        signal = (
            np.sin(2 * np.pi * frequency * samples) * max_amplitude
        ).astype(np.int16)
        return signal

def generate_binaural_beat(D,L,R):
    parameters = {
        'output_file_name': 'binaural_beat.wav',
        'duration': D,
        'left': L,
        'right': R
    }
    binaural_beat = BinauralBeat(parameters)
    binaural_beat.export()
