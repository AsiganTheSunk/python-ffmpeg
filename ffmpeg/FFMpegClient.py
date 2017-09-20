#!/usr/bin/env python

import subprocess, os
from ffmpeg.exiftool import extract_metadata as exifmetadata

from ffmpeg.exiftool import retrieve_number_of_streams

class FFmpegClient():
    def __init__(self):
        # load default preset
        # params and stuff here
        # inicializarlo en un thread
        # ver como hacer redireccion del progreso usando str_erro, str_dev etc etc, con pipes probablemente.
        self.params = {}

    def extract_all_subtitles(self, path='', dest_path=''):
        n_streams = retrieve_number_of_streams(path, 'SUBTITLE')

        for index in range(0, n_streams, 1):
            COMMAND = 'ffmpeg -v quiet -i ' + path + ' -map 0:s:' + str(index) + ' ' + (dest_path + str(index) + '.srt')
            print COMMAND
            subprocess.call(COMMAND, shell=True)
        return

    def extract_all_audio(self, path='', dest_path=''):
        n_streams = retrieve_number_of_streams(path, 'AUDIO')

        DISABLE_VIDEO_RECORDING = ' -vn '
        AUDIO_SAMPLING = ' -ar 44100 '
        AUDIO_CHANNELS = ' -ac 2 -ab 320k '
        AUDIO_FORMAT = ' -f mp3 '

        for index in range(0, n_streams, 1):
            COMMAND = 'ffmpeg -v quiet -i ' + path + ' -map 0:a:' + str(index) + ' ' \
                      + DISABLE_VIDEO_RECORDING \
                      + AUDIO_SAMPLING + AUDIO_CHANNELS + AUDIO_FORMAT \
                      + (dest_path + str(index) + '.mp3')
            print COMMAND
            subprocess.call(COMMAND, shell=True)
        return

    def extract_audio(self, path='', dest_path=''):
        try:
            INPUT_FILE = ' -i '
            DISABLE_VIDEO_RECORDING = ' -vn '
            AUDIO_SAMPLING = ' -ar 44100 '
            AUDIO_CHANNELS = ' -ac 2 -ab 320k '
            AUDIO_FORMAT = ' -f mp3 '

            COMMAND = 'ffmpeg' + INPUT_FILE + path \
                      + DISABLE_VIDEO_RECORDING \
                      + AUDIO_SAMPLING + AUDIO_CHANNELS + AUDIO_FORMAT \
                      + dest_path

            subprocess.call(COMMAND, shell=True)
            return True
        except Exception as e:
            print e
            print 'Unable to extract subtitles'
            return False


    def inyect_audio(self, path='', dest_path=''):
        return


    def extract_subtitles(self, path='', dest_path=''):
        try:
            INPUT_FILE = ' -i '
            SUBTITLE_MAP = ' -map 0:s:0 '

            COMMAND = 'ffmpeg' + INPUT_FILE + path + SUBTITLE_MAP + dest_path
            subprocess.call(COMMAND, shell=True)
            return True
        except Exception as e:
            print e
            print 'Unable to extract subtitles'
            return False


    def inyect_subtitles(self, path='', dest_path=''):
        return


    def extract_metadata(self):
        #TODO call to exiftool
        exifmetadata()
        return


    def inyect_metadata(self):
        return


    def encode_file(self, path='', dest_path=''):
        return

