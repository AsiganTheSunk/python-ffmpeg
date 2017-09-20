#!/usr/bin/env python

class FFStream():
    def __init__(self, index, profile, codec_type, codec_name, witdh, height, language):
        self.index = index
        self.profile = profile
        self.codec_type = codec_type
        self.codec_name = codec_name
        self.width = witdh
        self.height = height
        self.language = language

    def __str__(self):
        return ('index: %s\nprofile: %s\ncodec_type: %s\ncodec_name: %s\nwidth: %s\nheight: %s\nlanguage: %s\n'
                % (self.index, self.profile, self.codec_type, self.codec_name, self.width, self.height, self.language))