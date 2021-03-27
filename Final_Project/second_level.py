import random

options = ['a', 'b', 'c', 'd']


def lifelines():
    answer = random.choice(options)
    print("The correct answer can be:", end=" ")
    print(answer)


def questions2():
    second_level = {
        "What is the name of Shakespeare’s shortest tragedy? "
        "a)Hamlet b)Othello c)Antony and Cleopatra d)Macbeth": "d",
        "Quebec is a province in Canada. What language do they speak there?"
        " a)French b)English c)German d)Spanish": "a",
        "What happened during the years 1939-1945? a)World War I "
        "b) World War II c)American Revolutionary War d)Northwest Indian War": "b",
        "Which U.S. State is known as the “Sunflower State”? "
        "a)Boston b)Florida c)Kansas d)Montana": "c",
        "What plant is known to help heal a sunburn? "
        "a)Aloe b)Cactus c)Bamboo d)Golden buttopns": "a",
        "How many hearts does an octopus have? a)4 b)2 c)5 d)3 ": "d",
        "Which is a chain of international hotels?"
        " a)Four Tops b)Four Pennies c)Four Seasons d)Four Posters": "c",
        "Which of these countries did not host a Formula 1 Grand Prix race in 2003? "
        "a)Monaco b)France c)Italy d)Madagascar": "d",
        "Who built the Great Wall of China? a)The Qin Dynasty b)The Xia Dynasty "
        "c)The Shang Dynasty d)The Han Dynasty": "a",
        "Which jazz singer sings the song “What A Wonderful World”? "
        "a)Louis Amstrong b)Al Jarreau c)Frank Sinatra d)Ella Fitzgerald": "a",
        "Who was the author of the novel The Lion, the Witch, and the Wardrobe? "
        "a)Agatha Christie b)Harold Robbins c)Paulo Coelho d)C.S. Lewis": "d",
        "Which two planets in our solar system are known as “ice giants”? "
        "a)Mercury and Mars b)Neptune and Uranus c)Neptune and Jupiter d) Uranus and Earth": "b",
        "Arnold Schwarzenegger was once the governor of which U.S. State? "
        "a)Kansas b)New York c)California d)Montana": "c",
        "Which country is known to consume the most chocolate?"
        " a)Germany b)Belgium c)Moscow d)Switzerland": "d",
        "Who founded Kodak and the first camera? "
        "a)George Eastman b)Hans Lippershey c)Alister Hardy d)Niels Bohr": "a",
        "An older person is sometimes described as 'long in the ...'? "
        " a)Tooth b)Eye c)Hair d)Nose": "a",
        "Danny, Joey, Jesse, DJ, Stephanie, and Michelle are characters on what ‘90s show? "
        "a)Kenan & Kel b)My so-called life c)Full House d)Parker lewis can’t lose": "c",
        "Who is the fastest runner in the world?"
        " a)Usain Bolt b)Mo Farah c)Almaz Ayana d)Galen Rupp": "a",
        "Which of these is a spicy Indian dish? "
        "a)Spaghetti b)Biriani c)Bellini d)Crostini": "b",
        "Which of these is a theory about the creation of the universe?"
        " a)Big Bong b)Big Bang c)Big Ben d)Big Bertha": "b",

    }

    question, answer = random.choice(list(second_level.items()))
    print(question)
    print("My answer is:", end=" ")
    user_answer = input()
    if user_answer == '*':
        lifelines()
        print("My answer is:", end=" ")
        user_answer = input()

    return user_answer == answer
