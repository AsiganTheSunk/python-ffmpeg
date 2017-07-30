#!/usr/bin/env python

import subprocess, os
from main.exiftool import extract_metadata as exifmetadata


class FFmpegClient():
    def __init__(self):
        # load default preset
        # params and stuff here
        # inicializarlo en un thread
        # ver como hacer redireccion del progreso usando str_erro, str_dev etc etc, con pipes probablemente.
        self.params = {}


    def extract_audio(self, path='', dest_path=''):
        return


    def inyect_audio(self, path='', dest_path=''):
        return


    def extract_subtitles(self, path='', dest_path=''):
        path = str(os.getcwd()) + '/test/SampleVideoSubtitles.mkv'
        dest_path = str(os.getcwd()) + '/test/OutputSampleSubtitles.ass'

        COMMAND = 'ffmpeg -i ' + path + ' -map 0:s:0 ' + dest_path
        subprocess.call(COMMAND, shell=True)
        return


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

