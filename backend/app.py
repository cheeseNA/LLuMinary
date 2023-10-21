import os
import json

from bot.bot import Bot
from fastapi import FastAPI, Request, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

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

# @app.get("/")
# def read_root(request: Request):
#     return templates.TemplateResponse("chat.html", {"request": request})


@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
    print('ATTEMPTING TO CONNECT')
    await websocket.accept()
    print('CONNECTION ACCEPTED')
    # prev_convo = [
    #     {'role': 'user', 'content': 'my name is Robert'},
    #     {'role': 'assistant', 'content': 'Hello, my name is AI. How can I assist you today?'}]

    while True:
        bot = Bot(200)
        chat = True
        with bot.model.chat_session(system_prompt='answer in 4 sentences max'):
            # if prev_convo:
            #     # print('yes')
            #     bot.model.current_chat_session = prev_convo
            # TODO initialize chat session
            while chat:
                user_message = await websocket.receive_text()
                print(user_message)
                user_messages.append(user_message)

                if user_message == 'END':
                    chat = False
                    print(bot.get_chat_session())  # TODO store chat session
                else:
                    new_resp = bot.respond(user_message)
                    print(bot.get_chat_session())
                    # send list [{}]

                    await websocket.send_text(json.dumps(bot.get_chat_session()))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)