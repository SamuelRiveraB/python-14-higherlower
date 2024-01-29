from game_data import data
import random


def higher_lower():

    rdm = 0
    rdm2 = 0
    score = 0

    while True:
        if(rdm == 0 and rdm2 == 0):
            while rdm == rdm2:
                rdm = random.randint(0, len(data)-1)
                rdm2 = random.randint(0, len(data)-1)
        else:
            rdm = rdm2
            rdm2 = random.randint(0, len(data)-1)
        more = data[rdm]["follower_count"] > data[rdm2]["follower_count"]
        print(f"Compare A: {data[rdm]['name']}, a {data[rdm]['description']} from {data[rdm]['country']}")
        print(f"Against B: {data[rdm2]['name']}, a {data[rdm2]['description']} from {data[rdm2]['country']}")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if choice == 'a' and more:
            score += 1
            print(f"Correct, current score: {score}")
        elif choice == 'a' and not more:
            print(f"You lost. Final score: {score}")
            return
        elif choice == 'b' and more:
            print(f"You lost. Final score: {score}")
            return
        elif choice == 'b' and not more:
            score += 1
            print(f"Correct, current score: {score}")

higher_lower()