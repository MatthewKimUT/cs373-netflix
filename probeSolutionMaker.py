#!/usr/bin/env python3
import sys
from probe_actual import *

if __name__ == '__main__':
	probe = open("/u/downing/cs/netflix/probe.txt", "r")
	out = open("/u/myk235/cs373/cs373-netflix/probe_actual_new.py", "w")
	line = probe.readline()
	movie_no = ""
	file_name = ""
	customer = ""
	temp_ids = []
	out.write("probe_actual = [")
	probe_values = [0] * 17770
	customer_amount = [0] * 17770
	num = 0
	while(line):
		if ":" in line:
			movie_no = line[:-2]
			line = probe.readline()
			temp_ids = []
			num = 0;
		while(line):
			if ":" in line:
				break
			num += 1
			line = probe.readline()
		index = int(movie_no) - 1
		customer_amount[index] = num
	counter = 0;
	for i in range(len(customer_amount)):
		if customer_amount[i] != 0:
			tmp = customer_amount[i]
			if i == 0:
				out.write("[")
			else:
				out.write(",[")
			ratings = []
			for j in range(tmp):
				if j == 0:
					out.write(str(probe_actual[counter]))
				else:
					out.write("," + str(probe_actual[counter]))
				counter += 1
			out.write("]")
		else:
			if(i == 0):
				out.write("0")
			else:
				out.write(",0")
	out.write("]")
	out.close()
	probe.close()