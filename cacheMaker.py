#!/usr/bin/env python3

import sys
import os.path

if __name__ == '__main__':
	path = "/u/downing/cs/netflix/training_set/"
	directory = os.listdir(path)
	sorted_dir = sorted(directory)
	out = open('/u/myk235/cs373/cs373-netflix/customer_cache.py', 'w')
	customers = [None] * 2649429
	out.write("customer_cache = [")
	print(sys.maxsize)
	for fileName in sorted_dir:
		fullPath = os.path.join(path, fileName)
		if os.path.isfile(fullPath):
			temp = open(fullPath)
			line = temp.readline()
			movieNo = line[:-1]
			line = temp.readline()
			value = 0
			count = 1
			while line:
				arr = line.split(",")
				cNum = int(arr[0])
				rating = float(arr[1])
				if customers[cNum - 1] == None:
					customers[cNum -1] = [rating, 1]
				else:
					entry = customers[cNum - 1]
					newEntry = [((entry[0] * entry[1]) + rating) / (entry[1] + 1), entry[1] + 1]
					customers[cNum - 1] = newEntry
				line = temp.readline()
			print(movieNo + " is finished")
			temp.close()
	for i in range(len(customers)):
		tempEntry = customers[i]
		if(i == 0):
			out.write(str(-1))
		elif tempEntry != None:
			out.write("," + str(tempEntry[0]))
			print("Customer " + str(i + 1) + " is finished")
		else:
			out.write("," + str(-1))
	out.write("]")
	out.close()