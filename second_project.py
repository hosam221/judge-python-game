import time
import random


def print_sleep(message, wait_time):
    print(message)
    time.sleep(wait_time)


def intro():
    print_sleep(f"You are Judge {person}."
                f" Today you will pass judgment on the thief {person}", 3)
    print_sleep(f"who stole a {stolen} from a person in the street.", 2)
    print_sleep("Execution of the accused", 2)
    print_sleep("Imprisonment of the accused.", 2)
    print_sleep("Pardon of the accused.", 2)
    where_to()


def where_to():
    print_sleep("", 1)
    print_sleep("Enter 1 to Execution of the accused.", 2)
    print_sleep("Enter 2 to Imprisonment of the accused.", 2)
    print_sleep("Enter 3 to Pardon of the accused.", 2)
    print_sleep("What would you like to do?", 0)
    choice = ''
    while choice not in ['1', '2', '3']:
        choice = input("(Please enter 1 or 2 or 3.)\n")
    if choice == '1':
        execution()
    elif choice == '2':
        imprison()
    elif choice == '3':
        forgive()


def execution():
    if random.choice([True, False]):
        print_sleep("The judge sentenced the accused"
                    " to death by hanging.", 2)
        print_sleep(f"The executioner {person} successfully"
                    " carried out the sentence.", 2)
        print_sleep("You have done justice! "
                    "The court session has ended for today!", 2)
    else:
        print_sleep("Trying to escape and evade justice!", 2)
        print_sleep("The accused was arrested again!", 2)
        print_sleep("Choose what you want to do with the accused:", 2)
        first_where()


def first_where():
    print_sleep("", 1)
    print_sleep(f"Enter 1 to The court adjourned for {day}"
                " days from now, with his detention in prison.", 2)
    print_sleep("Enter 2 to Sentence him to death immediately.", 2)
    print_sleep("What would you like to do?", 0)
    choice = ''
    while choice not in ['1', '2']:
        choice = input("(Please enter 1 or 2.)\n")
    if choice == '1':
        print_sleep("The court has been adjourned.", 1)
    elif choice == '2':
        execution()


def imprison():
    if random.choice([True, False]):
        print_sleep("The judge sentenced the accused to prison"
                    " until an unknown date.", 2)
        print_sleep(f"The executioner {person} successfully "
                    "carried out the sentence.", 2)
        print_sleep("You have done justice!"
                    " The court session has ended for today!", 2)
    else:
        print_sleep("The accused has fled from justice!", 2)
        print_sleep("The police failed to find him!", 2)
        print_sleep("Unfortunately, nothing can be done now."
                    " The court has failed to achieve justice.", 2)


def forgive():
    if random.choice([True, False]):
        print_sleep("The judge ruled to pardon and release the accused.", 2)
        print_sleep(f"The executioner {person}"
                    " successfully carried out the sentence.", 2)
        print_sleep("You have done justice! The court"
                    " session has ended for today!", 2)
    else:
        print_sleep("The judge ruled to pardon"
                    " and release the accused!", 2)
        print_sleep(f"Oh, the {stolen} thief is back "
                    "after getting out of prison!", 2)
        print_sleep("The police pursued the thief and caught him.", 2)
        print_sleep("In your opinion, what is the appropriate "
                    "ruling that the judge should take?", 2)
        second_where()


def second_where():
    print_sleep("", 1)
    print_sleep(f"Enter 1 to court adjourned for {day}"
                " days from now, with his detention in prison.", 2)
    print_sleep("Enter 2 to Sentence him to death immediately.", 2)
    print_sleep("Enter 3 to Imprisonment of the accused.", 2)
    print_sleep("Enter 4 to Pardon of the accused.", 2)
    print_sleep("What would you like to do?", 0)
    choice = ''
    while choice not in ['1', '2', '3', '4']:
        choice = input("(Please enter 1 or 2 or 3 or 4.)\n")
    if choice == '1':
        print_sleep("The court has been adjourned.", 1)
    elif choice == '2':
        execution()
    elif choice == '3':
        imprison()
    elif choice == '4':
        forgive()


def play_again():
    choice = ''
    while choice not in ['y', 'n']:
        choice = input("Would you like to play again? (y/n)")
        if choice == 'n':
            print_sleep("Thanks for playing! See you next time.", 2)
            return 'game_over'
        elif choice == 'y':
            print_sleep("Excellent! Restarting the game ...", 2)
            return 'running'


game_state = 'running'
while game_state == 'running':
    persons = ['Ahmad', 'Husam', 'Mohammad', 'Hasan', 'Zain']
    person = random.choice(persons)
    stolen_goods = ['car', 'phone', 'wallet']
    stolen = random.choice(stolen_goods)
    days = ['5', '10', '15', '20', '25']
    day = random.choice(days)

    intro()
    where_to()

    game_state = play_again()
