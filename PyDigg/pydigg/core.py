# Python libraries
import os, json

# Project functions

# TODO: Extract file path to a input on interface

path = "D:\Projetos\demo.knockout.asp"

# Looking for ASP classic files

extension = ".asp"

nodesData = list()
linksData = list()

# dirList = os.listdir(path)

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
                    {'name': 'Id', 'iskey': True, 'figure': "Decision", 'color': 'purple'}
                )

                for line in lines:

                    typeRelation = ">"

                    if line:

                        line = line.strip()

                        toFileName = ""
                        extPosition = line.find(extension)

                        if extPosition > 0:

                            print(line)
                            # fileName.replace(path, ""),
                            incPosition = line.find("include file=")
                            if incPosition > 0:
                                typeRelation = "include"
                                toFileName = line[incPosition + 13:extPosition + 4]

                            linkPosition = line.find("href=")

                            if linkPosition > 0:
                                typeRelation = "link"
                                toFileName = line[linkPosition + 4:extPosition + 4]

                            toFileName = toFileName.replace("\"", "")
                            toFileName = toFileName.replace("=", "")

                            if toFileName.rfind("/") > 0:
                                toFileName = toFileName[toFileName.rfind("/") + 1:]

                            linksData.append(
                                {'from': fileName, 'to': toFileName, 'text': typeRelation, 'toText': ">"}
                            )

                        # Check if the line has a definition of a ASP Function
                        if line.lower().startswith("function ") > 0:
                            dataItems.append(
                                {'name': line[8:].strip(), 'iskey': False, 'figure': "Decision", 'color': 'purple'}
                            )

                        # Check if the line has a definition of a ASP Sub (without return)
                        if line.lower().startswith("sub ") > 0:
                            dataItems.append(
                                {'name': line[3:].strip(), 'iskey': False, 'figure': "Decision", 'color': 'purple'}
                            )

                nodesData.append(
                    {
                        'key': fileName,
                        'title': file,
                        'items': dataItems
                    }
                )

            # print(" ")

entityRelationData = {
    'nodes': nodesData,
    'links': linksData
}

# Writing JSON data in a physical file
with open('entityRelationData.json', 'w') as f:
    json.dump(entityRelationData, f)
