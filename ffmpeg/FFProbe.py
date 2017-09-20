import subprocess, os
import json

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

class FFProbe():
    def __init__(self, input_file):
        self.input_file = input_file
        self.streams = []

    def get_metadata(self):
        COMMAND = 'ffprobe -v quiet -print_format json -show_format -show_entries stream=index,profile,codec_type,codec_name,width,height:stream_tags=language ' + str(self.input_file) + ' >' + str(os.getcwd() + '/test/OutputMetadata.json')
        print COMMAND
        subprocess.call(COMMAND, shell=True)


    def parse_data(self):
        profile = ''
        width = ''
        height = ''
        language = ''

        f = open((str(os.getcwd() + '/test/OutputMetadata.json')), 'r')
        raw_data = f.read()
        data = json.loads(raw_data)

        for item in data['streams']:
            print 'ENTER'
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


            ffstream = FFStream(index, profile, codec_type, codec_name, width, height, language)
            self.streams.append(ffstream)

        return self.streams