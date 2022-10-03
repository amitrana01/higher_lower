from art import logo, vs
from game_data import data
import random



score = 0
user_answer = ''
answer = ''
while user_answer == answer:
    print(logo)
    choice1 = random.choice(data)
    choice2 = random.choice(data)
    if choice1 == choice2:
        choice2 = random.choice(data)
    print(f'Compare A: {choice1["name"]}, a {choice1["description"]}, from {choice1["country"]}.')
    follower1 = choice1["follower_count"]
    # print(follower1)
    print(vs)

    print(f'Against B: {choice2["name"]}, a {choice2["description"]}, from {choice2["country"]}.')
    follower2 = choice2["follower_count"]
    # print(follower2)
    if follower1 > follower2:
        answer = follower1
    else:
        answer = follower2

    user_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_answer == 'a':
        user_answer = choice1["follower_count"]
    else:
        user_answer = choice2["follower_count"]

    if user_answer == answer:
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        # user_answer != answer
