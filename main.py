#!/usr/bin/env python
from ffmpeg.FFMpeg import FFMpeg
from ffmpeg.FFProbe import FFProbe
import select
from ffmpeg.config import audio_presets, subtitle_presets
from ffmpeg.Metadata import ExtendedMetadata
from ffmpeg.FFClient import FFClient

# 0.6734

import os
import subprocess
import json

def main():
    mkv_simple_source = str(os.getcwd()) + '/test/samples/SampleVideo.mkv'
    mkv_multi_source = str(os.getcwd()) + '/test/samples/SampleMultiAS.mkv'



    subtitle_output_dest = str(os.getcwd()) + '/test/samples/SampleSubtitleOutput'
    audio_output_dest = str(os.getcwd()) + '/test/samples/SampleAudioTestOutput'
    video_output_dest = str(os.getcwd()) + '/test/samples/SampleVideoTestOutput'
    silence_dest = str(os.getcwd()) + '/test/samples/SilenceAudioTrack'
    combined_output = str(os.getcwd()) + '/test/samples/CombinedAudioTrack'
    wasabi_eng = '\'/media/asigan/1AD0F286D0F26801/WASABI Test/Wasabi.2001.1080p.BluRay.DTS.x264-CRiSC [PublicHD]/Wasabi.2001.1080p.BluRay.DTS.x264-CRiSC.mkv\''
    wasabi_spa = '\'/media/asigan/1AD0F286D0F26801/WASABI Test/Wasabi[HDrip][Spanish][www.lokotorrents.com]/Wasabi[HDrip][Spanish][www.lokotorrents.com].avi\''

    ffmpeg = FFMpeg()

    path = '\'/media/asigan/1AD0F286D0F26801/Osmosis Jones.720p.(Spa2.0)(Eng5.1).mkv\''
    dest = '\'/media/asigan/1AD0F286D0F26801/audio_samples/osmosis_audio_testb\''


    # TODO FUTURE TEST SINGLE AUDIO EXTRACT
    # params = audio_presets['wav-mono-preset']
    #ffmpeg.extract_audio(path=mkv_multi_source, dest=audio_output_dest, stream=0, debug=True, quiet=True, overwrite=False)
    # ffmpeg.extract_audio(path=mkv_multi_source, dest=audio_output_dest, params=params, stream=0, debug=True, quiet=False, overwrite=False)

    # TODO FUTURE TEST SINGLE SUBTITLE EXTRACT
    #ffmpeg.extract_subtitle(path=mkv_multi_source, dest=subtitle_output_dest, stream=0, debug=True, quiet=False, overwrite=False)

    # TODO FUTURE TEST ALL AUDIO EXTRACT
    #ffmpeg.extract_all_audio(path=mkv_multi_source, dest=audio_output_dest, debug=True, quiet=False, overwrite=False)

    # TODO FUTURE TEST ALL SUBTITLE EXTRACT
    #ffmpeg.extract_all_subtitles(path=mkv_multi_source, dest=subtitle_output_dest, debug=True, quiet=False, overwrite=False)

    # TODO FUTURE TEST SINGLE SUBTITLE INYECT
    #ffmpeg.inyect_subtitle(path=mkv_multi_source, spath=str(subtitle_output_dest + '0.srt'), dest= video_output_dest, debug=True, quiet=False, overwrite=False)

    # TODO FUTURE TEST SINGLE AUDIO INYECT
    #ffmpeg.inyect_audio_c(path=mkv_multi_source, apath=str(audio_output_dest + '0.mp3'), dest=video_output_dest, master=False, debug=True, quiet=False, overwrite=True)

    # TODO FUTURE TEST METADATA INYECT
    #metadata = ExtendedMetadata(name='The Lord Yisus', ename='', season='', episode='', quality='', extension='', uploader='',
    #                 source='', year='', film_flag='', language='', subtitle='', fflag='',
    #                 director='', actors='', genre='Fantasy & Dragons', duration='', chapters='')

    #ffmpeg.inyect_metadata(path=mkv_multi_source, dest=video_output_dest, metadata=metadata, debug=True, overwrite=True)

    # TODO FUTURE TEST FFPROBE
    #ffprobe = FFProbe(video_output_dest + '.mkv')
    #ffprobe.get_general_metadata()

    # TODO FUTURE TEST CONVERT SRT TO ASS
    #ffmpeg.convert_srt_to_ass(path=subtitle_output_dest+'0.srt', dest=subtitle_output_dest, debug=True)

    # TODO FUTURE TEST CREATE SILENCE
    #ffmpeg.create_silence_track(dest=silence_dest, duration=0.6734, debug=True)

    #ffprobe = FFProbe('/media/asigan/1AD0F286D0F26801/audio_samples/osmosis_silence.mp3')
    #ffprobe.get_general_metadata()

    # TODO FUTURE TEST SILENCE SILENCE
    # ffmpeg.concat_audio_tracks(track0=(silence_dest + '.mp3'), track1=(audio_output_dest + '0.mp3'), dest=combined_output, debug=True)

    osmosis_source = '/media/asigan/1AD0F286D0F26801/audio_samples/osmosis_audio_testb1.mp3'
    osmosis_output = '/media/asigan/1AD0F286D0F26801/audio_samples/audio_shorter_test'
    #ffmpeg.trim_audio(path=osmosis_source, dest=osmosis_output, _from=0.6734, _to=5720.477000, debug=True)

    osmosis_output_dest = '/media/asigan/1AD0F286D0F26801/osmosis_audio_delayed_test-new'
    osmosis_source_2 = '/media/asigan/1AD0F286D0F26801/Osmosis.Jones.2001.1080p.HDTV.x264.DD5.1-FGT/Osmosis.Jones.2001.1080p.HDTV.x264.DD5.1-FGT.mkv'

    #ffmpeg.inyect_audio(path=osmosis_output_dest+'cuarto.mkv', apath='/media/asigan/1AD0F286D0F26801/audio_samples/osmosis_audio_test0.mp3', dest=osmosis_output_dest+'DUAL')
    #ffmpeg.inyect_audio_c(path=osmosis_source_2, apath= osmosis_output + '.mp3', dest=osmosis_output_dest+'testtuto3', master=True)

    # ffprobe = FFProbe(osmosis_output_dest+'cuarto.mkv')
    # ffprobe.get_general_metadata()
    # ffprobe = FFProbe(osmosis_output_dest+'DUAL.mkv')
    # ffprobe.get_general_metadata()

    # ffmpeg -y -i '/media/asigan/1AD0F286D0F26801/WASABI Test/Wasabi.2001.1080p.BluRay.DTS.x264-CRiSC [PublicHD]/Wasabi.2001.1080p.BluRay.DTS.x264-CRiSC.mkv' -vn -ar 44100 -ac 1 -ab 320k -f wav '/media/asigan/1AD0F286D0F26801/wasabi_audio_test_eng.wav'
    # ffmpeg -y -i '/media/asigan/1AD0F286D0F26801/WASABI Test/Wasabi[HDrip][Spanish][www.lokotorrents.com]/Wasabi[HDrip][Spanish][www.lokotorrents.com].avi' -vn -ar 44100 -ac 1 -ab 320k -f wav '/media/asigan/1AD0F286D0F26801/wasabi_audio_test_esp.wav'
    # ffmpeg -y -i '/media/asigan/1AD0F286D0F26801/Osmosis.Jones.2001.1080p.HDTV.x264.DD5.1-FGT/Osmosis.Jones.2001.1080p.HDTV.x264.DD5.1-FGT.mkv'   -vn -ar 44100 -ac 1 -ab 320k -f wav '/media/asigan/1AD0F286D0F26801/osmosis_audio_test_eng.wav'
    # ffmpeg -y -i '/media/asigan/1AD0F286D0F26801/Osmosis Jones.720p.(Spa2.0)(Eng5.1).mkv' -map 0:a:1 -vn -ar 44100 -ac 1 -ab 320k -f mp3 '/media/asigan/1AD0F286D0F26801/osmosis_audio_test_esp.mp3'

    ffclient = FFClient()
    # ffclient.sync_audio_tracks(master='/media/asigan/1AD0F286D0F26801/OsmosisTest/Osmosis.Jones.2001.1080p.HDTV.x264.DD5.1-FGT/Osmosis.Jones.2001.1080p.HDTV.x264.DD5.1-FGT.mkv',
    #                           slave='/media/asigan/1AD0F286D0F26801/OsmosisTest/Osmosis Jones.720p.(Spa2.0)(Eng5.1).mkv',
    #                           dest='/media/asigan/1AD0F286D0F26801/osmosis_test',
    #                           m_stream=0, s_stream=1, debug=True, quiet=True, overwrite=True)

    # ffclient.sync_audio_tracks(master='/media/asigan/1AD0F286D0F26801/OsmosisTest/Osmosis Jones.720p.(Spa2.0)(Eng5.1).mkv',
    #                           slave = '/media/asigan/1AD0F286D0F26801/OsmosisTest/Osmosis.Jones.2001.1080p.HDTV.x264.DD5.1-FGT/Osmosis.Jones.2001.1080p.HDTV.x264.DD5.1-FGT.mkv',
    #                           dest='/media/asigan/1AD0F286D0F26801/real_test',
    #                           m_stream=0, s_stream=0, debug=False, quiet=False, overwrite=False)

    # ffclient.sync_audio_tracks(
    #     master='/media/asigan/1AD0F286D0F26801/PulpFiction/Pulp.Fiction.1994.720p.BluRay.H264.AAC-RARBG/Pulp.Fiction.1994.720p.BluRay.H264.AAC-RARBG.mp4',
    #     slave='/media/asigan/1AD0F286D0F26801/PulpFiction/Pulp.Fiction.DVD+VHS.Galego.by.XibaD.[www.ProxectoMeiga.co.nr].ogm',
    #     dest='/media/asigan/1AD0F286D0F26801/pulp_test',
    #     m_stream=0, s_stream=0, debug=False, quiet=True, overwrite=False)

    ffclient.sync_audio_tracks(
        master='/media/asigan/1AD0F286D0F26801/WasabiTest/Wasabi.2001.1080p.BluRay.DTS.x264-CRiSC [PublicHD]/Wasabi.2001.1080p.BluRay.DTS.x264-CRiSC.mkv',
        slave='/media/asigan/1AD0F286D0F26801/WasabiTest/Wasabi[HDrip][Spanish][www.lokotorrents.com]/Wasabi[HDrip][Spanish][www.lokotorrents.com].avi',
        dest='/media/asigan/1AD0F286D0F26801/wasabi_test',
        m_stream=0, s_stream=0, debug=True, quiet=True, overwrite=False)


if __name__ == '__main__':
     main()

# TODO AQUI ESTO DE ABAJO FUNCIONA
# Cut the final seconds to match the lenght of the original audio
#ffmpeg -i '/media/asigan/1AD0F286D0F26801/audio_samples/osmosis_audio_testb1.mp3' -ss 0.6734 -to 5720.477000 -c copy '/media/asigan/1AD0F286D0F26801/audio_samples/audio_shorter.mp3'

#ffmpeg -y -i '/media/asigan/1AD0F286D0F26801/osmosis_audio_delayed_test23413BBBBBB.mkv' -i '/media/asigan/1AD0F286D0F26801/audio_samples/osmosis_audio_test0.mp3' -map 0:v -map 0:a -map 1:a -map 0:s:? -c:v copy -c:a copy -c:s copy '/media/asigan/1AD0F286D0F26801/osmosis_audio_delayed_test23413BBBBBB_DUAL.mkv'
#ffmpeg -y -i '/media/asigan/1AD0F286D0F26801/Osmosis.Jones.2001.1080p.HDTV.x264.DD5.1-FGT/Osmosis.Jones.2001.1080p.HDTV.x264.DD5.1-FGT.mkv' -i '/media/asigan/1AD0F286D0F26801/audio_samples/audio_shorter.mp3' -map 0:v:? -map 1:0:? -map 0:s:? -c:v copy -c:a copy -c:s copy '/media/asigan/1AD0F286D0F26801/osmosis_audio_delayed_testNEWBRAND.mkv'

#ffprobe  -print_format json -show_entries streams -show_format '/media/asigan/1AD0F286D0F26801/osmosis_audio_delayed_test23413BBBBBB_DUAL.mkv'