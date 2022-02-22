import re

# read data from input file
inputFile = open("websiteData.txt", "r")
data = inputFile.read()
data = [x.strip() for x in data.split()]
inputFile.close()


# parse data for emails
emails = []
for x in data:
    if x.find("@") != -1:
        emails.append(x)

print(emails)

# write to output file
outputFile = open("result.json", "w")
outputFile.write("\n".join(emails))
outputFile.close()
