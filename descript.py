# utility to append stream titles to files from youtube-dl description files
from os import path, listdir
import sys

files = sys.argv[1:]

def get_basename(file):
	return path.splitext(file)[0]

def has_same_basename(file, other_file):
	return get_basename(file) == get_basename(other_file)

def is_duplicate(file, other_file):
	return path.isfile(other_file) and has_same_basename(file, other_file) and file != other_file

def get_duplicates(file):
	return [other_file for other_file in listdir('.') if is_duplicate(file, other_file)]

for file in files:
	for duplicate in get_duplicates(file):
		print(duplicate)
