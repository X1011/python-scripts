from os import path, listdir
import sys

files = sys.argv

for file in files:
	# Get basename of file (without extension)
	basename = path.splitext(file)[0]
	
	for other_file in [f for f in listdir('.') if path.isfile(f)]:
		# Check if other file is a regular file and has the same basename (but different name)
		if path.isfile(other_file) and path.splitext(other_file)[0] == basename and other_file != file:
			print(other_file)
