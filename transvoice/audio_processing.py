import librosa
from pydub import AudioSegment

# Charger la musique
def load_audio_file(file_path):
    y, sr = librosa.load(file_path, sr=None)
    return y, sr

# Charger et traiter la voix
def process_voice(voice_path):
    voice = AudioSegment.from_file(voice_path)
    voice.export("processed_voice.wav", format="wav")
    y_voice, sr_voice = librosa.load("processed_voice.wav", sr=None)
    return y_voice, sr_voice

# Extraire les caractéristiques de la musique
def extract_music_features(y, sr):
    tempo, _ = librosa.beat.beat_track(y, sr=sr)
    pitches, magnitudes = librosa.core.piptrack(y=y, sr=sr)
    return tempo, pitches
