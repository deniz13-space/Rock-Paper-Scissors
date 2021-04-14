import random
   
def a():

    print(("-" * 21) + "\nRock, Paper, Scissors\n" + ("-" * 21))

    user_score, computer_score = 0, 0

    while True:

        print("\n1 - Rock\n2 - Paper\n3 - Scissors\n4 - Quit\n5 - View Score\n6 - Reset Score")

        user_choice = input("Your choice: ")

        computer_choice = random.choice(["1", "2", "3"])
   
        if user_choice == "1":

            if computer_choice == "1":

                print("Computer's choice: Rock\nRock equal to rock. Scoreless!")
           
            elif computer_choice == "2":

                print("Computer's choice: Paper\nPaper wraps stone. You lose")

                computer_score += 100
           
            elif computer_choice == "3":

                print("Computer's choice: Scissors\nRock breaks scissors. You win")

                user_score += 100
           
        elif user_choice == "2":

            if computer_choice == "1":

                print("Computer's choice: Rock\nPaper wraps stone. You win")

                user_score += 100
           
            elif computer_choice == "2":

                print("Computer's choice: Paper\nPaper equal to paper. Scoreless!")
           
            elif computer_choice == "3":

                print("Computer's choice: Scissors\nScissors cuts paper. You lose")

                computer_score += 100
           
        elif user_choice == "3":

            if computer_choice == "1":

                print("Computer's choice: Rock\nRock breaks scissors. You lose")

                computer_score += 100
           
            elif computer_choice == "2":

                print("Computer's choice: Paper\nScissors cuts paper. You win")

                user_score += 100
           
            elif computer_choice == "3":

                print("Computer's choice: Scissors\nScissors equal to scissors. Scoreless")

        if user_choice == "5": 

            print("\nUser's score: {}\nComputer's score: {}".format(user_score, computer_score))
    
        if user_choice == "6":

            user_score = 0

            computer_score = 0
            
        if user_choice == "4":
            
            break
      
a()