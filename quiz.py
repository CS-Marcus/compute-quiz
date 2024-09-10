#variable to keep the score of the user 
score = 0 

'''
This function checks if the user's answer is correct
it takes the users answer and removes the spaces and turns it into complete lower case 
to check if the answer is correct
'''
def answer(input, ans):

    if input.lower().replace(" ","") == ans:
        global score
        score += 1 
        print("\nCorrect!\n")
    else:
        print("\nIncorrect\n")


'''
This function runs the main code of the project
'''
def main():
    print("\nWelcome to the computer quiz!\n")

    play = input("Do you want to play: ")

    if play.lower().replace(" ","") != "yes":
        quit()

    print("\nYou will have 4 questions to answer")

    user_input = input("\n1. What does RAM stand for: ")
    answer(user_input, "randomaccessmemory")

    user_input = input("\n2. Is c++ a high-level programming language? ")
    answer(user_input, "true")

    user_input = input('\n3. What does the acronym "HTTP" stand for? ')
    answer(user_input, "hypertexttransferprotocol")

    user_input = input("\n4. What does the CPU stand for in a computer? ")
    answer(user_input, "centralprocessingunit")


    print(f"Here is your score {score}")

main()