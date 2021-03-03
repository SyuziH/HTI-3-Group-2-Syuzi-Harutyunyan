print(" Welcome to the Hangman game! You have five guesses to get the answer correct, or you will loose:(")

import random

file = open("D:/HTI-3-Group-2-Syuzi-Harutyunyan/Homework 8/fruits.txt")
file_content = file.read().splitlines()
secret_word = random.choice(file_content)
file.close()
guesses = ''
turns = 1
while turns < 7:
    failed = 0
    for char in secret_word:
        if char in guesses:
            print(char, end=" ")

        else:
            print("_", end=' ')
            failed += 1

    if failed == 0:
        print("You Win")
        break
    print('\n')
    guess = input()
    guesses += guess
    if guess not in secret_word:
        turns += 1
