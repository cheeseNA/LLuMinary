from backend.bot.mappings import *

THRESHOLD = 10
HARD_CODED = {'Numerical Methods for Computer Science': 'its a hard course, but \n'}
EVENTS = {''}
KEYWORDS = {'ETH Zurich': 5, 'with': 1, 'course': 2, 'how': 1, 'Zurich': 4, 'prof': 2}


def check_input(usr_input: str) -> bool:
    """
    Given some input, check if its ETH specific related
    :param usr_input: str
    :return: bool: representing if ETH related
    """
    score = 0
    inputs = usr_input.split()

    for word in KEYWORDS.keys():
        if word in usr_input:
            score += KEYWORDS[word]
    for u_in in inputs:
        if map_course(u_in):  # repeated code
            score += THRESHOLD
    print(score)
    return score >= THRESHOLD


