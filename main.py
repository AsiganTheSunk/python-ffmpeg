#!/usr/bin/env python
from ffmpeg.FFMpegClient import FFmpegClient
from ffmpeg.FFProbe import FFProbe

import os
import subprocess
import json

def main():
    mkv_source = str(os.getcwd()) + '/test/samples/SampleVideo.mkv'
    mkv_multi_source = str(os.getcwd()) + '/test/samples/SampleMultiAS.mkv'

    new_mkv_multi_source = str(os.getcwd()) + '/test/samples/NewSampleMultiAS.mkv'
    subtitle_output = str(os.getcwd()) + '/test/samples/SampleSubtitle'
    audio_output = str(os.getcwd()) + '/test/samples/SampleAudio'

    ffmpeg = FFmpegClient()
    #ffmpeg.extract_all_subtitles(mkv_multi_source, subtitle_output)
    #ffmpeg.extract_all_audio(mkv_multi_source, audio_output)
    #ffmpeg.convert_srt_to_ass('/home/asigan/python-ffmpeg/test/samples/SampleSubtitle4.srt','/home/asigan/python-ffmpeg/test/samples/NewSampleSubtitle4')
    #ffmpeg.inyect_subtitle(mkv_multi_source, '/home/asigan/python-ffmpeg/test/samples/NewSampleSubtitle4.ass', '/home/asigan/python-ffmpeg/test/samples/NewSampleMultiAS.mkv')
    #ffmpeg.inyect_audio('/home/asigan/python-ffmpeg/test/samples/NewSampleMultiAS.mkv', '/home/asigan/python-ffmpeg/test/samples/SampleAudio0.mp3', '/home/asigan/python-ffmpeg/test/samples/NewSampleMultiAS.mkv')
    #ffprobe = FFProbe('/home/asigan/python-ffmpeg/test/samples/NewSampleMultiAS.mkv')
    #ffprobe.get_general_metadata()

    #ffmpeg.test(mkv_multi_source, new_mkv_multi_source)
    
    ffmpeg.encode_file(mkv_multi_source, new_mkv_multi_source)
    # TODO Further Testing!!
    #ffmpeg.inyect_metadata(mkv_multi_source, mkv_multi_source)




if __name__ == '__main__':
     main()
