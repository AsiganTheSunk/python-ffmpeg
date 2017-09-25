#!/usr/bin/env python

presets = {'default-preset':{'crf':'18',
                             'preset':'slow',
                             'audio':'flac',
                             'kbitrate-audio':'320k',
                             'threads':'2'} ,
           'movie-preset':{'crf':'18',
                             'preset':'slow',
                             'audio':'flac',
                             'kbitrate-audio':'320k',
                             'threads':'2'} ,
           'show-preset':{'crf':'18',
                             'preset':'slow',
                             'audio':'flac',
                             'kbitrate-audio':'320k',
                             'threads':'2'} ,
           'anime-preset':{'crf':'18',
                             'preset':'slow',
                             'audio':'flac',
                             'kbitrate-audio':'320k',
                             'threads':'2'}
           }


audio_presets = {'mp3-preset':{'audio':'mp3',
                               'sampling-rate':'44100',
                               'channels':'2',
                               'kbitrate-audio':'320k',
                               'threads':'2'},

                'flac-preset':{'audio':'flac',
                               'sampling-rate':'44100',
                               'channels':'2',
                               'kbitrate-audio':'320k',
                               'threads':'2'},

                'aac-preset':{'audio':'aac',
                              'sampling-rate':'44100',
                              'channels':'2',
                              'kbitrate-audio':'320k',
                              'threads':'2'},

                'wav-mono-preset':{'audio':'wav',
                                   'sampling-rate':'44100',
                                   'channels':'1',
                                   'kbitrate-audio':'320k',
                                   'threads':'2'}
                }

subtitle_presets = {'srt-preset':{'subtitle':'srt',
                                  'threads':'1'},
                    'ass-preset':{'subtitle':'ass',
                                  'threads': '1'}
                    }

