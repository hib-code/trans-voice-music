from audio_processing import load_audio_file, process_voice, extract_music_features
from transformation import match_voice_to_music, combine_music_and_voice
import librosa

# Charger la musique
music_path = 'audio/music.mp3'
y_music, sr_music = load_audio_file(music_path)

# Charger et traiter la voix
voice_path = 'audio/voice.mp3'
y_voice, sr_voice = process_voice(voice_path)

# Extraire les caractéristiques de la musique
tempo, pitches = extract_music_features(y_music, sr_music)

# Transformer la voix pour correspondre à la musique
transformed_voice = match_voice_to_music(y_voice, pitches, sr_voice)

# Combiner la musique et la voix transformée
combined_audio = combine_music_and_voice(y_music, transformed_voice, sr_music)

# Sauvegarder le fichier final
librosa.output.write_wav("final_output.wav", combined_audio, sr_music)

print("Transformation terminée. Le fichier final est enregistré sous 'final_output.wav'.")
