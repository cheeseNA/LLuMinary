"""
FOR TESTING
"""

import os
import json

from bot.bot import Bot
from fastapi import FastAPI, Request, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import logging
import ast

templates = Jinja2Templates(directory="templates")

app = FastAPI()
user_messages = []

origins = [
    "*",
    "http://localhost:3000",
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
    print('ATTEMPTING TO CONNECT')
    await websocket.accept()
    print('CONNECTION ACCEPTED')
    # prev_convo = [
    #     {'role': 'user', 'content': 'my name is Robert'},
    #     {'role': 'assistant', 'content': 'Hello, my name is AI. How can I assist you today?'}]

    while True:
        logging.basicConfig(level=logging.INFO)
        bot = Bot(200)
        chat = True
        # prev_convo = await websocket.receive_text()
        # print(prev_convo)

        with bot.model.chat_session('Answer in 6 sentences max'):
            # check for previous chat history
            # if prev_convo == "":
            #     pass
            # elif len(prev_convo) > 1:
            #     prev = ast.literal_eval(prev_convo)
            #     if isinstance(prev, list):
            #         bot.model.current_chat_session = prev

            while chat:
                user_message = await websocket.receive_text()
                print(user_message)
                user_messages.append(user_message)

                if user_message == 'END':
                    chat = False
                    print(bot.get_chat_session())  # TODO store chat session
                else:
                    bot.respond(user_message)
                    print(bot.get_chat_session())
                    await websocket.send_text(json.dumps(bot.get_chat_session()))


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9000)
