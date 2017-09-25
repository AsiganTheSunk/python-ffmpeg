#!/usr/bin/env python

import subprocess, os
from ffmpeg.FFProbe import FFProbe
from ffmpeg.config import presets, audio_presets, subtitle_presets
import re
import pexpect
import select
import time

from ffmpeg.Metadata import ExtendedMetadata

from pipes import quote

# TODO make a wav to 1 channel function for the aligment
# TODO make the extract_by_index()

class FFMpeg():
    def __init__(self):
        self.COMMAND_QUIET = '-v quiet'
        self.COMMAND_OVERWRITE = '-y '
        self.default_threads = 1

    def eval_commands(self, quiet, overwrite):
        _quiet = ''
        _overwrite = ''

        if quiet:
            _quiet = self.COMMAND_QUIET

        if overwrite:
            _overwrite = self.COMMAND_OVERWRITE

        return (_quiet, _overwrite)

    '''
    
        FFMpegCLient Extraction Functions
            
            This section of the code includes the following functions:
       
        -- extract_all_subtitles: retrieve all subtitles from a media source and convert them to a especific format
        -- extract_all_audio: retrieve all audio from a media source and convert them to a especific format
      
        -- extract_subtitles: retrieve subtitles from a media source by a given index
        -- extract_audio: retrieve audio from a media source by a given index
       
    '''

    def extract_all_subtitles(self, path, dest, params=subtitle_presets['srt-preset'], debug=False, quiet=False, overwrite=False):
        try:
            ffprobe = FFProbe(path)
            ffprobe.get_metadata()
            ns_streams = ffprobe.code_type_count('subtitle')

            for index in range(0, ns_streams, 1):
                self.extract_subtitle(path=path, dest=dest, stream=index, params=params, debug=debug, quiet=quiet, overwrite=overwrite)
            return True
        except Exception as e:
            print e
            return False

    def extract_all_audio(self, path, dest, params=audio_presets['mp3-preset'], debug=False, quiet=False, overwrite=False):
        try:
            ffprobe = FFProbe(path)
            ffprobe.get_metadata()
            na_streams = ffprobe.code_type_count('audio')

            for index in range(0, na_streams, 1):
                self.extract_audio(path=path, dest=dest, stream=index, params=params, debug=debug, quiet=quiet, overwrite=overwrite)
            return True
        except Exception as e:
            print e
            return False


    #TODO Future: extract_audio_by_index() extract_audio_by_language()
    def extract_audio(self, path, dest, stream, params=audio_presets['mp3-preset'], debug=False, quiet=False, overwrite=False):
        _quiet, _overwrite = self.eval_commands(quiet=quiet, overwrite=overwrite)

        try:
            COMMAND = 'ffmpeg {overwrite} {quiet} -i {path} -map 0:a:{stream} -map_metadata 0 -ar {sampling} -ac {channels} -ab {bitrate} -threads {threads} {dest}{stream}.{audio}'.format(
                overwrite=_overwrite,
                quiet=_quiet,
                path=quote(path),
                dest=quote(dest),
                stream=stream,
                sampling=params['sampling-rate'],
                channels=params['channels'],
                audio=params['audio'],
                bitrate=params['kbitrate-audio'],
                threads=params['threads'],
            )

            if debug:
                print ' {command} \n'.format(command=COMMAND)

            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            p.communicate()
            #print p.stdout.read()

            p.stdout.close()
            return True

        except Exception as e:
            print e
            return False

    # TODO Future: extract_subtitles_by_index() extract_subtitles_by_language()
    def extract_subtitle(self, path, dest, stream, params=subtitle_presets['srt-preset'], debug=False, quiet=False, overwrite=False):
        _quiet, _overwrite = self.eval_commands(quiet=quiet, overwrite=overwrite)

        try:
            COMMAND = 'ffmpeg {overwrite} {quiet} -i {path} -map 0:s:{stream} -map_metadata 0 -c:s copy -threads {threads} {dest}{stream}.{subtitle}'.format(
                overwrite=_overwrite,
                quiet=_quiet,
                path=quote(path),
                dest=quote(dest),
                stream=stream,
                threads=params['threads'],
                subtitle = params['subtitle'],
            )
            if debug:
                print ' {command} \n'.format(command=COMMAND)


            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            p.communicate()
            p.stdout.close()

            return True
        except Exception as e:
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

    def inyect_subtitle(self, path, spath, dest, debug=False, quiet=False, overwrite=False):
        _quiet, _overwrite = self.eval_commands(quiet=quiet, overwrite=overwrite)

        try:
            COMMAND = 'ffmpeg {overwrite} {quiet} -i {path} -f {sformat} -i {spath} -map 0:v -map 0:a -map 0:s:? -map 1:s -map_metadata 0 -map_metadata 1 -c:v copy -c:a copy -c:s copy' \
                      ' -threads {threads} {dest}.{format}'.format(
                overwrite=_overwrite,
                quiet=_quiet,
                path=quote(path),
                spath=quote(spath),
                dest=quote(dest),
                format=path[-3:],
                sformat=spath[-3:],
                threads=self.default_threads
            )

            if debug:
                print ' {command} \n'.format(command=COMMAND)

            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            p.communicate()
            p.stdout.close()

            return True

        except Exception as e:
            print e
            return False


    def inyect_audio(self, path, apath, dest, debug=False, quiet=False, overwrite=False):
        _quiet, _overwrite = self.eval_commands(quiet=quiet, overwrite=overwrite)

        try:
            COMMAND = 'ffmpeg {overwrite} {quiet} -i {path} -i {apath}  -map 0:v -map 0:a -map 1:a -map 0:s:? -c:v copy -c:a copy -c:s copy' \
                      ' -threads {threads} {dest}.{format}'.format(
                overwrite=_overwrite,
                quiet=_quiet,
                path=quote(path),
                apath=quote(apath),
                dest=quote(dest),
                format=path[-3:],
                #aformat=apath[-3:],
                threads=self.default_threads
            )

            if debug:
                print ' {command} \n'.format(command=COMMAND)

            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            p.communicate()
            p.stdout.close()

        except Exception as e:
            print e
            return False

    def eval_mapping(self, master):
        if master:
            return '-map 0:v:? -map 1:0 -map 0:a -map 0:s'
        return '-map 0:v -map 0:a -map 1:0 -map 0:s'

    def inyect_audio_c(self, path, apath, dest, master=False, debug=False, quiet=False, overwrite=False):
        _quiet, _overwrite = self.eval_commands(quiet=quiet, overwrite=overwrite)
        _master = self.eval_mapping(master=master)

        try:
            # -map 0:v:? -map 1:0 -map 0:a -map 0:s:?
            COMMAND = 'ffmpeg {overwrite} {quiet} -i {path} -f {aformat} -i {apath} {mapping} -map_metadata 0 -map_metadata 1 -c:v copy -c:a copy -c:s copy' \
                      ' -threads {threads} {dest}.{format}'.format(
                overwrite=_overwrite,
                quiet=_quiet,
                path=quote(path),
                apath=quote(apath),
                dest=quote(dest),
                format=path[-3:],
                aformat=apath[-3:],
                mapping=_master,
                threads=self.default_threads
            )

            if debug:
                print ' {command} \n'.format(command=COMMAND)

            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            p.communicate()
            p.stdout.close()

        except Exception as e:
            print e
            return False

    def inyect_metadata(self, path, dest, metadata, debug=False, quiet=False, overwrite=False):
        _quiet, _overwrite = self.eval_commands(quiet=quiet, overwrite=overwrite)
        _metadata = self.unpack_metadata(metadata)

        try:
            COMMAND = 'ffmpeg {overwrite} {quiet} -i {path} -map 0:v -map 0:a -map 0:s -c:v copy -c:a copy -c:s copy {metadata} -threads {threads} {dest}.{format}'.format(
                overwrite=_overwrite,
                quiet=_quiet,
                path=quote(path),
                dest=quote(dest),
                metadata=_metadata,
                format=path[-3:],
                threads=self.default_threads
            )

            if debug:
                print ' {command} \n'.format(command=COMMAND)

            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            p.communicate()
            p.stdout.close()

            return True

        except Exception as e:
            print e
            return False

    # TODO PENDIENTE DE TERMINAR
    def unpack_metadata(self, ExtendedMetadata):
        title = ' -metadata title=' + quote(ExtendedMetadata.get_name()) + ' '
        genre = ' -metadata genre=' + quote(ExtendedMetadata.get_genre()) + ' '
        return (title + genre)


    def convert_srt_to_ass(self, path='', dest='', debug=False, quiet=False, overwrite=True):
        _quiet, _overwrite = self.eval_commands(quiet=quiet, overwrite=overwrite)
        try:
            COMMAND = 'ffmpeg {overwrite} {quiet} -i {path} -threads {threads} {dest}.ass'.format(
                overwrite=_overwrite,
                quiet=_quiet,
                path=quote(path),
                dest=quote(dest),
                threads=self.default_threads
            )

            if debug:
                print ' {command} \n'.format(command=COMMAND)

            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            p.communicate()
            p.stdout.close()
            return True

        except Exception as e:
            print e
            print 'Unable to convert srt to ass'
            return False

    def create_silence_track(self, dest, duration, params=audio_presets['mp3-preset'], debug=False, quiet=False, overwrite=False):
        _quiet, _overwrite = self.eval_commands(quiet=quiet, overwrite=overwrite)
        try:
            COMMAND = 'ffmpeg {overwrite} {quiet} -f lavfi -i aevalsrc=0:0::duration={duration} -ar {sampling} -ac {channels} -ab {bitrate} -threads {threads} {dest}.{audio}'.format(
                overwrite=_overwrite,
                quiet=_quiet,
                dest=quote(dest),
                duration=duration,
                audio=params['audio'],
                sampling=params['sampling-rate'],
                channels=params['channels'],
                bitrate=params['kbitrate-audio'],
                threads=self.default_threads
            )

            if debug:
                print ' {command} \n'.format(command=COMMAND)

            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            p.communicate()
            p.stdout.close()
            return True
        except Exception as e:
            print e
            return False

    def concat_audio_tracks(self, track0, track1, dest, params=audio_presets['mp3-preset'],debug=False, quiet=False, overwrite=False):
        _quiet, _overwrite = self.eval_commands(quiet=quiet, overwrite=overwrite)

        try:
            COMMAND = 'ffmpeg {overwrite} {quiet} -i concat:{tracks} -threads {threads} -codec copy {dest}.{audio}'.format(
                overwrite=_overwrite,
                quiet=_quiet,
                dest=quote(dest),
                audio=params['audio'],
                tracks=quote(track0 + '|' + track1),
                threads=self.default_threads
            )

            if debug:
                print ' {command} \n'.format(command=COMMAND)

            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            p.communicate()
            p.stdout.close()

            return True
        except Exception as e:
            print e
            return False


    def trim_audio(self, path, dest, _from, _to, debug=False, quiet=False, overwrite=False):
        _quiet, _overwrite = self.eval_commands(quiet=quiet, overwrite=overwrite)
        # Cut the final seconds to match the lenght of the original audio
        # ffmpeg -i '/media/asigan/1AD0F286D0F26801/audio_samples/osmosis_audio_testb1.mp3' -ss 0.6734 -to 5720.477000 -c copy '/media/asigan/1AD0F286D0F26801/audio_samples/audio_shorter.mp3'
        try:
            COMMAND = 'ffmpeg {overwrite} {quiet} -i {path} -ss {ini} -to {end} -codec copy -threads {threads} {dest}.{audio}'.format(
                overwrite=_overwrite,
                quiet=_quiet,
                path=quote(path),
                dest=quote(dest),
                ini=_from,
                end=_to,
                audio=path[-3:],
                threads=self.default_threads
            )

            if debug:
                print ' {command} \n'.format(command=COMMAND)

            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True)
            p.communicate()
            p.stdout.close()

            return True
        except Exception as e:
            print e
            return False


    '''
    
        FFMpegClient Enconding Functions
                            
            This section of the code includes the following functions:
        
        -- encode_file:
        
    '''

    def encode_file(self, path='', dest_path='', params=presets['default-preset']):
        try:
            COMMAND = 'ffmpeg -v quiet -y -i {path} -map 0:v -map 0:a -map 0:s -c:v libx265 -preset {preset} -x265-params crf={crf}:pools=none' \
                      ' -threads {threads} -c:a {audio} -ab {bitrate} -c:s copy {dest}'.format(
                path=path,
                dest=dest_path,
                preset=params['preset'],
                crf=params['crf'],
                threads=params['threads'],
                audio=params['audio'],
                bitrate=params['kbitrate-audio']
            )

            print COMMAND

            p = subprocess.Popen(COMMAND, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
            #frames = re.search('frame= *\d+', raw_data, re.IGNORECASE).group(0)
            #print frames
            p.stdout.close()
            return True
        except Exception as e:
            print e
            return False
