from gtts import gTTS

def text_to_speech(text, lang="en"):

    tts = gTTS(text=text, lang=lang)

    output_path = "audio/output.mp3"

    tts.save(output_path)

    return output_path