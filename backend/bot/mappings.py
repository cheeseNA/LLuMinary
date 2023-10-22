import json
import random

REVIEW_PATH = '../course_reviews.json'

ABBREV = {
    ("failed", "messed up"): "consolation",
    ("learning phase", "exam phase", "studying phase"): "lernphase",
    ("vis", "CAB", "polyball", "Bjorn", "Hackathon", "Katzensee", "diversity", "housing"): "student life",

    ("diskmat", "diskrete mathematik", "diskmathe", "diskmath",
     "diskrete mathe"): "Discrete Mathematics",
    ("linalg", "lineare algebra"): "Linear Algebra",
    ("eprog", "intro to programming", "prog", "programming class"): "Introduction to Programming",
    ("AuD", "Algorithms", "Algorithms and Datastructures",
     "Algorithmen und Datenstrukturen"): "Algorithms and Data Structures",

    ("AnW", "Algowahr", "Algorithmen und Wahrscheinlichkeit"): "Algorithms and Probability",
    ("pprog", "Parallele Programmierung", "Parallele Programmieren", "Paralleles Programmieren",
     "Paralleles Programmierung"): "Parallel Programming",
    ("ana", "ana1", "analysis", "analysis I"): "Analysis 1",
    ("DDCA", "digital design", "computer architecture", "labs", "FPGAs",
     "FPGA"): "Digital Design and Computer Architecture",

    ("numcs", "NumCS", "numerics", "numerical methods",
     "NumCSE"): "Numerical Methods for Computer Science",
    ("ana", "ana2", "analysis", "analysis II"): "Analysis 2",
    ("SPCA", "systems programming"): "Systems Programming and Computer Architecture",
    (
    "TI", "Theoretische Informatik", "TheoInf", "Theoretische Inf"): "Theoretical Computer Science",

    ("FMFP", "functional programming", "haskell", "monads", "formal methods",
     "functional programming and formal methods"): "Formal Methods and Functional Programming",
    ("DMDB", "databases", "database programming", "SQL", "data modeling", "data modelling",
     "data modelling and databases"): "Data Modeling and Databases",
    ("WuS", "Wahrscheinlichkeit und Statistik"): "Probability and Statistics",
    ("CN", "networks", "compnet"): "Computer Networks",

    ("APC", "Algorithms Probability and Computing"): "Algorithms, Probability and Computing",
    ("systems", ""): "Computer Systems",
    ("CD", "comp design"): "Compiler Design",
    ("HCI", ""): "Human Computer Interaction",
    ("IML", ""): "Introduction to Machine Learning",
    ("VisComp", "VisCom"): "Visual Computing",
    ("InfSec", ""): "Information Security",
    ("RSE", ""): "Rigorous Software Engineering",

    ("algolab", ""): "Algorithms Lab",
    ("ASL", "systems lab"): "Advanced Systems Lab",
    ("CIL", "comp intelligence lab", "intelligence lab"): "Computational Intelligence Lab",
    ("ISL", "security lab"): "Information Security Lab"
}


def map_course(abbreviation: str) -> str | None:
    """Maps a student's course abbreviation to the actual course name (e.x. diskmat to Discrete Mathematics).
    Returns None if abbreviation unknown."""
    if abbreviation == "":
        return None
    if abbreviation == "AnD":
        return "Algorithms and Data Structures"
    abbreviation = abbreviation.lower()

    for value in ABBREV.values():
        if value.lower() == abbreviation:
            return value  # perfect match

    for key in ABBREV.keys():
        for keyword in key:
            if keyword.lower() == abbreviation:
                return ABBREV[key]

    return None


def return_review(full_name: str) -> str | None:
    """
    Return Review given full name if exists
    :param full_name:
    :return:
    """
    with open(REVIEW_PATH, 'r') as json_file:
        data = json.load(json_file)
        if full_name in data.keys():
            full_rev = ''
            for rev in data[full_name]:
                full_rev = full_rev + '; ' + rev
            # return random.choice(data[full_name])
            return full_rev
