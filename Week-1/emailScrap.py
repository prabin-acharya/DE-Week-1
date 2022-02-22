import re

# read data from input file(websiteData.txt)
inputFile = open("websiteData.txt", "r")
data = inputFile.read()
inputFile.close()


# extract emails
# \w [a-zA-Z0-9_]
# +  repeat one or more times
emails = re.findall(r'[\w\.-]+@[\w\.-]+', data)


# write to output file(result.json)
outputFile = open("result.json", "w")
outputFile.write("\n".join(emails))
outputFile.close()
