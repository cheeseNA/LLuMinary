"""
FIGURE OUT WHY NTLK IS NOT WORKING!
"""
from backend.bot.bot import Bot

THRESHOLD = 10
# it is better to just keep the stem of the words of the inputs, and do this automatically,
# using NTLK but NTLK is not working for some reasons, and we are out of time so this is a less
# elegant solution.

KEYWORDS = {'depressed': 4, 'very': 2, 'hate myself': 9, 'can\'t do it': 5, 'overwhelming': 5,}


def depression_check(usr_input: str) -> bool:
    """
    Given some input, check if they are sad
    :param usr_input: str
    :return: bool: representing if ETH related
    """
    score = 0

    for word in KEYWORDS.keys():
        if word in usr_input:
            score += KEYWORDS[word]

    return score >= THRESHOLD


def redirect(bot: Bot) -> None:
    """
    Redirect the user to a mental health app
    """
    rsp = """As much as I hope you enjoy talking to me, I\'m not physical human,
     you should consult someone close, or visit 
     https://ethz.ch/students/en/advice/studies-and-health/contacts-health.html
     for more support."""

    bot.model.current_chat_session.append({'role': 'assistant', 'content': rsp})



