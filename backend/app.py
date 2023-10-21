import os
from fastapi import FastAPI, WebSocket, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from backend.templates import *  # Make sure to import this module if necessary
from backend.bot.bot import *

templates = Jinja2Templates(directory="templates")

app = FastAPI()
user_messages = []

origins = [
    "https://lluminaries.serveo.net",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        user_message = await websocket.receive_text()
        print(user_message)
        user_messages.append(user_message)
        response = chatbot_response(user_message)
        await websocket.send_text(response)

def chatbot_response(user_input):
    bot = Bot(200)
    response = bot.generate(user_input)
    print(response)
    return response

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
