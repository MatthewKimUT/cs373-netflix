#!/usr/bin/env python3

import sys
import os.path

if __name__ == '__main__':
	testInfo = open("/u/myk235/cs373/cs373-netflix/movie_cache.txt", "r")
	out = open("/u/myk235/cs373/cs373-netflix/movie_cache.py", "w")
	out.write("movie_cache = [");
	line = testInfo.readline()
	out.write(line[:-1])
	while(line):
		out.write("," + line[:-1])
		line = testInfo.readline()
		print("here at line " + line)
	out.write("]")
	out.close()
	testInfo.close()