import os
print (os.environ['PYTHONPATH'])


import sys
print (sys.path)


import librosa
import soundfile
import os
import glob
import pickle
import numpy as np
from sklearn.model_selection import *
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def extract_feature(f_name, mfcc, chroma, mel):
    with soundfile.SoundFile(f_name) as sound_file:
        result = np.array([])
        x = sound_file.read(dtype="float32")
        sample_rate = sound_file.samplerate
        stft = np.abs(librosa.stft(x))
        if chroma:
            chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
        if mfcc:
            mfc_c = np.mean(librosa.feature.mfcc(y=x, sr=sample_rate, n_mfcc=40).T,axis=0)
        if mel:
            mel = np.mean(librosa.feature.melspectrogram(x, sr=sample_rate).T,axis=0)
        result = np.hstack((result, mfc_c))
        result = np.hstack((result, chroma))
        result = np.hstack((result, mel))
    return result


observed_emo=['calm','happy','fearful','disgust']


# dictionary definition
emotions = {'01':'neutral',
  '02':'calm',
  '03':'happy',
  '04':'sad',
  '05':'angry',
  '06':'fearful',
  '07':'disgust',
  '08':'surprised'
            };


def load_data(test_size=0.2):
    x,y=[],[]
    for file in glob.glob("dataset/speech-emotion-recognition-ravdess-data/Actor_*/*.wav"):
        f_name = os.path.basename(file)
        emotion = emotions[ f_name.split("-")[2] ]
        if emotion not in observed_emo:
            continue
        print(f_name)
        feature=extract_feature(file, mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    return train_test_split(np.array(x),y,test_size=test_size,random_state=9)


def main():
    x_train, x_test, y_train, y_test = load_data(test_size=0.1)
    print(x_train.shape[0],x_test.shape[0])
    print(x_train.shape[1])
    model=MLPClassifier(alpha=0.01,batch_size=256,epsilon=1e-08,hidden_layer_sizes=(300,),learning_rate='adaptive',max_iter=500)
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    print(y_pred)
    accuracy=accuracy_score(y_true=y_test,y_pred=y_pred)
    print(accuracy)
    pickle.dump(model,open('mymodel', 'wb'))
    return 0

def func(path):
    feat=[]
    feat.append(extract_feature(f_name=path, mfcc=True, chroma=True, mel=True))
    model=pickle.load(open('mymodel','rb'))
    pred_mood=model.predict(feat)
    if pred_mood[0]=='calm':
        return 0
    if pred_mood[0]=='happy':
        return 1
    if pred_mood[0]=='fearful':
        return 2
    if pred_mood[0]=='disgust':
        return 3


