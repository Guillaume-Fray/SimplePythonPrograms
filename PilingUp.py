from collections import deque

T = int(input())
num_of_blocks = 0
blocks = deque()

for i in range(T):
	ordered = []
	pile = True
	answer = "Yes"
	num_of_blocks = int(input())
	string = str(raw_input())
	s = string.split(" ")
	k = 0
	for j in range(num_of_blocks):
		cube = int(s[j])
		blocks.append(cube)
	while (k < num_of_blocks):
		if (blocks[0] > blocks[-1]):
			ordered.append(blocks[0])
			blocks.popleft()
			k += 1
		if (blocks[0] <= blocks[-1]):
			ordered.append(blocks[-1])
			blocks.pop()
			k += 1

	k = 0
	while (k < num_of_blocks and pile):
		if (k == 0 and ordered[k + 1] > ordered[k]):
			pile = False
		if (k > 0 and ordered[k] > ordered[k - 1]):
			pile = False
		k += 1

	if (not pile):
		answer = "No"

	print(answer)
