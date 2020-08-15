import os, io, librosa
import numpy as np
import matplotlib.pyplot as plt
import IPython.display as ipd
import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment
import streamlit as st
from PIL import Image
from settings import IMAGE_DIR, DURATION, WAVE_OUTPUT_FILE, CSS_DIR
from scipy.io.wavfile import write

class ReadAudio: #reading the recorded audio
	def readAudio():
		try:
			audio_file = open(WAVE_OUTPUT_FILE, 'rb')
		except:
			st.write("Error reading file")

		return audio_file

class ExploreAudio: #for visualizing recorded audio
	def exploreAudio():
		rd_file = ReadAudio.readAudio()	
		samples, sample_rate = librosa.load(rd_file, sr=16000)
		st.write("Sample length: ", len(samples))
		st.write("Sample rate: ", sample_rate)
		st.write("Shape of the audio", np.shape(samples))
		fig = plt.figure(figsize=(14, 8))
		ax1 = fig.add_subplot(211)
		ax1.set_title('Raw wave of ' + 'recorded audio', fontsize=15)
		ax1.set_xlabel('time', fontsize=15)
		ax1.set_ylabel('Amplitude', fontsize=15)
		ax1.plot(np.linspace(0, sample_rate/len(samples), sample_rate), samples)
		st.pyplot()

def main():
	st.title("Voice to letter in Nepali Web App")
	st.sidebar.title("Voice to letter in Nepali")

	st.sidebar.subheader("Visualize recorded data")

	image = Image.open(os.path.join(IMAGE_DIR, 'mic.png'))
	st.subheader("Click on the record button and speak")
	st.image(image)

	
	if st.button('Record'):
		with st.spinner(f'Recording for {DURATION} seconds ...'):
			f_path = WAVE_OUTPUT_FILE
			fs = 16000
			seconds = 1
			recording = sd.rec(int(seconds*fs), samplerate = fs, channels = 1)
			sd.wait()
			write(f_path, fs, recording) #saving file 
		st.success('Recording completed')

	if st.button('Play'):
		try:
			audio_file = open(WAVE_OUTPUT_FILE, 'rb')
			audio_bytes = audio_file.read()
			st.audio(audio_bytes, format='audio/wav')

		except FileNotFound:
			st.write("Please record sound first")



	if st.sidebar.button("Audio info"):
		audio_file = open(WAVE_OUTPUT_FILE, 'rb')
		audio_bytes = audio_file.read()
		st.audio(audio_bytes, format='audio/wav')
		ExploreAudio.exploreAudio()




if __name__ == '__main__':
	main()

