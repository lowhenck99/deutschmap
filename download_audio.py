import json
import os
from gtts import gTTS

# Créer le dossier audio s'il n'existe pas
if not os.path.exists('audio'):
    os.makedirs('audio')

# Charger le fichier de vocabulaire
with open('vocabulary.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Parcourir les niveaux (A1, A2, etc.)
for level, words_dict in data.items():
    if isinstance(words_dict, dict):
        for german_text, translation in words_dict.items():
            # Nettoyer le nom du fichier audio
            clean_name = german_text.replace(" ", "_").replace("/", "_").replace("?", "").replace("!", "").lower()
            filename = f"{clean_name}.mp3"
            filepath = os.path.join('audio', filename)

            if not os.path.exists(filepath):
                print(f"Téléchargement [{level}] : {german_text} -> {filename}")
                try:
                    tts = gTTS(text=german_text, lang='de')
                    tts.save(filepath)
                except Exception as e:
                    print(f"Erreur pour '{german_text}': {e}")

print("Téléchargement de tous les audios terminé !")