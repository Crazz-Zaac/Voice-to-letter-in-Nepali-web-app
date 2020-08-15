import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# OUT_DIR = os.path.join(ROOT_DIR, 'output/')
RECORDING_DIR = os.path.join(ROOT_DIR, 'recording')
IMAGE_DIR = os.path.join(ROOT_DIR, 'images')
CSS_DIR = os.path.join(ROOT_DIR, 'css')

DEFAULT_SAMPLE_RATE = 16000
MAX_INPUT_CHANNELS = 1
WAVE_OUTPUT_FILE = os.path.join(RECORDING_DIR, "recorded.wav")

# READ_FILE = os.path.join(RECORDING_DIR, "recorded.wav")

DURATION = 1 #1 second
CHUNK_SIZE = 1000