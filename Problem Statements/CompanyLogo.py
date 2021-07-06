#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
	s = input()
	output = ''
	string = []
	table = []
	maxpose = 0
	maxpose2 = 0
	maxpose3 = 0

	for i in range(26):
		table.append(0)
	for char in s:
		string.append(char)

	for i in range(0, len(string)):
		k = ord(string[i])
		table[k - 97] += 1

	maxi = table[0]
	for i in range(26):
		if (table[i] > maxi):
			maxi = table[i]
			maxpose = i
	output = chr(maxpose + 97) + " " + str(maxi)
	print(output)
	table[maxpose] = 0

	maxi2 = table[0]
	for i in range(26):
		if (table[i] > maxi2):
			maxi2 = table[i]
			maxpose2 = i
	output = chr(maxpose2 + 97) + " " + str(maxi2)
	print(output)
	table[maxpose2] = 0

	maxi3 = table[0]
	for i in range(26):
		if (table[i] > maxi3):
			maxi3 = table[i]
			maxpose3 = i
	output = chr(maxpose3 + 97) + " " + str(maxi3)
	print(output)
	table[maxpose3] = 0


