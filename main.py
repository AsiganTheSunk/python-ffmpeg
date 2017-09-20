#!/usr/bin/env python
from ffmpeg.FFMpegClient import FFmpegClient
import ffmpeg.exiftool as ExifTool

from ffmpeg.FFProbe import FFProbe

import os

def main():
    metadata_path = str(os.getcwd() + '/test/OutputMetadata.txt')
    metadata_path2 = str(os.getcwd() + '/test/OutputMetadata2.txt')

    mp4_source = str(os.getcwd()) + '/test/samples/SampleVideo.mkv'
    mkv_source = str(os.getcwd()) + '/test/samples/SampleVideo.mkv'
    mkv_multi_source = str(os.getcwd()) + '/test/samples/SampleMultiAS.mkv'

    subtitle_output = str(os.getcwd()) + '/test/samples/SampleSubtitle'
    audio_output = str(os.getcwd()) + '/test/samples/SampleAudio'

    ffmpeg = FFmpegClient()
    # ffmpeg.extract_subtitles(path=mkv_multi_source, dest_path=str(os.getcwd()) + '/test/samples/SampleSubtitles.ass')
    # ffmpeg.extract_audio(path=mkv_multi_source, dest_path=str(os.getcwd()) + '/test/samples/SampleAudio.mp3')


    # ffmpeg.extract_all_subtitles(mkv_multi_source, subtitle_output)
    # ffmpeg.extract_all_audio(mkv_multi_source, audio_output)

    ffprobe = FFProbe(mkv_source)
    streams = ffprobe.get_metadata()
    for i in streams:
        print str(i)



if __name__ == '__main__':
     main()
