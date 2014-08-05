# Script for comparing characters distribution among texts
# Usage:
# python character_comparator.py [directory]
# directory is a path to a directory containing several text files


import sys
import os
from collections import defaultdict

consider_space = True

book_maps = []
book_names = []

input_dir = sys.argv[1]
for book_filepath in os.listdir(input_dir):
    if book_filepath.endswith(".txt"):
    	with open(os.path.join(input_dir, book_filepath), 'r') as book_file:
			book_map = defaultdict(int)
			for line in book_file:
				for letter in line:
					book_map[letter] += 1
			book_maps.append(book_map)
			book_names.append(book_filepath)

for book_map in book_maps:
	print book_map

other_maps = list(book_maps)
i = 0
j = 0
for first_map in book_maps:
	other_maps.remove(first_map)
	for second_map in other_maps:
		if first_map == second_map:
			print book_names[i] + " is equal to " + book_names[j]
		j = j + 1
	i = i + 1
	
