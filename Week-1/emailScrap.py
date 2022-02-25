import json
import re

# read data from input file(websiteData.txt)
inputFile = open("websiteData.txt", "r")
inputData = inputFile.readlines()
inputFile.close()


# Function to determine type of the email


def emailType(email):
    username = email.split("@")[0]

    # Check if the email is of format firstname.lastname@email.com
    # \w [a-zA-Z0-9_]
    # +  repeat one or more times
    if(re.match(r'[\w\.\-_]+\.[\w\.\-_]+', username)):
        return "Human"
    # Check if username is less than 8 characters
    elif(len(username) < 8):
        return "Non-Human"
    else:
        return "Not Sure"


# Create an empty dictionary
emailsDict = dict()


# Loop through each line of the file
for line in inputData:
    # Remove the leading spaces and newline character
    line = line.strip()

    # Lower case the string
    line = line.lower()

    # Split the line into words
    words = line.split()

    # Iterate over each word in line
    for word in words:
        # Check for emails
        if re.match(r'[\w\.\-_]+@[\w\.\-_]+', word):
            # Check if the email is already in dictionary
            if word in emailsDict:
                emailsDict[word]["Occurances"] += 1
            else:
                # Add the email  to dictionary with occurances and type of email
                emailsDict[word] = {
                    "Occurances": 1, "emailType": emailType(word)}


# convert into json and write to output file(result.json)
emailsJSON = json.dumps(emailsDict, indent=0)
outputFile = open("result.json", "w")
outputFile.write(emailsJSON)
outputFile.close()
