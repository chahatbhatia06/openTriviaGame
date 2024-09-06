import requests
import html
import random


# Get a pool of trivia questions
def get_question_pool(amount: int, category: int) -> list:
    url = f"https://opentdb.com/api.php?amount={amount}&category={category}"
    response = requests.get(url)
    response_json = response.json()
    return response_json["results"]


# Shuffle the answer choices for these questions
def shuffle_choices(choices: list) -> list:
    random.shuffle(choices)
    return choices


# Print the answer choices to the console
def print_choices(choices: list) -> None:
    for choice_index, choice in enumerate(choices):
        print(f"{choice_index + 1},{html.unescape(choice)}")

# Getting the user's input to the console
def get_user_choice() ->int:
    while True:
        user_choice = int(input("Enter the number of your choice: "))
        if user_choice in range(1, 5):
            return user_choice - 1
        else:
            print("Oops invalid input.")


# Play the game
def play_game(amount: int, category: int) -> None:
    question_pool = get_question_pool(amount, category)
    for question in question_pool:
        question_text = html.unescape(question["question"])
        print(question_text)
        choices = question["incorrect_answers"]
        choices.extend([question["correct_answer"]])
        shuffled_choices = shuffle_choices(choices)
        print_choices(shuffled_choices)
        user_choice_index = get_user_choice()
        user_choice_text = shuffled_choices[user_choice_index]
        correct_choice_text = html.unescape(question["correct_answer"])
        if user_choice_text == correct_choice_text:
            print(f"Correct! You answered: {correct_choice_text}\n")
        else:
            print(f"Incorrect answer. The correct answer is: {correct_choice_text}\n")

# Calling Main Function
if __name__ == "__main__":
     amount = 10
     category = 11
     play_game(amount, category)
