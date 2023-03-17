from os import path, listdir
import sys

files = sys.argv

def get_basename(file):
	return path.splitext(file)[0]

def is_regular_file(file):
	return path.isfile(file)

def has_same_basename(file, other_file):
	return get_basename(file) == get_basename(other_file)

def is_not_same_file(file, other_file):
	return file != other_file

def is_duplicate(file, other_file):
	return is_regular_file(other_file) and has_same_basename(file, other_file) and is_not_same_file(file, other_file)

def get_duplicates(file):
	return [other_file for other_file in listdir('.') if is_duplicate(file, other_file)]

def print_duplicates(file):
	for duplicate in get_duplicates(file):
		print(duplicate)

for file in files[1:]:
	print_duplicates(file)
