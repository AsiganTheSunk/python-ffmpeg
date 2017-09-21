#!/usr/bin/env python

import subprocess, os
import json
from ffmpeg.FFStream import FFStream


class FFProbe():
    def __init__(self, input_file):
        self.input_file = input_file
        self.streams = []

    def get_general_metadata(self):
        COMMAND = 'ffprobe -v quiet -print_format json -show_format -show_entries streams ' + str(self.input_file)

        p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
        raw_data = p.stdout.read()
        print raw_data
        p.stdout.close()

    def get_metadata(self):
        COMMAND = 'ffprobe -v quiet -print_format json -show_format ' \
                  '-show_entries stream=index,profile,codec_type,codec_name,width,height:stream_tags=language ' \
                  + str(self.input_file)

        p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
        raw_data = p.stdout.read()
        data = json.loads(raw_data)
        p.stdout.close()
        for item in data['streams']:
            profile = ''
            width = ''
            height = ''
            language = ''
            bit_rate = ''

            index = item['index']
            codec_type = item['codec_type']
            codec_name = item['codec_name']

            if codec_type is 'video' or 'audio':
                try:
                    profile = item['profile']

                except:
                    profile = ''

            if codec_type in 'video':
                try:
                    width = item['width']
                    height = item['height']
                except:
                    height = ''
                    width = ''

            if codec_type in 'subtitle':
                try:
                    language = item['tags']['language']
                except:
                    language = ''

            ffstream = FFStream(index, profile, codec_type, codec_name, bit_rate,width, height, language)
            self.streams.append(ffstream)

        return self.streams

    def code_type_count(self, key):
        counter = 0
        for item in self.streams:
            if item.codec_type in key:
                counter +=1

        return counter


