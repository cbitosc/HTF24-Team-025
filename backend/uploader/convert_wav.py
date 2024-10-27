import azure.cognitiveservices.speech as speechsdk
import os
from moviepy.editor import AudioFileClip
import spacy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import threading

# Load the SpaCy model
nlp = spacy.load("en_core_web_md")

def mp4_to_wav(mp4_file_path, wav_file_path):
    os.makedirs(os.path.dirname(wav_file_path), exist_ok=True)
    audio_clip = AudioFileClip(mp4_file_path)
    audio_clip.write_audiofile(wav_file_path, codec='pcm_s16le')
    audio_clip.close()

# Function to transcribe long audio using recognize_continuous
def transcribe_audio(audio_file_path):
    subscription_key = "AZURE_SUBSCRIPTION_KEY"
    region = "YOUR_REGION"

    speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=region)
    audio_config = speechsdk.audio.AudioConfig(filename=os.path.abspath(audio_file_path))
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    # Continuous transcription result storage
    all_text = []
    done = threading.Event()

    def handle_result(evt):
        all_text.append(evt.result.text)

    def handle_session_stop(evt):
        print("Transcription session stopped.")
        done.set()

    speech_recognizer.recognized.connect(handle_result)
    speech_recognizer.session_stopped.connect(handle_session_stop)

    # Start continuous recognition
    print("Transcription started...")
    speech_recognizer.start_continuous_recognition()
    done.wait()  # Wait until transcription is done
    speech_recognizer.stop_continuous_recognition()

    return " ".join(all_text)

def summarize_text(text, num_sentences=20):
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    sentence_vectors = np.array([doc[sent.start:sent.end].vector for sent in doc.sents])
    similarity_matrix = cosine_similarity(sentence_vectors)
    scores = similarity_matrix.sum(axis=1)
    ranked_sentences = [sentences[i] for i in np.argsort(scores, axis=0)[-num_sentences:]]
    return ' '.join(ranked_sentences)



def convert_wav(mp4_file,wav_file):
    try:
        # Step 1: Convert MP4 to WAV
        mp4_to_wav(mp4_file, wav_file)
        
        # Step 2: Transcribe Audio
        transcribed_text = transcribe_audio(wav_file)
        
        # Step 3: Summarize Text if transcription is successful
        if transcribed_text:
            return summarize_text(transcribed_text)
    except Exception as e:
        print(f"Main error: {str(e)}")



# Example usage
# mp4_file = r'C:\Diploma++\CBIT\Hacktober 24\PS15\final\HTF24-Problem Statement Website Demo.mp4'  # Replace with your MP4 file path
# wav_file = r'C:\Diploma++\CBIT\Hacktober 24\PS15\final\output.wav'  # ReplF24-Problem Statement Websace with the desired WAV file path

# convert_wav(mp4_file,wav_file)