from first_level import questions1
from second_level import questions2
from third_level import questions3

with open('Prints.txt', 'r') as the_file:
    for line in the_file.readlines():
        print(line, end='')
print('\n')
print("Please write your name -> ", end=" ")
name = input()
print("Please write your surname -> ", end=" ")
surname = input()
print('{}{} {} {}'.format("You can start the game ", name, surname,
                          "Good Luck!"))
print("First level. ", "\n")

times = 0
money = 0
while times < 5:
    if questions1():
        money += 100
        print("{} {}{}{}".format("Your answer is correct.", "Now you have ",
                                 money, "$."))
        print("==========================================")
        times += 1
        if times == 5:
            print("Congrats! You passed 1st level!..Now you have 500$.Do you "
                  "want to continue the game or take the money?.If you want "
                  "to continue the game  write 'Yes',otherwise 'No'.")
            decision = input()
            if decision == "Yes":
                print("Second level !")
                times = 0
                money = 500
                while times < 5:
                    if questions2():
                        money += 300
                        print("{} {}{}{}".format("Your answer is correct.",
                                                 "Now you have ", money, "$."))
                        print("==========================================")
                        times += 1
                        if times == 5:
                            print("Congrats! You passed 2nd level!..Now you "
                                  "have 2000$.Do you want to continue the game"
                                  " or take the money?.If you want to continue"
                                  " the game  write 'Yes',otherwise 'No'.")
                            decision = input()
                            if decision == "Yes":
                                print("Third level !")
                                times = 0
                                money = 2000
                                while times < 5:
                                    if questions3():
                                        money += 500
                                        print("{} {}{}{}".format(
                                            "Your answer is correct.",
                                            "Now you have ", money, "$."))
                                        print("====================")
                                        times += 1
                                        if times == 5:
                                            print("Congratulations on winning "
                                                  "this game!!!...Now you have"
                                                  " 4500$")


                                    else:
                                        print("You lost the game")
                                        break
                                else:
                                    continue
                                break

                            else:
                                print("Thank you for participating."
                                      "You have now 2000$")
                                break

                    else:
                        print("You lost the game")
                        break
                else:
                    continue
                break


            else:
                print("Thank you for participating.You have now 500$")
                break

    else:
        print("You lost  the game")
        break
