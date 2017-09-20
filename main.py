#!/usr/bin/env python
from ffmpeg.FFMpegClient import FFmpegClient
import os
import subprocess

def main():
    mkv_multi_source = str(os.getcwd()) + '/test/samples/SampleMultiAS.mkv'
    subtitle_output = str(os.getcwd()) + '/test/samples/SampleSubtitle'
    audio_output = str(os.getcwd()) + '/test/samples/SampleAudio'

    ffmpeg = FFmpegClient()
    # ffmpeg.extract_subtitles(mkv_multi_source, (subtitle_output + '.ass'))
    # ffmpeg.extract_audio(mkv_multi_source, (audio_output + '.mp3'))

    ffmpeg.extract_all_subtitles(mkv_multi_source, subtitle_output)
    ffmpeg.extract_all_audio(mkv_multi_source, audio_output)

    '''
        Esto para recuperar la salida del comando con un pipe y tratarlo sin necesidad de fichero intermedio.
    '''
    cmd = 'ffprobe -v quiet -print_format json -show_format ' + mkv_multi_source
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    print p.stdout.read()


    #for a in iter(p.stdout.readline, b''):
    #    print a.decode('UTF-8')


    p.stdout.close()


if __name__ == '__main__':
     main()
