from settings import MODEL_DIR
import streamlit as st
#from keras.models import load_model
from app import ReadAudio
import librosa, os
import numpy as np

all_label = ["ka", "kha", "ga", "gha", "nga"]
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
y = le.fit_transform(all_label)
classes = list(le.classes_)

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# model = load_model(MODEL_DIR)

class PredAudio:
	def pred(audio):
		#resampling the recorded audio
		samples, sample_rate = librosa.load(audio, sr=16000)
		st.write('Samples: ', samples)
		st.write('Sample rate: ', sample_rate)
		samples = librosa.resample(samples, sample_rate, 8000)
		samples = np.array(samples).reshape(-1,8000,1)

		#predicting audio
		prob = model.predict(audio.reshape(-1,8000,1))
		index = np.argmax(prob[0])
		char = classes[index]
		st.write("Text: ", char)

