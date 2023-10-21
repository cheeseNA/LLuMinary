from gpt4all import GPT4All

MODEL_PATH = "/home/main1/Downloads/GPT4All-13B-snoozy.ggmlv3.q4_0.bin"
TOKENS = 200
STREAMING = True
THREADS = 16

gpt = GPT4All("/home/main1/Downloads/GPT4All-13B-snoozy.ggmlv3.q4_0.bin", n_threads=16)

DISCRETE_MATH_INFO = """Discrete Mathematics, also known as Diskmat: a very tough 1st semester course, hated by a lot of people, it features a lot of
formal proofs which most people struggle with. The professor is Ueli Maurer and has been teaching this course for many years. 
Start early with the exam preparations so you have time to go through all of the old exams which there are a lot of. 
Don't worry if you can't immediately solve most exercises. Course is mandatory, so not much choice. 
However, it was a very interesting subject and helps a lot going forward. It helps to think more logically and find answers to questions easier.
It is pretty difficult though, and often requires a lot of effort to get the topics done. The script is super useful and pretty much perfect to learn, 
the lecture is sometimes more confusing than just reading the script. Still, the exam is pretty hard. Overall very cool subject."""

AUD_INFO = """An Algorithms course taught by professor Steurer, it features the concepts of runtime, recursion, dynamic programming
and graph theory, most people find dynamic programming especially challenging."""

AUD_ADVICE = """Start solving Leetcode problems around mid-semester when Dynamic Programming and Graph theory part of the course
starts."""

LINEAR_ALGEBRA_INFO = """Even though taught by a new professor this year, historically one of the easiest courses of the first semester, 
even if the content is quite formal the exam has usually been very similar every year."""

LINEAR_ALGEBRA_ADVICE = """Linear Algebra is a very important course useful in the later years, make sure you get a good hang of it
even if it seems a bit rough and formal at first."""

INTRO_TO_PROGRAMMING_INFO = """Taught by Prof. Gross this Java course has usually been especially easy for people with prior programming
experience and especially hard for people without it."""

INTRO_TO_PROGRAMMING_ADVICE = """Start practicing programming skills very early, especially focusing on puzzle questions such as
recursion, trees and pointers"""

FIRST_SEMESTER_INFO = """
The first semester courses are:
""" + DISCRETE_MATH_INFO + AUD_INFO + LINEAR_ALGEBRA_INFO + INTRO_TO_PROGRAMMING_INFO

ANW_INFO = """This course co-taught by Prof. Steger and Welzl is a continuation of the Algorithms course of the 1st semester, 
Algorithms and Probability teaches students some applied graph theory - connectivity, matchings, coloring, max-flow and 
some geometric algorithms. Apart from that a major block of the course is the Probability part."""

ANW_ADVICE = """Regularly do practice quizzes, questions from them appear on the exam."""

PPROG_INFO = """The course of Parallel Programming taught by Prof. Solenthalter and Prof. Hoefler is an introduction to 
writing multi-threaded code."""

PPROG_ADVICE = """Start solving the exams very early, they've historically been very similar very year which makes it the best way to prepare."""

ANALYSIS1_INFO = """The standard Real Analysis course, usually taught by a different professor every year.
It goes through limits, functions, continuity, differentiation and integration over the real numbers."""

ANALYSIS_ADVICE = """Because the professor is different almost every year it's heavily recommended to put a lot of focus into
the weekly exercises as it's hard to predict what the professor will put on the exam."""

COMPUTER_ARCHITECTURE_INFO = """A course taught by a very passionate Prof. Onur Mutlu. It features labs that account for 30%
of the grade where you program FPGAs in Verilog by implementing a 32bit processor."""

COMPUTER_ARCHITECTURE_ADVICE = """As bad as it may sound, the lectures are almost completely irrelevant to the exam,
one can just focus on solving the old exams and completely skip the lectures and readings."""

SECOND_SEMESTER_INFO = ANW_INFO + PPROG_INFO + ANALYSIS1_INFO + COMPUTER_ARCHITECTURE_INFO

###### 2nd year ######

ANALYSIS2_INFO = """A multivariable calculus course which first covers ordinary differential equations before moving to
continuity, differentiability and integration over vector spaces of real numbers."""

##### EXTRA_INFO #####


LERNPHASE_INFO = """Lernphase is the time when students have time to study intensely for the upcoming exams. It's especially tough
because it happens either in Winter over Christmas through January with only 1 month of preparation time, or in the Summer
holidays (June-July) which means students can't enjoy any free time."""

CONVERSATION_MODE_FRIENDLY = (
    "You're a friendly, empathetic fellow older student, write words of support for a younger student"
    "that's struggling in their studies.")
CONVERSATION_MODE_MOTIVATIONAL = """You're a fellow older student, write a motivating speech for a younger student that's struggling with
motivation"""
CONVERSATION_MODE_PASSIVE_AGGRESSIVE = """You're a pissed-off, bitter older student that feels superior. Write a cheeky response to the
younger student. He says that:"""


# feel free to add more


def chatbot_interface(current_question: str, previous_promps: list[str], student_name: str, student_semester: int,
                      conversation_style: int):
    # TODO - how can we make it sound natural, while preserving at least some memory from the previous prompts and not losing out on speed?
    # out of the box it doesn't sound very natural, we have to try out different prompt combinations
    """Ideas:
    -make it non-deterministic
    -scan the student prompt for course keywords (e.x. diskmat, NumCS and inject only the required responses to reduce context
    -write a script that reads the current date and injects the correct time information into the prompt: e.x. semester
    start/mid-semester/lernphase/grades out day/holidays etc.
    -during idle-time make the bot summarize previous prompts and feed them instead to reduce context size
    """
    question = "Student: I'm really struggling with Diskmat, can you give me some advice? "
    prompt = CONVERSATION_MODE_MOTIVATIONAL + DISCRETE_MATH_INFO + question

    for token in gpt.generate(prompt=prompt, max_tokens=TOKENS, streaming=STREAMING, n_batch=THREADS):
        print(token, sep=" ", end=" ")

# question = """
# Student: Hey, I've been feeling a little overwhelmed recently, especially with Diskmat, could you offer some advice?\nFriendly bot:
# """
# prompt = "I am depressed. Make me not depressed."


# output = []

# for token in gpt.generate(prompt=prompt, max_tokens=tokens, streaming=streaming, n_batch=16, temp=3.0):
#    print(token, sep=" ", end=" ")




