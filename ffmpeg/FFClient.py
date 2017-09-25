#!/usr/bin/env python

from ffmpeg.FFMpeg import FFMpeg
from ffmpeg.FFProbe import FFProbe

from utils.alignment_by_row_channels import align
from ffmpeg.config import audio_presets
import os

class FFClient():
    def __init__(self):
        return

    def eval_path(self, path):
        if os.path.exists(path):
            return path
        return None

    #subs = {'sync_type':'subs', 'duration':'0.05'}
    #add = {'sync_type':'add', 'duration':'0.05'}

    def eval_trim_type(self, params):
        if params['sync_type'] == 'subs':
            return params['duration'], 0

        if params['sync_type'] == 'add':
            return 0, params['duration']

    def sync_audio_tracks(self, master, slave, dest, m_stream=0, s_stream=0, params=None, debug=False, quiet=False, overwrite=True):

        _master_path = self.eval_path(master)
        _slave_path = self.eval_path(slave)
        _dest_path = self.eval_path(dest)

        ffmpeg = FFMpeg()

        if params is None:
            if debug:
                print 'FFClient extracting streams from master, slave files ...'

            ffmpeg.extract_audio(path=_master_path, dest=(_dest_path + '/master_audio'), stream=m_stream,
                                 params=audio_presets['wav-mono-preset'], debug=debug, quiet=quiet, overwrite=overwrite)
            ffmpeg.extract_audio(path=_slave_path, dest= (_dest_path + '/slave_audio'), stream=s_stream,
                                 params=audio_presets['wav-mono-preset'], debug=debug, quiet=quiet, overwrite=overwrite)

            _master_audio_path = (_dest_path + '/master_audio{stream}.wav').format(stream=m_stream)
            _slave_audio_path = (_dest_path + '/slave_audio{stream}.wav').format(stream=s_stream)

            if debug:
                print 'FFClient calculating distance between tracks ...'
            _subs, _add = align(wav1=_master_audio_path, wav2=_slave_audio_path)
            print _subs, _add
        else:
            _subs, _add = self.eval_trim_type(params=params)

        _master_ffprobe = FFProbe(_master_path)
        _master_ffprobe.get_metadata()
        _master_duration = _master_ffprobe.streams[0].duration

        _slave_ffprobe = FFProbe(_slave_path)
        _slave_ffprobe.get_metadata()
        _slave_duration = _slave_ffprobe.streams[0].duration

        if debug:
            print 'FFClient extracting slave_audio_track ...'

        ffmpeg.extract_audio(path=_slave_path, dest=(_dest_path + '/slave_audio'), stream=s_stream,
                             params=audio_presets['mp3-preset'], debug=debug, quiet=quiet, overwrite=overwrite)


        if (_subs != 0) or (_subs and _add == 0):
            if debug:
                print 'FFClient trimming slave_audio_track ...'

            _slave_audio_track = (_dest_path + '/slave_audio{stream}.mp3').format(stream=s_stream)
            _slave_trimmed_track_path = (_dest_path + '/slave_audio_trimmed{stream}').format(stream=s_stream)
            ffmpeg.trim_audio(path=_slave_audio_track, dest=_slave_trimmed_track_path, _from=_subs,
                              _to=_master_duration, debug=debug, quiet=quiet, overwrite=overwrite)

            _slave_trimmed_track = (_dest_path + '/slave_audio_trimmed{stream}.mp3').format(stream=s_stream)
            _rebuilded_master_path = _dest_path + '/rebuilded_master_file'

            ffmpeg.inyect_audio_c(path=_master_path, apath=_slave_trimmed_track, dest=_rebuilded_master_path,
                                  master=True, debug=True, quiet=quiet, overwrite=overwrite)
        if _add != 0:
            if debug:
                print 'FFClient concating and trimming slave_audio_track ...'
            _slave_audio_track = (_dest_path + '/slave_audio{stream}.mp3').format(stream=s_stream)
            _slave_silent_track_path = (_dest_path + '/slave_audio_silence{stream}').format(stream=s_stream)

            # Create a silence at the begining of the audio file to displace
            ffmpeg.create_silence_track(dest=_slave_silent_track_path, duration=_add,
                                        params=audio_presets['mp3-preset'], debug=debug, quiet=quiet,
                                        overwrite=overwrite)
            _slave_silent_track = (_dest_path + '/slave_audio_silence{stream}.mp3').format(stream=s_stream)
            _slave_combined_track_path = (_dest_path + '/slave_audio_combined{stream}').format(stream=s_stream)

            # Concant the early track with the original to make a new combined track
            ffmpeg.concat_audio_tracks( track0=_slave_silent_track, track1=_slave_audio_track,
                                        dest=_slave_combined_track_path, params=audio_presets['mp3-preset'],
                                        debug=debug, quiet=quiet, overwrite=overwrite)
            _slave_combined_track = (_dest_path + '/slave_audio_combined{stream}.mp3').format(stream=s_stream)
            _slave_trimmed_track_path = (_dest_path + '/slave_audio_trimmed{stream}').format(stream=s_stream)

            # Trim the audio to fit in the containter
            ffmpeg.trim_audio(path=_slave_combined_track, dest=_slave_trimmed_track_path, _from=_subs,
                              _to=_master_duration, debug=True, quiet=quiet, overwrite=overwrite)
            _slave_trimmed_track = (_dest_path + '/slave_audio_trimmed{stream}.mp3').format(stream=s_stream)
            _rebuilded_master_path = _dest_path + '/rebuilded_master_file'

            # Inyect the new audio in the container
            ffmpeg.inyect_audio_c(path=_master_path, apath=_slave_trimmed_track, dest=_rebuilded_master_path,
                                  master=True, debug=True, quiet=quiet, overwrite=overwrite)
        return

    def metadata(self):
        # validate path
        # get-metada if relevant
        # get general if not relevant
        return

    def enconde_file(self):
        # validate path
        # encode
        return

    def add_metadata_tag(self):
        # validate path
        # decompose params to call function
        return

    def add_audio_track(self):
        # validate path
        # decompose params to call function
        return

    def add_subtitle_track(self):
        # validate path
        # decompose params to call function
        return

    def extract_audio_track(self, path, dest, params, debug=False):
        # validate path
        # decompose params to call function
        return

    def extract_subtitle_track(self, map):
        # validate path
        # decompose params to call function
        return

    def extract_metadata_tag(self, map):
        # validate path
        # decompose params to call function
        return


