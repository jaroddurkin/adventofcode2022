leaderboard = [0, 0, 0]
with open("input.txt") as f:
    s = 0
    for l in f:
        if l == "\n":
            # kinda weird but hey its O(n)
            if leaderboard[0] < s:
                leaderboard[2] = leaderboard[1]
                leaderboard[1] = leaderboard[0]
                leaderboard[0] = s
            elif leaderboard[1] < s:
                leaderboard[2] = leaderboard[1]
                leaderboard[1] = s
            elif leaderboard[2] < s:
                leaderboard[2] = s
            s = 0
        else:
            s += int(l)
print(sum(leaderboard))