.PHONY: clean run

run:
	clean
	python main.py

clean:
	rm -f /home/asigan/python-ffmpeg/test/samples/NewSampleMultiAS.mkv
	rm -f /home/asigan/python-ffmpeg/test/samples/*.srt
	rm -f /home/asigan/python-ffmpeg/test/samples/*.ass
	rm -f /home/asigan/python-ffmpeg/test/samples/*.mp3
	rm -f /home/asigan/python-ffmpeg/test/samples/*.json


