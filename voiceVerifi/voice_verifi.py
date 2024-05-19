import pyaudio
import wave
import librosa
import numpy as np
from sklearn import svm
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

def record_audio(filename, duration=5, fs=44100):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=fs,
                    input=True,
                    frames_per_buffer=1024)
    frames = []

    print("Recording...")
    for _ in range(0, int(fs / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)
    print("Recording finished")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

def extract_features(filename):
    y, sr = librosa.load(filename, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfccs_mean = np.mean(mfccs, axis=1)
    return mfccs_mean

def train_model():
    # Dummy dataset (replace with actual features and labels)
    X = np.array([[1, 2], [2, 3], [3, 4], [5, 6]])  # feature vectors
    y = np.array([0, 0, 1, 1])  # labels (0: target speaker, 1: others)

    # Use a pipeline with StandardScaler and SVM for better performance
    clf = make_pipeline(StandardScaler(), svm.SVC(probability=True))
    clf.fit(X, y)
    return clf

def verify_voice(model, filename):
    features = extract_features(filename).reshape(1, -1)
    proba = model.predict_proba(features)[0][0]

    if proba > 0.5:
        print("Voice verified")
    else:
        print("Voice not verified")

if __name__ == "__main__":
    # Record a new sample
    filename = "test.wav"
    record_audio(filename)

    # Extract features and train the model
    model = train_model()

    # Verify the recorded voice
    verify_voice(model, filename)
