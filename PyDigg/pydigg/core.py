import os, json

path = "D:\Projetos\demo.knockout.asp" 

extension = ".asp" 

""" 

dirList = os.listdir(path) 
for file in dirList: 
	if file.endswith(".asp"): 
		print(file) 

""" 

for root, dirs, files in os.walk(path): 
	for file in files: 
		if file.endswith(extension): 
			fileName = os.path.join(root, file) 
			print(fileName) 
			print(" ")
			# Identify a charmap of a file 
			# https://nlp.fi.muni.cz/projects/chared/ 
			with open(fileName, encoding="latin_1") as f: 
				lines = f.readlines() 
				for line in lines: 
					if line: 
						if line.find(extension) > 0: 
							print(line)
			print(" ")