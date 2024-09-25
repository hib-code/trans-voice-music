import librosa

# Modifier la hauteur de la voix pour correspondre à la musique
def match_voice_to_music(y_voice, pitches, sr_voice):
    pitch_shifted_voice = librosa.effects.pitch_shift(y_voice, sr_voice, n_steps=2)
    return pitch_shifted_voice

# Combiner la musique et la voix
def combine_music_and_voice(y_music, y_voice_transformed, sr):
    combined_audio = y_music * 0.5 + y_voice_transformed * 0.5  # Ajustement du volume
    return combined_audio
