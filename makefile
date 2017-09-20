.PHONY: clean run

run:
    clean
	python main.py

clean:
	rm -f /home/asigan/python-ffmpeg/test/*.srt
	rm -f /home/asigan/python-ffmpeg/test/*.ass
	rm -f /home/asigan/python-ffmpeg/test/*.mp3
	rm -f /home/asigan/python-ffmpeg/test/*.json


