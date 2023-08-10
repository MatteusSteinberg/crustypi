from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import time
from os import path, makedirs

picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

folder = 'videos'

def capture_video(duration: int, timestamp: str):

    if not path.exists(folder):
      makedirs(folder)

    encoder = H264Encoder(10000000)
    output = FfmpegOutput(f'{folder}/{timestamp}.mp4', audio=True)

    picam2.start_recording(encoder, output)
    time.sleep(duration)
    picam2.stop_recording()

    return