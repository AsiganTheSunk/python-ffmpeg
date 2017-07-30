#!/usr/bin/env python
from main.FFmpegClient import FFmpegClient
import main.exiftool as ExifTool
import os

def main():
    metadata_path = str(os.getcwd() + '/test/OutputMetadata.txt')
    source = str(os.getcwd()) + '/test/SampleVideoSubtitles.mkv'

    #ffmpeg = FFmpegClient()
    #ffmpeg.extract_subtitles()
    #ffmpeg.extract_audio()
    ExifTool.extract_metadata(path=source, dest_path=metadata_path)
    ExifTool.retrieve_audio_codec(path=metadata_path)
    ExifTool.retrieve_video_codec(path=metadata_path)
    ExifTool.retrieve_track_name(path=metadata_path)
    ExifTool.retrieve_track_language(path=metadata_path)
    print '----'*10
    ExifTool.retrieve_audio_info(path=metadata_path)
    print '----' * 10
    ExifTool.retrieve_video_info(path=metadata_path)
    print '----' * 10
    ExifTool.retrieve_file_info(path=metadata_path)

    return


if __name__ == '__main__':
     main()
