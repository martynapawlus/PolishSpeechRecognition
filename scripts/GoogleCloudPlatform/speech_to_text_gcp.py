
import os
from google.cloud import speech
from google.cloud import storage
import json

# Create a config file with your own configuration in config_file_dev.json config file
config_file_name = "config_file_dev.json"

with open(config_file_name, 'r') as json_data_file:
    configuration = json.load(json_data_file)

print("################################")
# print(configuration)
print("################################")

# credential_path should have your path to .json configuration file
json_credential_path = configuration["json_file"]["json_file_path"]
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = json_credential_path


def transcribe_gcs(gcs_uri):

    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="pl-PL",
        enable_word_time_offsets=True,
        enable_automatic_punctuation=True,
    )

    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result()

    #Extracting a name of a transcribed file with .trn extension
    without_extra_slash = os.path.normpath(gcs_uri)
    last_part = os.path.basename(without_extra_slash)
    last_part.split(".")
    file_name = last_part.split(".")[0]
    file_name_trn = file_name + ".trn"

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    path = configuration["transcribed_files"]["transcribed_files_dir"] + file_name_trn
    for result in response.results:
        with open(path, "a", encoding="utf8") as f:
            f.write(result.alternatives[0].transcript)

    #Adding (Speaker 1) which is required in sclite
    f = open(path, "r+")
    lines = f.readlines()
    f.close()
    keep = []
    for line in lines:
        if not line.isspace():
            keep.append(line.replace("\n", ""))
    fh = open(path, "w")
    fh.write("".join(keep))
    fh.write("    (Speaker 1)\n")
    fh.close()

    return response

#Usage of a google cloud storage
client = storage.Client()
for blob in client.list_blobs(configuration["gc_storage"]["bucket_name"], prefix=configuration["gc_storage"]["dir_name"]):
    print(str(blob.name))
    file_url = configuration["gc_storage"]["bucket_url"] + str(blob.name)
    transcribe_gcs(file_url)

print("####################################################################################")
print("PROGRAM END")
print("####################################################################################")
print("Thank you for using this code")
