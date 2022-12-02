def calc_score(filename):
	fp = open("two_input.txt")

	win_map = {"A":"Y", "B":"Z", "C":"X"}
	tie_map = {"A":"X", "B":"Y", "C":"Z"}

	score = 0
	for line in fp:
		opp, choice = line[:-1].split(" ")
		
		score += ord(choice) - 87
		if win_map[opp] == choice:
			score += 6
		elif tie_map[opp] == choice:
			score += 3

	return score

def calc_score2(filename):
	fp = open("two_input.txt")

	score = 0
	for line in fp:
		opp, outcome = line[:-1].split(" ")
		
		win_map  = {"A":2, "B":3, "C":1}
		tie_map  = {"A":1, "B":2, "C":3}
		lose_map = {"A":3, "B":1, "C":2}
		if outcome == "X":
			score += lose_map[opp]
		elif outcome == "Y":
			score += tie_map[opp] + 3
		else:
			score += win_map[opp] + 6

	return score
if __name__ == '__main__':
	print(calc_score("two_input.txt"))
	print(calc_score2("two_input.txt"))
