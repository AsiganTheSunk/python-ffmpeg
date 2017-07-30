#!/usr/bin/env python

import subprocess, os

def extract_metadata(path='', dest_path=''):
    path = str(os.getcwd()) + '/test/SampleVideoSubtitles.mkv'
    dest_path = str(os.getcwd() + '/test/OutputMetadata.txt')
    try:
        print ('Exiftool: Retrieving Metadata from - ' + path)
        COMMAND = 'exiftool ' + path + ' >' + dest_path
        subprocess.call(COMMAND, shell=True)
        print('Exiftool: Successfully retrieved Metadata- ' + path)
        return
    except:
        print('Exiftool: Something went wrong retrieving Metadata from - ' + path)
        return

def inyect_metadata(self, path='', dest_path=''):
    return



def extract_audio_info(self):
    return

def extract_video_codec(self):
    return


def extract_audio_metadata(self):
    self.extract_video_codec()
    self.extract_video_res()
    self.extract_video_name()

