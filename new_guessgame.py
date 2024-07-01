import random as rand

questions = [
    "How are you {}?",
    "{} what is your current location?",
    "What is your profession {}?",
    "{} what is your best car brand?",
    "what is your dream city {}?",
]

question_num = range(1,len(questions) + 1)
question_choice = dict(zip(question_num,questions))
# print (question_choice)

def random_question() -> str:
    random_num = rand.choice(question_num)
    return question_choice[random_num]
    

def selected_question() -> str:
    try:
        user_choice =  int(input("Pick a question number between 1 and 5: "))
        return question_choice[user_choice]
    except KeyError:
        print("Oops! Error found")
    except ValueError:
        print("Error! Enter a digit!")
    except AttributeError:
        print ("Error found!")
        return


def run() -> str:
    try:
        name = input("Enter your name: ")
        if not name:
            return
        try:    
            question_type = int(input("Enter 1 for random question and 2 for a selected question: "))
        except ValueError:
            print("Error! Enter either 1 or 2.")
            return
        if question_type == 1:
            print(random_question().format(name))
        elif question_type == 2:
            print(selected_question().format(name))
        else:
            print("choose either 1 or 2 \nbreaking...\nTry again!")
            return
    except AttributeError:
        print ("Oops! Error found check your entries and try again.")
run()