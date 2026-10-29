
teams = ["Team A", "Team B", "Team C"]

questions = {
    "What is 5 + 3?": "8",
    "What is the capital of India?": "delhi",
    "Which language are you learning?": "python"
}

score = {
    "Team A": 0,
    "Team B": 0,
    "Team C": 0
}

for question, answer in questions.items():
    print("\nQuestion:", question)

    for team in teams:
        user_answer = input(team + ", enter your answer: ").lower()

        if user_answer == answer:
            print("Correct answer!")
            score[team] += 1
            break
        else:
            print("Wrong answer! Next team gets a chance.")

print("\n--- FINAL SCORE ---")

for team in teams:
    print(team, ":", score[team])
