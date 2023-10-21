import random

CONSOLATION_RESPONSE = [
    """I'm sorry to hear that you didn't get the result you were aiming for on your exam. I know it can be really frustrating and disappointing, but please don't be too hard on yourself. We all face setbacks from time to time, and this doesn't define your capabilities. If there's anything I can do to help you prepare for the next one or if you just need someone to talk to, I'm here for you. Remember, it's just a moment in your academic journey, and there are many more opportunities ahead to shine. Keep your spirits up!""",
    """I'm really sorry to hear that your exam didn't go as planned. I totally get how frustrating and disappointing that can be, but don't sweat it too much. We all have those tough moments. Your grade doesn't define how awesome you are. If you need some help or just want to chat about it, I'm here. We've got your back for the next round – together, we'll totally crush it!""",
    """Hey, I heard you didn't do so hot on your exam, and I just wanted to say, bummer, man. I know how it feels, and it totally sucks. But, seriously, don't beat yourself up about it. We all have our off days, and exams can be a real pain. If you need help prepping for the next one or just want to vent, I'm here for you. We've got your back, and there are plenty more chances to rock it in the future. Keep your chin up, alright?""",
    """I'm really sorry to hear about your exam results. I know how it feels when things don't go as planned. But don't sweat it too much – exams can be super tricky. We've all been there. If you need any help gearing up for the next round or just want to chat about it, count me in. You're way more than just one test score, and there are plenty more chances to ace it. Keep your head up, buddy!"""
]

# 4 entries

LERNPHASE_INFO = ["""Lernphase is the time when students have time to study intensely for the upcoming exams. It's especially tough
because it happens either in Winter over Christmas through January with only 1 month of preparation time, or in the Summer
holidays (June-July) which means students can't enjoy any free time.""",
"""Oh, the "Lernphase" is a real grind for us students. It's that brutal stretch when we have to hunker down and cram for the upcoming exams. The worst part? It hits us like a ton of bricks in the middle of winter, from Christmas through January, giving us just a measly month to get our act together. Or, if we're unlucky, it strikes during those precious summer holidays in June and July, robbing us of any chance to enjoy some carefree free time. It's like a never-ending battle against the books, and trust me, it's painful!""",
"""The "Lernphase" marks the period when students can dedicate themselves to intensive exam preparation. This phase presents a particular challenge, as it occurs either during the winter break, spanning from Christmas through January, allowing only a month for preparation, or during the summer holidays in June and July, which means students have limited opportunities for leisure and relaxation.""",
"""The dreaded "Lernphase" is when we students go into turbo study mode for our impending exams. It's a real struggle because it either hits us like a snowstorm during the Christmas break through January, giving us just one measly month to cram, or it invades our precious summer holidays in June and July, leaving us with no free time to enjoy. It's like a painful, relentless exam boot camp that we can't escape."""
]

# 4 entries

DISCRETE_MATH_INFO = ["""Discrete Mathematics, also known as Diskmat: a very tough 1st semester course, hated by a lot of people, it features a lot of
formal proofs which most people struggle with. The professor is Ueli Maurer and has been teaching this course for many years. 
Start early with the exam preparations so you have time to go through all of the old exams which there are a lot of. 
Don't worry if you can't immediately solve most exercises.""",
"""Discrete Mathematics, commonly referred to as Diskmat, is a challenging introductory course in the first semester that is often disliked by many due to its emphasis on formal proofs, a concept that proves to be quite challenging for most students. The course is taught by the experienced professor Ueli Maurer, who has been instructing it for several years. It is advisable to commence your exam preparations well in advance to allow sufficient time to review the numerous past exam papers available. If you find yourself unable to immediately solve most of the exercises, there's no need to fret.""",
"""Course is mandatory, so not much choice. 
However, it was a very interesting subject and helps a lot going forward. It helps to think more logically and find answers to questions easier.
It is pretty difficult though, and often requires a lot of effort to get the topics done. The script is super useful and pretty much perfect to learn, 
the lecture is sometimes more confusing than just reading the script. Still, the exam is pretty hard. Overall very cool subject.\n""",
"""You gotta take this course, no way around it. But you know what? It's actually pretty interesting and can be a big help down the road. It makes you think more logically and solves questions more easily.
But let's be real, it's not a walk in the park. You'll need to put in some serious effort to get the hang of the topics. The course material, called the script, is a lifesaver. It's super useful and pretty much perfect for learning. Sometimes, the lectures can be more confusing than just reading the script. And yeah, brace yourself, the exam is pretty tough. But all in all, it's a cool subject.""",
"""Diskmat, the mandatory Discrete Mathematics course taught by Professor Ueli Maurer, was surprisingly engaging. It enhanced logical thinking but required substantial effort. The course materials, particularly the script, were a lifeline, while the lectures sometimes added confusion. The exam, overseen by Professor Maurer, was tough but served as a solid test of knowledge. In the end, a challenging yet rewarding experience."""]

# 5 entries



AUD_INFO = [
"""An Algorithms course taught by professor Steurer, it features the concepts of runtime, recursion, dynamic programming and graph theory, most people find dynamic programming especially challenging. Start solving Leetcode problems around mid-semester when Dynamic Programming and Graph theory part of the course. starts. Most people struggle with Dynamic Programming.""",
"""The first few weeks are considered difficult by most, since you don't have a "grace period" of sorts like you do in other subjects before hard exercises appear. O-Notation and formal Induction can be tricky to grasp at first. Yet, once you reach Graph Theory, the course becomes significantly easier (and more enjoyable) in my opinion. Nearly everything apart from the algorithms presented in the first 2-3 lectures is really useful later on. Overall I quite enjoyed the course (was a TA for it later, so duh) and can only say that you should persist through the first few weeks - it'll get better with time.""",
"""In general, super interesting! This is a great base for future courses. The profs do tend to make the explanation more confusing than it needs to be, and some lectures are confusing you more than teaching you new things. The script is quite nice, but more extensive than the infos from the lecture itself. The (coding) exercises are only partially doable from the course, and need a lot of time / prior knowledge (or google) to perfectly finish. Overall very good, but since it's a Basisprüfung-Course, there is not really a decision to be made."""
]
# 3 summaries



LINEAR_ALGEBRA_INFO = ["""Taught by Prof. Imamoglu and Prof. Sorkine-Hornung, historically one of the easiest courses of the first semester, 
even if the content is quite formal the exam has usually been very similar every year. Linear Algebra is a very important course 
useful in the later years, make sure you get a good hang of it even if it seems a bit rough and formal at first. Most people 
struggle with spectral decompositions and numerous proofs.""",

"""Professors Imamoglu and Sorkine-Hornung team up for this first-semester course, which has traditionally been one of the more manageable ones. Despite the formal nature of the material, the exam tends to follow a consistent pattern from year to year. Linear Algebra may seem a bit tough and formal initially, but it's a crucial foundation for the years ahead. Spectral decompositions and a bunch of proofs can trip you up, but don't let that discourage you. Keep at it, and you'll get the hang of it."""

]

# 2 summaries

INTRO_TO_PROGRAMMING_INFO = ["""Taught by Prof. Gross this Java course has usually been especially easy for people with prior programming
experience and especially hard for people without it.Start practicing programming skills very early, especially focusing on 
puzzle questions such as recursion, trees and pointers.""",

"""A super cool and nice professor. The lecture is a bit boring and 
slow, but some needed that speed so it was quite okay. Java was definitely useful for other courses too, and if you don't 
have any coding experience (like I had), it is designed exceptionally well to follow the information. Exercises and lessons 
were done great too, fitting difficulty and very tied to the course itself. The exam was not too hard, but that 100% reflects 
on how much you did during the semester. It is not hard, but it still needs a lot of time to get right.""",

"""It can be difficult without prior coding experience. The key is to practice a lot of EBNF and old programming exam questions. The subject can also be very rewarding. In my opinion, it is one of the Subjects where a very good grade is achievable for everyone with enough practice. """
                             ]

# 3 entries

ANW_INFO = ["""This course co-taught by Prof. Steger and Welzl is a continuation of the Algorithms course of the 1st semester, 
Algorithms and Probability teaches students some applied graph theory - connectivity, matchings, coloring, max-flow and 
some geometric algorithms. Apart from that a major block of the course is the Probability part.""", """Super interesting course, 
with quite difficult topics that are explained exceptionally well. The profs were all great, the script is super useful, 
the exercise sessions were extremely helpful and the bonus points at perfect difficulty. More or less, exactly how you 
would want a course to be. However, the exam was a bit harder than expected, especially the written part. 
It was definitely possible to pass, though hard to get a really good grade. Would definitely prepare a bit more than 
average for this one. Regularly do practice quizzes, questions from them appear on the exam."""]

# 2 entries

PPROG_INFO = ["""The course of Parallel Programming taught by Prof. Solenthalter and Prof. Hoefler is an introduction to 
writing multi-threaded code. Course and topic are very interesting. However, the course itself is not structured well at all: 
the lecture itself is quite messy and often a bit boring. The exercise lessons were only partially helpful, it felt like the 
TAs were not prepared enough for the job. Also, some definitions changed mid-course, which does not bode well for the already 
unclear course. There also is no official script. However, the exam is not too hard and helps a bit to boost your average. 
The PVW script and course are (in my opinion) way more useful than the lectures themselves. Start solving the exams very early, 
they've historically been very similar very year which makes it the best way to prepare."""]

ANALYSIS1_INFO = ["""The standard Real Analysis course, usually taught by a different professor every year.
It goes through limits, functions, continuity, differentiation and integration over the real numbers. Not that fun but moderately useful. Because the professor is different almost 
every year it's heavily recommended to put a lot of focus into the weekly exercises as it's hard to predict what the professor will put on the exam.""",
"""Depending on how much Analysis you had in high school this course might not require a lot of effort. However solving the exercise sheets and attend 
the exercise sessions is important if you want a good grade."""]

COMPUTER_ARCHITECTURE_INFO = ["""A course taught by a very passionate Prof. Onur Mutlu. It features labs that account for 30%
of the grade where you program FPGAs in Verilog by implementing a 32bit processor.""",
"""Course is quite alright, good introduction into basic topics. However, the lecture is more or less a powerpoint presentation with hundreds of slides, 
which makes it hard to understand what is important. The labs are a bit messy too, and you are not really prepared for them at all. The course, labs 
and the exam are only sharing the same general topic, the exact details are extremely different for all of them. The lecture does not prepare you 
for the exam at all. Thankfully, it is not hard to pass (80% pass, quoted from the prof) and the same type of questions are in it every year. Just prepare 
with the old exams and the Optional Homework, and you will likely have a good grade. As bad as it may sound, the lectures are almost completely irrelevant to the exam,
one can just focus on solving the old exams and completely skip the lectures and readings."""]


ANALYSIS2_INFO = ["""A multivariable calculus course which first covers ordinary differential equations before moving to
continuity, differentiability and integration over vector spaces of real numbers.""", """A mechanical course about multivariate calculus and ODEs.
The content is not much but there is a lot of integration and calculation in general required of you"""]

##### EXTRA_INFO #####

STUDENT_LIFE_SUMMARIES = [
"""Computer Science students at ETH Zurich are active members of the VIS (Verein der Informatikstudenten) association, fostering connections within their program. VIS hosts various annual events, including the Hackathon and the Katzensee Barbeque. They also have a bear mascot named Bjorn. Notably, exams are held in August, leading to jokes about ETH students lacking free time. While CS students are humorously labeled as anti-social, a myriad of semester-long events counters this stereotype. The grand Polyball, held in November at the ETH main building, is the largest continental European ball. ETH Computer Science students enjoy perks like three free coffees or one free beer daily. Although most classes occur in the main building, CAB is the favored hangout spot, featuring a luxurious recreation room with a pool table and sofas. Unlike many English-speaking countries, students don't reside on campus, exacerbating Zurich's housing crisis and making affordable apartments hard to find. ETH's diversity shines, with over a third of students hailing from abroad, making it one of Europe's most diverse universities.""",
"""Computer Science students at ETH Zurich are part of the VIS (Verein der Informatikstudenten) association, fostering connections within the program. VIS organizes various events annually, including the Hackathon and Katzensee Barbeque, creating a vibrant social scene. The association has a bear mascot named Bjorn. Infamously, exams are held in August, leading to jokes about ETH students having no free time, though the reality is different due to numerous semester events. The Computer Science students are humorously described as anti-social, but events like the Polyball in November at the ETH main building, the largest ball in continental Europe, counter this stereotype. Additionally, ETH Computer Science students enjoy access to three free coffees or one free beer per day, while the CAB building, featuring a luxurious recreation room with a pool table and sofas, is a central hub despite most academic activities occurring in the main building. Unlike many English-speaking countries, students don't live on campus, exacerbating housing challenges in Zurich, where finding an affordable apartment is notoriously difficult. Nonetheless, ETH Zurich boasts a diverse student population, with over one-third hailing from abroad, making it one of the most diverse universities in Europe.""",
"""Computer Science students at ETH Zurich are actively involved in the VIS (Verein der Informatikstudenten) association, fostering connections within the program. VIS coordinates numerous annual events, including the renowned Hackathon and the delightful Katzensee Barbeque. The association's mascot, Bjorn the bear, adds a playful touch to the community. While ETH students face infamous August exams, often the subject of jests about their lack of free time, events throughout the semester belie the stereotype of CS students as anti-social. Notably, the annual Polyball in November, held at the ETH main building, ranks as continental Europe's largest ball. Students enjoy privileges such as three free coffees or one free beer per day and frequent CAB, a hub for recreation with a pool table and cozy sofas. Despite the absence of on-campus living, which aligns with Swiss norms, finding affordable housing in Zurich remains a challenging endeavor. ETH Zurich's remarkable diversity stands out, with over one-third of students hailing from abroad, rendering it one of Europe's more cosmopolitan universities.""",
"""Computer Science students at ETH Zurich are affiliated with the VIS (Verein der Informatikstudenten) association, fostering program-wide connections. VIS annually coordinates diverse events, including the Hackathon and Katzensee Barbeque. The association's playful mascot, Bjorn the bear, adds a touch of character. Notably, the August exam schedule has earned a reputation for consuming ETH students' free time, a source of many jokes. Although Computer Science students may jokingly be called anti-social, the numerous events throughout the semester challenge this stereotype, fostering a more sociable atmosphere within the community.""",
"""Computer Science students at ETH Zurich are members of the VIS (Verein der Informatikstudenten) association, promoting program-wide connections. VIS hosts numerous annual events, including the Hackathon and Katzensee Barbeque, and boasts a bear mascot named Bjorn. ETH students endure August exams, often a target for humor regarding their limited free time. The stereotype of CS students as anti-social is countered by the plethora of semester-long events, demonstrating their sociable side.""",
"""Computer Science students at ETH Zurich are members of the VIS (Verein der Informatikstudenten) association, fostering connections within the program. VIS hosts multiple annual events, including the Hackathon and Katzensee Barbeque. Their mascot, Bjorn the bear, adds a fun element to the community. The notoriety of August exams at ETH spawns jokes about students having no free time. While CS students may jokingly be labeled as anti-social, the many events throughout the semester contradict this stereotype, fostering a vibrant social atmosphere.""",
"""ETH Computer Science students enjoy daily access to three free coffees or one free beer. While lectures and exercises primarily occur in the main building, CAB serves as a favorite hangout, featuring an upscale recreation room with amenities like a pool table and sofas. Unlike the common practice in English-speaking countries, students at ETH Zurich don't live on campus, and the housing crisis in Zurich exacerbates the challenge of finding affordable apartments. With over one-third of students originating from abroad, ETH is notably one of Europe's more diverse universities. Students hold Professors like Ueli Maurer, a Discrete Math expert, and Onur Mutlu, an enthusiastic computer architecture specialist, in high regard.""",
"""ETH Zurich's Computer Science students enjoy perks like three free coffees or one free beer daily. Although most academic activities occur in the main building, CAB is the preferred hangout spot, boasting a chic recreation room with a pool table and comfy sofas. Unlike typical English-speaking countries, on-campus housing is rare, compounding the difficulty of finding affordable apartments amid Zurich's housing crisis. The university's remarkable diversity shines through, with over one-third of students hailing from abroad, making it one of Europe's more cosmopolitan institutions. Notably, students admire professors like Ueli Maurer, celebrated for his expertise in Discrete Math, and Onur Mutlu, an enthusiastic specialist in computer architecture.""",
"""ETH Computer Science students enjoy daily perks of 3 free coffees or 1 free beer. While lectures mainly occur in the main building, CAB becomes the go-to spot, offering a posh recreation room with a pool table and comfy sofas. Unlike the norm in English-speaking countries, students don't reside on campus, compounding the challenge of finding affordable housing amidst Zurich's housing crisis. The university's diversity shines with over one-third of students hailing from abroad, making it one of Europe's more multicultural institutions. Renowned professors like Ueli Maurer, a Discrete Math expert, and Onur Mutlu, an enthusiastic computer architecture specialist, are favorites among students."""
]



#### Might not be necessary ####
CONVERSATION_MODE_FRIENDLY = (
    "You're a friendly, empathetic fellow older student, write words of support for a younger student"
    "that's struggling in their studies. He says that:\n")
CONVERSATION_MODE_MOTIVATIONAL = """You're a fellow older student, write a motivating speech for a younger student that's struggling with
motivation. He says that: \n"""
CONVERSATION_MODE_PASSIVE_AGGRESSIVE = """You're a pissed-off, bitter older student that feels superior. Write a cheeky response to the
younger student. He says that:\n"""



def prompt_scan(prompt: str) -> str:
    """Scans the prompt for keywords, if a special keyword is found, returns a randomly chosen
    prescripted response. Else it returns null in which case you have to make
    bot generate a proper, unscripted response"""

    words = prompt.split()
    for word in words:
        response = decide_response(word)
        if response is not None:
            return response

    return None




def decide_response(response_identifier: str):
    """The response identifier comes from the mappings.map_course function.
    Important! If response is None - generate a proper (unscripted) response"""
    if response_identifier == "consolation":
        return CONSOLATION_RESPONSE[random.randint(0, len(CONSOLATION_RESPONSE)-1)]
    elif response_identifier == "student life":
        return STUDENT_LIFE_SUMMARIES[random.randint(0, len(STUDENT_LIFE_SUMMARIES) - 1)]
    elif response_identifier == "lernphase":
        return LERNPHASE_INFO[random.randint(0, len(LERNPHASE_INFO) - 1)]
    elif response_identifier == "Linear Algebra":
        return LINEAR_ALGEBRA_INFO[random.randint(0, len(LINEAR_ALGEBRA_INFO)-1)]
    elif response_identifier == "Introduction to Programming":
        return INTRO_TO_PROGRAMMING_INFO[random.randint(0, len(INTRO_TO_PROGRAMMING_INFO)-1)]
    elif response_identifier == "Algorithms and Data Structures":
        return AUD_INFO[random.randint(0, len(AUD_INFO)-1)]
    elif response_identifier == "Algorithms and Probability":
        return ANW_INFO[random.randint(0, len(ANW_INFO)-1)]
    elif response_identifier == "Parallel Programming":
        return PPROG_INFO[random.randint(0, len(PPROG_INFO)-1)]
    elif response_identifier == "Digital Design and Computer Architecture":
        return COMPUTER_ARCHITECTURE_INFO[random.randint(0, len(COMPUTER_ARCHITECTURE_INFO)-1)]

    else:
        return None


