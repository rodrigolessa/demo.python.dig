import os, json

path = "D:\Projetos\demo.knockout.asp"

extension = ".asp"

nodeData = list()
linkData = list()

#dirList = os.listdir(path)

for root, dirs, files in os.walk(path):
	for file in files:
		if file.endswith(extension):
			fileName = os.path.join(root, file)
			print(fileName)
			# Identify a charmap of a file
			# https://nlp.fi.muni.cz/projects/chared/
			with open(fileName, encoding="latin_1") as f:
				lines = f.readlines()
				dataItems = list()
				dataItems.append(
					{ 'name' : 'Id', 'iskey' : True, 'figure' : "Decision", 'color' : 'purple' }
				)
				for line in lines:
					typeRelation = ">"
					if line:
						toNameFile = ""
						extPosition = line.find(extension)
						if extPosition > 0:
							print(line)
							#fileName.replace(path, ""),
							incPosition = line.find("include file=")
							if incPosition > 0:
								typeRelation = "include"
								toNameFile = line[incPosition + 13:extPosition + 4]
							linkPosition = line.find("href=")
							if linkPosition > 0:
								typeRelation = "link"
								toNameFile = line[linkPosition + 4:extPosition + 4]
							toNameFile = toNameFile.replace("\"", "")
							if toNameFile.find("/") > 0:
								toNameFile = toNameFile[toNameFile.find("/") + 1:]
							linkData.append(
								{ 'from' : file, 'to' : toNameFile, 'text' : typeRelation, 'toText' : ">" }
							)
						if line.startswith("function ") > 0:
							dataItems.append(
								{'name': 'Funcao', 'iskey': False, 'figure': "Decision", 'color': 'purple'}
							)
						if line.startswith("sub ") > 0:
							dataItems.append(
								{'name': 'Call', 'iskey': False, 'figure': "Decision", 'color': 'purple'}
							)
				nodeData.append(
					{
						'key' : file,
					  	'items' : dataItems
					}
				)
			#print(" ")

# Writing JSON data in a physical file
with open('data.json', 'w') as f:
	json.dump(nodeData, f)

with open('link.json', 'w') as g:
	json.dump(linkData, g)