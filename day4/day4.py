def count_full_contains(filename):
	fp = open(filename)

	count = 0
	for line in fp:
		first, second = line[:-1].split(',')

		first_s, first_e = first.split('-')
		second_s, second_e = second.split('-')

		if int(first_s) < int(second_s):
			if int(first_e) >= int(second_e):
				count += 1
		elif int(first_s) > int(second_s):
			if int(first_e) <= int(second_e):
				count += 1
		else:
			count += 1
	return count

def count_intersect(filename):
	fp = open(filename)

	count = 0
	for line in fp:
		first, second = line[:-1].split(',')

		first_s, first_e = first.split('-')
		second_s, second_e = second.split('-')

		if int(first_s) < int(second_s):
			if int(first_e) >= int(second_s):
				count += 1
		elif int(first_s) > int(second_s):
			if int(first_s) <= int(second_e):
				count += 1
		else:
			count += 1
	return count
if __name__ == '__main__':
	print(count_full_contains("four_input.txt"))
	print(count_intersect("four_input.txt"))