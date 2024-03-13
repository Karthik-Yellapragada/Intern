import random
def start_game():
    print('Welcome to the Mysterious Jungle game')
    print('The game has four Characters, each plays a crucial role for your survival')
    print('Vasundhara:The goddess of jungle')
    print('Nithin:The guard of jungle')
    print('Nirupama:The angel')
    print('Karthik:The devil')
    U_answer=input('Choose any one from the above')
    if U_answer.lower()=='vasundhara':
        vasundhara()
    elif U_answer.lower()=='nithin':
        nithin()
    elif U_answer.lower()=='nirupama':
        nirupama()
    elif U_answer.lower()=='karthik':
        karthik()
    else:
        print('Invalid selection')

def vasundhara():
    while True:
        print('Vasundhara is the goddess and the creator of the jungle...👸')
        print('To go further, the goddess has given you two ways: (left and right)')
        choice=input('enter 1-for right, 2-for left')
        if choice == '1':
           right1()
           break
        if choice == '2':
            print('The goddess gave you a map for your survival')
            follow_map()
            break
        else:
            print('Invalid choice')

def right1():
    print('The goddess has given you a tricky puzzle')
    print('_______ is the most numerous insect in the world which is almost blind and follows scent to move')
    answer = input('enter your answer')
    if answer.lower() == 'ant':
        print('You solved the puzzle')
        print('The goddess gave you two options:To get out of the jungle, TO move further')
        choice1 = input('Enter your choice:1-out , 2-move further')
        if choice1.lower() == '1':
            print('The goddess gave you a treasure box and teleported you to the exit')
            print('congratulations you won!..😊😇')
            main()
        elif choice1.lower() == '2':
            print('The goddess gave you another puzzle:')
            print('Which has the thickest fur among all mammals')
            answer1 = input('Enter your answer :')
            if answer1.lower() == 'sea otter':
                print('Your guess is correct')
                print('the goddess gave you a treasure box and teleported you to the exit')
                print('congratulations you won!..😊😇')
                main()
    else:
        print('The door remained locked')

def follow_map():
    print("You followed the map and discovered a secret door")
    print('to open the door you must solve a riddle')
    print('What can you hold in your left hand but not in your right')
    jawab=input('enter your answer :')
    if jawab.lower()=='right elbow':
        print('The door is the secret exit')
        print("Congratulations, you've won!....😊😇")
        main()
    else:
        print('Wrong answer..Better luck next time...')

def nithin():
    while True:
        print('Nithin is the protector and the saviour')
        print('To go further, the saviour has given you two ways: (left and right)')
        choice = input('enter 1-for right, 2-for left')
        if choice == '1':
            right2()
            break
        elif choice == '2':
            print('The saviour gave you a map for your survival')
            follow_map()
            break
        else:
            print('Invalid choice')

def right2():
    print('The saviour has given you a tricky puzzle')
    print('How many hearts does an octopus  have')
    answer = input('enter your answer')
    if answer.lower() == 'three':
        print('You solved the puzzle')
        print('The saviour gave you two options:To get out of the jungle, TO move further')
        choice1 = input('Enter your choice:1-out , 2-move further')
        if choice1.lower() == '1':
            print('The saviour gave you a treasure box and showed the exit')
            print('congratulations you won!..😊😇')
            main()
        elif choice1.lower() == '2':
            print('The saviour gave you another puzzle:')
            print('What is the slowest animal in the world??')
            answer1 = input('enter your answer')
            if answer1.lower() == 'sloth':
                print('Your guess is correct')
                print('The saviour gave you a treasure box and teleported you to the exit')
                print('congratulations you won!..😊😇')
                main()
    else:
        print('wrong answer....Better luck next time..')

def nirupama():
    while True:
        print('You have witnessed a angel before you')
        print('The angel wants to help you to get out')
        print('before that she wants to test your knowledge')
        print('A scorpion has 5 pairs of eyes ,how many eyes do 3 scorpions have???')
        choice = input('Enter your answer :')
        if choice.lower() == '30':
            right3()
            break
        else:
            print('Wrong answer try again!')

def right3():
    print('good you answered right!')
    print('I will give you two options : A map or A treasure box')
    choice=input('Choose any one :')
    if choice.lower()=='map':
        follow_map()
    elif choice.lower()=='treasure box':
        print('You found a treasure box')
        print('To open it you should solve a riddle')
        print('What type of music do rabbits listen to...??')
        ans=input('Your answer :')
        if ans.lower()=='hip hop':
            print('You are right....The box opened' )
            print('Again the angel appeared and given you a map for the secret exit')
            follow_map()
        else:
            print('Wrong answer try again!')
    else:
        print('Wrong answer try again!')

def karthik():
    while True:
        print('Karthik is the demon of the jungle')
        print('the demon gave you two options')
        print('left and right')
        choice=input('Enter your choice :')
        if choice.lower()=='left':
            print('the demon throwed you from the hill....You were dead..👻☠️💀')
            print('better luck next time!')
            main()
        if choice.lower()=='right':
            right4()
        else:
            print('the door remains locked...Better luck next time!')


def right4():
    print("You encounter a wild animal!")
    outcome = input(["run", "fight"])
    if outcome == "run":
        print("You run away and find a hidden path.")
        next_step()
    elif outcome== 'fight':
        print("You decide to fight the animal.")
        if random.random() < 0.5:  # 50% chance of winning the fight
            print("You defeat the animal and find a key.")
            next_step()
    else:
            print("Invalid choice")
def next_step():
    while True:
        choice = input("What's your next move? (1. Follow the map, 2. Explore further): ")
        if choice == '1':
            follow_map()
            break
        elif choice == '2':
            explore_further()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def explore_further():
    while True:
        print("You explore further and encounter a locked gate.")
        print("To unlock the gate, you must solve a riddle:")
        riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"
        answer = "echo"
        player_answer = input("Riddle: {}\nYour answer: ".format(riddle))
        if player_answer.lower() == answer:
            print("The gate opens, and you proceed.")
            print("You find yourself in a clearing with the exit visible.")
            print("Congratulations, you've won!")
            main()
        else:
            print("The gate remains locked. You must try again.")

def main():
    while True:
        play_again = input("Do you want to play the game? (yes/no): ")
        if play_again.lower() == "yes":
            start_game()
        else:
            print("Thank you for playing! Have a nice day....")
            break


if __name__ == "__main__":
    main()





