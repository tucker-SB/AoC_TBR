# def calorie_count(filename):
# 	fp = open(filename)
#
# 	maxi = 0
# 	curr = 0
#
# 	for line in fp:
# 		if len(line) == 1:
# 			maxi = maxi if curr < maxi else curr
# 			curr = 0
# 		else:
# 			curr += int(line)
#
# 	return maxi

import heapq
def calorie_count_top3(filename):
	fp = open(filename)

	maxis = [0,0,0]
	heapq.heapify(maxis)
	curr = 0

	for line in fp:
		if len(line) == 1:
			heapq.heappushpop(maxis, curr)
			curr = 0
		else:
			curr += int(line)

	return maxis

if __name__ == '__main__':
	#print(calorie_count("one_input.txt"))
	print(max(calorie_count_top3("one_input.txt"))) #part 1
	print(sum(calorie_count_top3("one_input.txt"))) #part 2




