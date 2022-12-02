points = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

wins = {
    "X": "C",
    "Y": "A",
    "Z": "B"
}

ties = {
    "X": "A",
    "Y": "B",
    "Z": "C",
}

decision = {
    "X": {
        "A": "Z",
        "B": "X",
        "C": "Y",
    },
    "Y": {
        "A": "X",
        "B": "Y",
        "C": "Z",
    },
    "Z": {
        "A": "Y",
        "B": "Z",
        "C": "X",
    }
}

with open("day2/input.txt") as f:
    score = 0
    for l in f:
        l = l.replace("\n", "")
        moves = l.split(' ')
        my_move = decision[moves[1]][moves[0]]
        score += points[my_move]
        if moves[0] == wins[my_move]:
            score += 6
        elif moves[0] == ties[my_move]:
            score += 3

print(score)
