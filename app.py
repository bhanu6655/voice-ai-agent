from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

from services.stt import speech_to_text
from services.agent import process_text
from services.tts import text_to_speech

import shutil
import time

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.post("/voice")

async def voice_chat(audio: UploadFile = File(...)):

    start_time = time.time()

    input_path = "audio/input.wav"

    with open(input_path, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)

    # Speech To Text
    text = speech_to_text(input_path)

    # AI Agent
    response_text, language = process_text(text)

    # Text To Speech
    audio_path = text_to_speech(response_text, language)

    latency = time.time() - start_time

    print(f"Latency: {latency:.2f} sec")

    return FileResponse(
        audio_path,
        media_type="audio/mpeg"
    )