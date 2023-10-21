from typing import List, Dict
from gpt4all import GPT4All

from backend.bot.mappings import map_course, return_review
from backend.bot.mental_health_support import *
from backend.bot.BOT_ETH_CONTEXT import prompt_scan


class Bot:
    def __init__(self, max_tokens=0) -> None:
        self.max_tokens = max_tokens
        self.model = GPT4All('gpt4all-13b-snoozy-q4_0.gguf')

    def respond(self, usr_input: str) -> None:
        """
        given an input, give a tailored response
        :param usr_input:
        :return: None
        """
        scanned_res = prompt_scan(usr_input)
        prompts = usr_input.split()
        if scanned_res is not None:
            self.model.current_chat_session.append({'role': 'user', 'content': usr_input})
            self.model.current_chat_session.append({'role': 'assistant', 'content': scanned_res})
            return

        for word in prompts:
            full_name = map_course(word)
            if full_name is not None:
                resp_front = return_review(full_name)

                # a dirty way
                self.model.generate(f'summarize this: {resp_front} ',
                                    max_tokens=self.max_tokens, modify=True,
                                    original=usr_input, temp=1.0)

                if depression_check(usr_input):
                    redirect(self)
                return
        else:
            self.model.generate(usr_input)
            if depression_check(usr_input):
                redirect(self)
            return

    def get_chat_session(self) -> List[Dict[str, str]]:
        """
        Return the current chat session of the bot
        :return: List of Dicts
        """
        return self.model.current_chat_session
