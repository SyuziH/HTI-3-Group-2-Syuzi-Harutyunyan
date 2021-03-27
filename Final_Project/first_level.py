import random

options = ['a', 'b', 'c', 'd']


def lifelines():
    answer = random.choice(options)
    print("The correct answer can be:", end=" ")
    print(answer)


def questions1():
    first_level = {
        "Which of these products is sold by the brands Colgate, Oral-B and Sensodyne?"
        " a)Deodorant b) Shampoo c) Toothpaste d) Sun cream": "c",
        "Who directed the film Titanic? "
        " a)Steven Spielberg b)Oliber Stone c)James Cameron d)John Woo": "c",
        "What is the past tense of the verb study?"
        " a)studyed b)studied c)studies d)studying": "b",
        "Which is the biggest island in the world?"
        " a)Greenland b)New Zealand c)Madagascar d)New Guinea": "a",
        "What might an electrician lay? a)Tables b)Gables c)Cables d)Stables": "c",
        "What is the largest country in the world?"
        " a)China b)Russia c)Armenia d)Poland": "b",
        "What are the five colours of the Olympic rings"
        "? a)Blue, yellow, black, green and red b)Blue, yellow, black, green and white"
        " c)Blue, yellow, brown, green and red d)Pink,yellow, black, green and red": "a",
        " Which singer has the most UK Number One singles ever? "
        "a)Arman Hovhannisyan b)Rihanna c)Lilit Hovhannisyan d)Elvis Presley": "d",
        "Which club won the 2017 UEFA Super Cup? "
        "a)Gandzasar b)Real Madrid c)Alashkert d)Atletico Madrid": "b",
        "Which singer was known amongst other things as 'The King of Pop'?"
        " a)Michael Jackson b)Jlo c)Tata d)Anush Arshakyan": "a",
        "In which movie would you hear the song 'Hakuna Matata'? "
        "a)Beauty and the Beast b)Lion King c)Cinderella d)Hercules": "b",
        "What sport does Cristiano Ronaldo play?"
        " a)basketball b)Soccer/football c)hockey d)skier": "b",
        "What is the name of the longest river in South America? "
        "a)Amazon b)Arax c)Volga d)Yangtze": "a",
        "What is the name of the actor who played Jack in Titanic? "
        "a)Morgan Freeman b)Robert De Niro c)Tom Hanks d)Leonardo DiCaprio": "d",
        "Which company uses Santa Claus for their advertisements?"
        " a)Coca Cola b)Fanta c)Amazon d)Netflix": "a",
        " What is the name of the character that Johnny Depp plays in Pirates of the Caribbean? "
        "a)Captain Jack Sparrow b)Forrest Gump c)Vivian Ward d)Bella Swan": "a",
        "How many players are there on a baseball team? a)1 b)5 c)22 d)9": "d",
        "What language is the most popularly spoken worldwide?"
        " a)British b)Armenian c)French d)Chinese": "d",
        "What is the date of “The Devils Night”?"
        " a)September 27th b)November 5th c)October 30th d) December 31th": "c",
        "What city is known as the City of Love? "
        "a)Yerevan b)Paris c)Amsterdam d)Berlin": "b"
    }

    question, answer = random.choice(list(first_level.items()))
    print(question)
    print("My answer is:", end=" ")
    user_answer = input()
    if user_answer == '*':
        lifelines()
        print("My answer is:", end=" ")
        user_answer = input()
    return user_answer == answer
