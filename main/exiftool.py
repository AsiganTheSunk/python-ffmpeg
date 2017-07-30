#!/usr/bin/env python

import subprocess, os
import re

AUDIO_CODEC = 'Audio Codec ID'
VIDEO_CODEC = 'Video Codec ID'
TRACK_NUMBER = 'Track Number'
TRACK_NAME = 'Track Name'
TRACK_LANGUAGE = 'Track Language'

def extract_metadata(path='', dest_path=''):

    try:
        print ('Exiftool: Retrieving Metadata from - ' + path)
        COMMAND = 'exiftool ' + path + ' >' + dest_path
        subprocess.call(COMMAND, shell=True)
        print('Exiftool: Successfully retrieved Metadata- ' + path)
        return
    except:
        print('Exiftool: Something went wrong retrieving Metadata from - ' + path)
        return

def inyect_metadata(path='', dest_path=''):
    return


def extract_audio_info():
    return


def extract_video_codec():
    return


def retrieve_file_info(path='', flag=''):
    if flag is '':
        try:
            with open(path) as f:
                lines = f.readlines()
                for line in lines:
                    print line[:-1]
        except:
            print('Exiftool: Something went wrong retrieving ' + flag + ' from - ' + path)
            return

    else:
        try:
            with open(path) as f:
                lines = f.readlines()
                for line in lines:
                    if flag in line:
                        print(str('Exiftool: ' + flag + ' - ' + line[34:-1]))
                        return
        except Exception as e:
            print('Exiftool: Something went wrong retrieving ' + flag + ' from - ' + path)
            return


def retrieve_audio_codec(path=''):
    return retrieve_file_info(path=path, flag=AUDIO_CODEC)


def retrieve_video_codec(path=''):
    return retrieve_file_info(path=path, flag=VIDEO_CODEC)


def retrieve_track_name(path=''):
    return retrieve_file_info(path=path, flag=TRACK_NAME)


def retrieve_track_language(path=''):
    return retrieve_file_info(path=path, flag=TRACK_LANGUAGE)


def retrieve_track_number(path=''):
    return retrieve_file_info(path=path, flag=TRACK_NUMBER)


def retrieve_video_info(path=''):
    retrieve_video_codec(path=path)


def retrieve_audio_info(path=''):
    retrieve_audio_codec(path=path)
    retrieve_track_name(path=path)



def retrieve_subtitles_info(path=''):
    retrieve_track_number(path=path)


