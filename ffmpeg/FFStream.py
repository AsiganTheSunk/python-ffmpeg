#!/usr/bin/env python

class FFStream():
    def __init__(self, index, profile, codec_type, codec_name, bit_rate, witdh, height, language, duration):
        self.index = index
        self.profile = profile
        self.codec_type = codec_type
        self.codec_name = codec_name
        self.bit_rate = bit_rate
        self.width = witdh
        self.height = height
        self.language = language
        self.duration = duration

    def __str__(self):
        return ('index: %s\nprofile: %s\ncodec_type: %s\ncodec_name: %s\nbit_rate: %s\nwidth: %s\nheight: %s\nlanguage: %s\nduration: %s\n'
                % (self.index, self.profile, self.codec_type, self.codec_name, self.bit_rate, self.width, self.height, self.language, self.duration))