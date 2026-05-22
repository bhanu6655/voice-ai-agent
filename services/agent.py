import os

from groq import Groq
from dotenv import load_dotenv

from services.db import book_appointment
from services.memory import add_memory, get_memory
from utils.language import detect_language

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def process_text(text):

    print("RUNNING NEW AGENT FILE")

    add_memory("user", text)

    language = detect_language(text)

    history = get_memory()

    memory_text = ""

    for item in history:
        memory_text += f"{item['role']}: {item['message']}\n"

    prompt = f"""
    You are a multilingual hospital assistant.

    Conversation:
    {memory_text}

    User:
    {text}

    Reply briefly.
    """

    print("USING MODEL: llama-3.1-8b-instant")

    completion = client.chat.completions.create(

        model="llama-3.1-8b-instant",

        messages=[
            {
                "role": "system",
                "content": "You are a hospital assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.7,
        max_tokens=100
    )

    ai_response = completion.choices[0].message.content

    text_lower = text.lower()

    if "book" in text_lower:

        doctor = "General Doctor"

        if "dentist" in text_lower:
            doctor = "Dentist"

        elif "cardio" in text_lower:
            doctor = "Cardiologist"

        book_appointment(
            patient="Bhanu",
            doctor=doctor,
            date="Tomorrow"
        )

    add_memory("assistant", ai_response)

    return ai_response, language