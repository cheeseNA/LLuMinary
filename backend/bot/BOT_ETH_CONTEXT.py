from gpt4all import GPT4All

DISCRETE_MATH_INFO = """Discrete Mathematics, also known as Diskmat: a very tough 1st semester course, hated by a lot of people, it features a lot of
formal proofs which most people struggle with. The professor is Ueli Maurer and has been teaching this course for many years. 
Start early with the exam preparations so you have time to go through all of the old exams which there are a lot of. 
Don't worry if you can't immediately solve most exercises. Course is mandatory, so not much choice. 
However, it was a very interesting subject and helps a lot going forward. It helps to think more logically and find answers to questions easier.
It is pretty difficult though, and often requires a lot of effort to get the topics done. The script is super useful and pretty much perfect to learn, 
the lecture is sometimes more confusing than just reading the script. Still, the exam is pretty hard. Overall very cool subject.\n"""

AUD_INFO = """An Algorithms course taught by professor Steurer, it features the concepts of runtime, recursion, dynamic programming
and graph theory, most people find dynamic programming especially challenging. Start solving Leetcode problems around mid-semester when Dynamic Programming and Graph theory part of the course.
starts. Most people struggle with Dynamic Programming. In general, a super interesting course! This is a great base for future courses. The profs do tend to make the explanation more confusing than it needs to be, and some lectures are confusing you more than teaching you new things. The script is quite nice, but more extensive than the infos from the lecture itself. The (coding) exercises are only partially doable from the course, and need a lot of time / prior knowledge (or google) to perfectly finish.
Overall very good, but since it's a 1st year course, there is not really a decision to be made."""

LINEAR_ALGEBRA_INFO = """Taught by Prof. Imamoglu and Prof. Sorkine-Hornung, historically one of the easiest courses of the first semester, 
even if the content is quite formal the exam has usually been very similar every year. Linear Algebra is a very important course 
useful in the later years, make sure you get a good hang of it even if it seems a bit rough and formal at first. Most people 
struggle with spectral decompositions and numerous proofs."""

INTRO_TO_PROGRAMMING_INFO = """Taught by Prof. Gross this Java course has usually been especially easy for people with prior programming
experience and especially hard for people without it.Start practicing programming skills very early, especially focusing on 
puzzle questions such as recursion, trees and pointers. A super cool and nice professor. The lecture is a bit boring and 
slow, but some needed that speed so it was quite okay. Java was definitely useful for other courses too, and if you don't 
have any coding experience (like I had), it is designed exceptionally well to follow the information. Exercises and lessons 
were done great too, fitting difficulty and very tied to the course itself. The exam was not too hard, but that 100% reflects 
on how much you did during the semester. It is not hard, but it still needs a lot of time to get right."""

FIRST_SEMESTER_INFO = """
The first semester courses are:
""" + DISCRETE_MATH_INFO + AUD_INFO + LINEAR_ALGEBRA_INFO + INTRO_TO_PROGRAMMING_INFO

ANW_INFO = """This course co-taught by Prof. Steger and Welzl is a continuation of the Algorithms course of the 1st semester, 
Algorithms and Probability teaches students some applied graph theory - connectivity, matchings, coloring, max-flow and 
some geometric algorithms. Apart from that a major block of the course is the Probability part. Super interesting course, 
with quite difficult topics that are explained exceptionally well. The profs were all great, the script is super useful, 
the exercise sessions were extremely helpful and the bonus points at perfect difficulty. More or less, exactly how you 
would want a course to be. However, the exam was a bit harder than expected, especially the written part. 
It was definitely possible to pass, though hard to get a really good grade. Would definitely prepare a bit more than 
average for this one. Regularly do practice quizzes, questions from them appear on the exam."""

PPROG_INFO = """The course of Parallel Programming taught by Prof. Solenthalter and Prof. Hoefler is an introduction to 
writing multi-threaded code. Course and topic are very interesting. However, the course itself is not structured well at all: 
the lecture itself is quite messy and often a bit boring. The exercise lessons were only partially helpful, it felt like the 
TAs were not prepared enough for the job. Also, some definitions changed mid-course, which does not bode well for the already 
unclear course. There also is no official script. However, the exam is not too hard and helps a bit to boost your average. 
The PVW script and course are (in my opinion) way more useful than the lectures themselves. Start solving the exams very early, 
they've historically been very similar very year which makes it the best way to prepare."""

ANALYSIS1_INFO = """The standard Real Analysis course, usually taught by a different professor every year.
It goes through limits, functions, continuity, differentiation and integration over the real numbers. Because the professor is different almost 
every year it's heavily recommended to put a lot of focus into the weekly exercises as it's hard to predict what the professor will put on the exam. 
Depending on how much Analysis you had in high school this course might not require a lot of effort. However solving the exercise sheets and attend 
the exercise sessions is important if you want a good grade."""

COMPUTER_ARCHITECTURE_INFO = """A course taught by a very passionate Prof. Onur Mutlu. It features labs that account for 30%
of the grade where you program FPGAs in Verilog by implementing a 32bit processor. 
Course is quite alright, good introduction into basic topics. However, the lecture is more or less a powerpoint presentation with hundreds of slides, 
which makes it hard to understand what is important. The labs are a bit messy too, and you are not really prepared for them at all. The course, labs 
and the exam are only sharing the same general topic, the exact details are extremely different for all of them. The lecture does not prepare you 
for the exam at all. Thankfully, it is not hard to pass (80% pass, quoted from the prof) and the same type of questions are in it every year. Just prepare 
with the old exams and the Optional Homework, and you will likely have a good grade. As bad as it may sound, the lectures are almost completely irrelevant to the exam,
one can just focus on solving the old exams and completely skip the lectures and readings."""

SECOND_SEMESTER_INFO = ANW_INFO + PPROG_INFO + ANALYSIS1_INFO + COMPUTER_ARCHITECTURE_INFO

###### 2nd year ######

ANALYSIS2_INFO = """A multivariable calculus course which first covers ordinary differential equations before moving to
continuity, differentiability and integration over vector spaces of real numbers. A mechanical course about multivariate calculus and ODEs.
The content is not much but there is a lot of integration and calculation in general required of you"""

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

LERNPHASE_INFO = """Lernphase is the time when students have time to study intensely for the upcoming exams. It's especially tough
because it happens either in Winter over Christmas through January with only 1 month of preparation time, or in the Summer
holidays (June-July) which means students can't enjoy any free time."""

CONVERSATION_MODE_FRIENDLY = (
    "You're a friendly, empathetic fellow older student, write words of support for a younger student"
    "that's struggling in their studies. He says that:\n")
CONVERSATION_MODE_MOTIVATIONAL = """You're a fellow older student, write a motivating speech for a younger student that's struggling with
motivation. He says that: \n"""
CONVERSATION_MODE_PASSIVE_AGGRESSIVE = """You're a pissed-off, bitter older student that feels superior. Write a cheeky response to the
younger student. He says that:\n"""




