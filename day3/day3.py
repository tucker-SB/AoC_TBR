def total_prio(filename):
	fp = open(filename)

	in_all = None
	for line in fp:
		length = len(line) - 1
		first, second = line[:length // 2], line[length // 2:length]
		
		first = set(list(first))
		second = set(list(second))

		both = first.intersection(second)
		
		if in_all:
			in_all = in_all + list(both)
		else:
			in_all = [] + list(both)

	score = 0	

	for char in in_all:
		if char.islower():
			score += ord(char) - 96
		else:
			score += ord(char) - 38


	return score

def badge_prio(filename):
	fp = open(filename)

	count = 0
	in_all = set([])
	score = 0
	for line in fp:
	
		both = line[:-1]
		
		both = set(both)
		
		if count == 0:
			in_all = both
			count += 1
		elif count == 2:
			in_all = in_all.intersection(both)
			score += get_prio(str(list(in_all)[0]))
			in_all = set([])
			count = 0
		else:
			in_all = in_all.intersection(both)
			count += 1

	return score

def get_prio(char):
	if char.islower():
		return ord(char) - 96
	else:
		return ord(char) - 38


	return score
if __name__ == '__main__':
	print(total_prio("three_input.txt"))
	print(badge_prio("three_input.txt"))
