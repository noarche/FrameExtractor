import os

# Set the path to FFmpeg
os.environ['PATH'] = 'C:/Users/block/ffmpeg/bin' + os.pathsep + os.environ['PATH']

# Add the following line to the scripts that need to use ffmpeg:
# from ffmpeg_path import *
