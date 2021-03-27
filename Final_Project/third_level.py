import random

options = ['a', 'b', 'c', 'd']


def lifelines():
    answer = random.choice(options)
    print("The correct answer can be:", end=" ")
    print(answer)


def questions3():
    third_level = {
        "What is dermatophobia the fear of? "
        "a)Skin disease b)Coronavirus c)Pica d)Moebius syndrome": "a",
        "The Battle of Austerlitz took place during which war "
        "a)WW2 b)Seven Years' War c)WWI d)Napoleonic Wars?": "d",
        "Which Famous battle was fought in 1066? "
        "a)Battle of Waterloo b)Battle of the Somme c)Battle of Agincourt d)Battle of Hastings": "d",
        "What was the name of the ship on which the Pilgrims traveled to North America in 1620? "
        "a)The Santa Maria b)The Mayflower c)The Beagle d)The Beatle": "b",
        "Rome was founded in which year? a)1BC b)251BC c)2000BC d)753BC": "d",
        "Who was the king of England before Elizabeth II? "
        "a)Henry VII b)George VI c)Edward III d)Richard III": "b",
        "In which year was Nelson Mandela released from prison?"
        " a)1990 b)2000 c)1995 d)1980": "a",
        "Which former Prime Minister of India was assassinated in 1991? "
        "a)Rowing b)Artistic Swimming c)Surfing d)Cycling BMX": "a",
        "Which Welsh singer played himself in the 1996 film Mars Attacks!? "
        "a)Bryn Terfel b)Karl Jenkins c)Osian Ellis d)Tom Jones": "d"
    }

    question, answer = random.choice(list(third_level.items()))
    print(question)
    print("My answer is:", end=" ")
    user_answer = input()
    if user_answer == '*':
        lifelines()
        print("My answer is:", end=" ")
        user_answer = input()

    return user_answer == answer
