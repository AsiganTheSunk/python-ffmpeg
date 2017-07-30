#!/usr/bin/env python
from main.FFmpegClient import FFmpegClient

def main():

    ffmpeg = FFmpegClient()
    #ffmpeg.extract_subtitles()
    #ffmpeg.extract_audio()
    ffmpeg.extract_metadata()
    return


if __name__ == '__main__':
     main()
