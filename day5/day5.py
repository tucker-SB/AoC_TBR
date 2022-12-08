
def get_top_crates(filename):
	fp = open(filename)
	lines = list(fp)
	crates, instructions = lines[:lines.index("\n")-1], lines[lines.index("\n")+1:]
		
	num_crates = len(crates[0]) // 4
	stacks = [ [] for _ in range(num_crates)]

	for line in crates:
		for i in range(num_crates):
			crate_val = line[i*4+1]
			if not crate_val == ' ':
				stacks[i] = [crate_val] + stacks[i]

	#print(stacks)
	for line in instructions:
		num, origin, dest = int(line.split(" ")[1]),int(line.split(" ")[3]),int(line.split(" ")[5])
		#print(num, origin, dest)
		for i in range(num):
			crate_val = stacks[origin-1].pop()
			stacks[dest - 1].append(crate_val)

	res = ""
	for stack in stacks:
		res += stack.pop()
	return res


def get_top_crates2(filename):
	fp = open(filename)
	lines = list(fp)
	crates, instructions = lines[:lines.index("\n")-1], lines[lines.index("\n")+1:]
		
	num_crates = len(crates[0]) // 4
	stacks = [ [] for _ in range(num_crates)]

	for line in crates:
		for i in range(num_crates):
			crate_val = line[i*4+1]
			if not crate_val == ' ':
				stacks[i] = [crate_val] + stacks[i]

	#print(stacks)
	for line in instructions:
		num, origin, dest = int(line.split(" ")[1]),int(line.split(" ")[3]),int(line.split(" ")[5])
		#print(num, origin, dest)
		stacks[dest - 1] = stacks[dest - 1] + stacks[origin - 1][-num:]
		stacks[origin - 1] = stacks[origin - 1][:-num]

	#print(stacks)
	res = ""
	for stack in stacks:
		res += stack.pop()
	return res


if __name__ == '__main__':
	print(get_top_crates("five_input.txt"))
	print(get_top_crates2("five_input.txt"))
	