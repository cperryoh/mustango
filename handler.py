import os
import json
import base64
import requests
import runpod
import soundfile as sf
from mustango import Mustango
import base64
def encode_wav_to_base64(wav_file_path):
    with open(wav_file_path, "rb") as wav_file:
        wav_data = wav_file.read()
        encoded_string = base64.b64encode(wav_data).decode('utf-8')
        return encoded_string
def handler(event):
    job_input = event["input"]
     if "prompt" not in job_input:
        return {"error": "No prompt provided"}
    model = Mustango("declare-lab/mustango")

    prompt = "This is a new age piece. There is a flute playing the main melody with a lot of staccato notes. The rhythmic background consists of a medium tempo electronic drum beat with percussive elements all over the spectrum. There is a playful atmosphere to the piece. This piece can be used in the soundtrack of a children's TV show or an advertisement jingle."

    music = model.generate(prompt)
    sf.write(f"music.wav", music, samplerate=16000)
    data=encoded_wav_to_base64("music.wav")
    if "prompt" not in job_input:
        return {"audio": data}


runpod.serverless.start({"handler": handler})
