import streamlit as st
from google import genai
import os , io
from dotenv import load_dotenv
from gtts import gTTS



load_dotenv()

my_api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=my_api_key)


def note_genarator(images):

    prompt = """Summarize the picture in note format at maz 100 words, 
    make sure to add necessary markdown to differentiate different section"""

    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[images,prompt]
)
    return response.text


def audio_transcription(text):
    speech = gTTS(text,lang = 'en',slow = False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    return audio_buffer

def quiz_generator(image,difficulty):
    prompt = f"""Generated 3 quizzes based on the {difficulty}. 
    Make sure to add markdown to differentiate the option,add correct answer too after the quiz"""

    response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[image,prompt]
)
    return response.text



