import sys, os
import subprocess
import time

if len(sys.argv) != 3:
	print 'usage: {} [video_list_file] [download_destination]'.format(sys.argv[0])
	sys.exit()

VIDEO_LIST_FILE = sys.argv[1]
VIDEO_DOWNLOAD_DEST = sys.argv[2]
VIDEO_FAILED_DOWNLOAD_FILE = './failed_download'

if os.path.isfile(VIDEO_FAILED_DOWNLOAD_FILE):
	print 'plz remove {} first and restart'.format(VIDEO_FAILED_DOWNLOAD_FILE)
	sys.exit()
else:
	f_failed = open(VIDEO_FAILED_DOWNLOAD_FILE, 'w')

with open(VIDEO_LIST_FILE, 'r') as f_in:
	for video in f_in:
		video = video.replace('\n', '')
		video_saving_path = os.path.join(VIDEO_DOWNLOAD_DEST, video+'.mp4')
		video_url = 'https://www.youtube.com/watch?v=' + video
		if os.path.isfile(video_saving_path):
			continue
		command = 'youtube-dl -f best -f mp4 {} -o {}'.format(video_url, video_saving_path)
		print command
		subprocess.call(command.split())
		if not os.path.isfile(video_saving_path):
			f_failed.write(command+'\n')
		else:
			time.sleep(3)


