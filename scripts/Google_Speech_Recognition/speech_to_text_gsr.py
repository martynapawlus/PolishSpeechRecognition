# Inspired by: Jakub Nawała <jnawala@agh.edu.pl>

import speech_recognition as sr
import glob
import os
import json

# Create a config file with your own configuration in config_file_dev.json config file
config_file_name = "config_file_dev2.json"

with open(config_file_name, 'r') as json_data_file:
    configuration = json.load(json_data_file)

print("################################")
# print(configuration)
print("################################")

fileset = [file for file in glob.glob(configuration["audio_files"]["folder_with_audio_files"] + "**/*.wav", recursive=True)]

for file in fileset:
    print(file)
    # use the audio file as the audio source
    r = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = r.record(source)  # read the entire audio file

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        without_extra_slash = os.path.normpath(file)
        last_part = os.path.basename(without_extra_slash)
        last_part.split(".")
        file_name = last_part.split(".")[0]
        file_name_trn = file_name + ".trn"
        print(file_name_trn)
        transcribed_file = configuration["transcribed_files"]["folder_with_transcribed_files"] + file_name_trn
        f = open( transcribed_file, "a", encoding="utf8")
        f.write( r.recognize_google(audio, language="pl"))

        # Adding (Speaker 1) which is required in sclite
        f = open( transcribed_file, "r+")
        lines = f.readlines()
        f.close()
        keep = []
        for line in lines:
            if not line.isspace():
                keep.append(line.replace("\n", ""))
        fh = open( transcribed_file, "w")
        fh.write("".join(keep))
        fh.write("    (Speaker 1)\n")
        fh.close()


    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
