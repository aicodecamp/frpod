import whisper
import timeit


# Function Summary
# trans: Transcribes an MP3 file using the Whisper model and saves the transcription to a text file.
def trans(mp3_file):
    models = whisper.available_models()
    print(models)
    model = whisper.load_model("large")
    result = model.transcribe(mp3_file, fp16=False, language='French')

    with open('t.txt' , 'w') as f:
        f.write(result['text'])


