#!/usr/bin/env python3
import sys

if __name__ == '__main__':
	path = "/u/downing/cs/netflix/training_set"
	probe = open("/u/downing/cs/netflix/probe.txt", "r")
	out = open("/u/myk235/cs373/cs373-netflix/probe_values.txt", "w")
	line = probe.readline()
	movie_no = ""
	file_name = ""
	temp = open(path + "/mv_0000001.txt")
	while(line):
		if ":" in line:
			movie_no = line[:-2]
			file_name = path + "/mv_" + movie_no.zfill(7) + ".txt"
			print("Reading probe data for movie " + movie_no)
		customer = line[:-1]
		temp = open(file_name, "r")
		newline = temp.readline()
		newline = temp.readline()
		while (newline):
			arr = newline.split(",")
			if(arr[0] == customer):
				out.write(arr[1] + ', ')
				break
			newline = temp.readline()
		line = probe.readline()
		temp.close()
	out.close()
	probe.close()