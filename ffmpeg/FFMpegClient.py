#!/usr/bin/env python

import subprocess, os
from ffmpeg.FFProbe import FFProbe

class FFmpegClient():
    def __init__(self):
        # load default preset
        # params and stuff here
        # inicializarlo en un thread
        self.params = {}

    '''
    
        FFMpegCLient Extraction Functions
            
            This section of the code includes the following functions:
       
        -- extract_all_subtitles: retrieve all subtitles from a media source and convert them to a especific format
        -- extract_all_audio: retrieve all audio from a media source and convert them to a especific format
      
        -- extract_subtitles: retrieve subtitles from a media source by a given index
        -- extract_audio: retrieve audio from a media source by a given index
       
    '''

    def extract_all_subtitles(self, path='', dest_path=''):
        try:
            ffprobe = FFProbe(path)
            ffprobe.get_metadata()
            n_streams = ffprobe.code_type_count('subtitle')

            for index in range(0, n_streams, 1):
                COMMAND = 'ffmpeg -v quiet -i ' + path + ' -map 0:s:' + str(index) + ' ' + (dest_path + str(index) + '.srt')
                #print COMMAND
                p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
                # raw_data = p.stdout.read()
                p.stdout.close()
            return True
        except:
            return False

    def extract_all_audio(self, path='', dest_path=''):
        try:
            ffprobe = FFProbe(path)
            ffprobe.get_metadata()
            n_streams = ffprobe.code_type_count('audio')

            DISABLE_VIDEO_RECORDING = ' -vn '
            AUDIO_SAMPLING = ' -ar 44100 '
            AUDIO_CHANNELS = ' -ac 2 -ab 320k '
            AUDIO_FORMAT = ' -f mp3 '

            for index in range(0, n_streams, 1):
                COMMAND = 'ffmpeg -v quiet -i ' + path + ' -map 0:a:' + str(index) + ' ' \
                          + DISABLE_VIDEO_RECORDING \
                          + AUDIO_SAMPLING + AUDIO_CHANNELS + AUDIO_FORMAT \
                          + (dest_path + str(index) + '.mp3')
                #print COMMAND
                p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
                # raw_data = p.stdout.read()
                p.stdout.close()
            return True
        except:
            return False

    #TODO Future: extract_audio_by_index() extract_audio_by_language()
    def extract_audio(self, path='', dest_path='', params={}):
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

            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            #raw_data = p.stdout.read()
            p.stdout.close()
            return True
        except Exception as e:
            print e
            print 'Unable to extract subtitles'
            return False

    # TODO Future: extract_subtitles_by_index() extract_subtitles_by_language()
    def extract_subtitles(self, path='', dest_path='', params={}):
        try:
            INPUT_FILE = ' -i '
            SUBTITLE_MAP = ' -map 0:s:0 '

            COMMAND = 'ffmpeg' + INPUT_FILE + path + SUBTITLE_MAP + dest_path
            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            #raw_data = p.stdout.read()
            p.stdout.close()
            return True
        except Exception as e:
            print e
            print 'Unable to extract subtitles'
            return False

    '''
        FFMpegCLient Inyection Functions
                    
            This section of the code includes the following functions:
        
        -- inyect_subtitles:
        -- inyect_audio:
        -- inyect_metadata:
    '''

    # Example line:
    # 'ffmpeg -i input.mp4 -f srt -i input.srt -map 0:0 -map 0:1 -map 1:0 -c:v copy -c:a copy -c:s mov_text output.mp4'
    def inyect_subtitle(self, path='', subtitles_path='', dest_path=''):
        try:
            COMMAND = 'ffmpeg -v quiet -y -i ' + path + ' -f ass -i ' + subtitles_path + ' -map 0:v -map 0:a -map 0:s -map 1:s -c:v copy -c:a copy -c:s copy ' + dest_path
            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            #raw_data = p.stdout.read()
            p.stdout.close()
            return True
        except:
            return False

    # Example line:
    # 'ffmpeg -i video.avi -i audio.mp3  -map 0:v -map 1:a -c:v copy -c:a copy output.avi'
    def inyect_audio(self, path='', audio_path='', dest_path=''):
        try:
            COMMAND = 'ffmpeg -y -i ' + path + ' -i ' + audio_path + ' -map 0:v -map 0:a -map 0:s -map 1:a -c:v copy -c:a copy -c:s copy ' + dest_path
            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            #raw_data = p.stdout.read()
            p.stdout.close()
            return True
        except Exception as e:
            print e
            return False

    # TODO Future: params={}
    # Example line:
    # 'ffmpeg -i input -c copy -metadata key1=value1 -metadata:s:v key2=value2 -metadata:s:a:0 key3=value3 out.mkv'
    def inyect_metadata(self, path='', dest_path='', params={}):
        try:
            COMMAND = 'ffmpeg -i ' + path + ' -map 0:v -map a -map s -c:v copy -c:a copy -c:s copy ' + ' -metadata genre=Fantasy ' + dest_path # TODO PARAMS SPLITTER
            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            #raw_data = p.stdout.read()
            p.stdout.close()
            return True
        except Exception as e:
            print e
            return False

    # FUNCTIONAL
    def convert_srt_to_ass(self, path='', dest_path=''):
        try:
            COMMAND = 'ffmpeg -v quiet -y -i ' + str(path) + ' ' + dest_path + '.ass'
            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            #raw_data = p.stdout.read()
            p.stdout.close()
            return True
        except:
            print 'Unable to convert srt to ass'
            return False

    '''
    
        FFMpegClient Enconding Functions
                            
            This section of the code includes the following functions:
        
        -- encode_file:
        
    '''

    def encode_file(self, path='', dest_path=''):
        return


