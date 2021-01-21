from sklearn import svm
from pycm import *
from os import walk
import librosa 
import numpy as np
import pickle
import os.path
import warnings 
warnings.filterwarnings('ignore')

def feature_extraction(folder):
    print("dkhalna extrcat ***************************************")
    hop_length = 512
    n_fft = 2048
    n_mels = 128
    labels = {'blues': 0, 'classical': 1, 'country': 2, 'disco': 3, 'hiphop': 4, 'jazz': 5,'metal': 6, 'pop': 7, 'reggae': 8, 'rock': 9}
    a = []
    b = []
    for nametype in list(labels.keys()):
        _wavs = []
        wavs_duration = []
        for (_,_,filenames) in walk(folder+nametype+"/"):
            _wavs.extend(filenames)
            break
        Mel_Spectrogram = []
        for _wav in _wavs:
            if(".wav" in _wav): 
                file = folder +nametype+"/"+_wav
                signal, rate = librosa.load(file)  
                S = librosa.feature.melspectrogram(signal, sr=rate, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)
                S_DB = librosa.power_to_db(S, ref=np.max)
                S_DB = S_DB.flatten()[:1200]
                a.append(S_DB)
                b.append(labels[nametype])

    print("khrajna men extract**************************************************")
    return a, b

def predict_genres(soundfile,clf):
    
    print('dkhalna predict_genres +++++++++++++++++++++++++++++++++++++++++++++++')

    hop_length = 512
    n_fft = 2048
    n_mels = 128
    types = {0: 'blues', 1: 'classical', 2: 'country', 3: 'disco', 4: 'hiphop', 5: 'jazz', 6: 'metal', 7: 'pop', 8: 'reggae', 9: 'rock'}  
    signal, rate = librosa.load(soundfile)  
    S = librosa.feature.melspectrogram(signal, sr=rate, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)
    S_DB = librosa.power_to_db(S, ref=np.max)
    S_DB = S_DB.flatten()[:1200]
    y_pred = clf.predict([S_DB])[0]

    print("khrajna men predict_genres+++++++++++++++++++++++++++++++++++++++++++++")
    return types[y_pred]  
	
	
##############################
def predict(fileName):

    #fileName = '/home/fekher-nouioui/Downloads/Dataset_projet_docker/rock.00099.wav'
    #folder = "/home/fekher-nouioui/Downloads/Dataset_projet_docker/genres_original_2/"
    
    folder = "./../genres_original_2/"

    x,y = feature_extraction(folder)



    clf = svm.SVC()
    clf = svm.SVC(kernel="rbf")
    clf.fit(x,y)	

    result = predict_genres(fileName,clf)

    return(result)


