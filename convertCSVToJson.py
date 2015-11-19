import csv
import simplejson
import os


def main():

	csvFile = open("Data/CSV/StreetNames.csv", "r")
	csvReader = csv.reader(csvFile)
	csvData = list(csvReader)
	fieldNames = tuple(csvData[0])
	csvFile.close()

	length = len(fieldNames)
	jsonFile = open("Data/JSON/StreetNames.json", "w")
	print len(csvData)

	for x in csvData:
		y = {}
		i = 0
		while i < length:
			y[fieldNames[i]] = x[i]
			i = i + 1
		simplejson.dump(y, jsonFile)
		jsonFile.write("\n")
	jsonFile.close()

main()
