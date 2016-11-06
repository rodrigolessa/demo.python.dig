import os, json

path = "D:\Projetos\demo.knockout.asp"

extension = ".asp"

entityRelationData = list()
nodesData = list()
linksData = list()

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
						line = line.strip()
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
							toNameFile = toNameFile.replace("=", "")
							if toNameFile.rfind("/") > 0:
								toNameFile = toNameFile[toNameFile.rfind("/") + 1:]
							linksData.append(
								{ 'from' : file, 'to' : toNameFile, 'text' : typeRelation, 'toText' : ">" }
							)
						if line.lower().startswith("function ") > 0:
							dataItems.append(
								{'name': line[8:].strip(), 'iskey': False, 'figure': "Decision", 'color': 'purple'}
							)
						if line.lower().startswith("sub ") > 0:
							dataItems.append(
								{'name': line[3:].strip(), 'iskey': False, 'figure': "Decision", 'color': 'purple'}
							)
				nodesData.append(
					{
						'key': file,
						'title': file,
						'items': dataItems
					}
				)
			#print(" ")

entityRelationData.append(
	{
		'nodes': nodesData,
		'links': linksData
	}
)

# Writing JSON data in a physical file
with open('entityRelationData.json', 'w') as f:
	json.dump(entityRelationData, f)