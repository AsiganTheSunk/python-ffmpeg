.PHONY: clean run

run:
	python main.py

clean:
	rm -f /home/asigan/python-ffmpeg/test/OutputSampleSubtitles.ass
	rm -f /home/asigan/python-ffmpeg/test/OutputSampleAudio.mp3
	rm -f /home/asigan/python-ffmpeg/test/OutputSampleVideo.mkv
	rm -f /home/asigan/python-ffmpeg/test/OutputMetadata.txt


