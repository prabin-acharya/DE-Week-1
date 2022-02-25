import re
import json

# read data from input file(websiteData.txt)
inputFile = open("websiteData.txt", "r")
inputData = inputFile.read()
inputFile.close()


# Function to extract emails
def extractEmails(text):
    # \w [a-zA-Z0-9_]
    # +  repeat one or more times
    return re.findall(r'[\w+._-]+@[\w._-]+\.[\w_-]+', text)


# Function to determine type of the email
def emailType(email):
    username = email.split("@")[0]
    # Check if the email is of format firstname.lastname@email.com
    if(re.match(r'[\w+._-]+\.[\w+._-]+', username)):
        return "Human"
    elif(len(username) < 8):
        return "Non-Human"
    else:
        return "Not Sure"


# Create an empty dictionary
emailsDict = dict()

emails = extractEmails(inputData)

for email in emails:
    # Check if the email is already in dictionary
    if email in emailsDict:
        emailsDict[email]["Occurances"] += 1
    else:
        # Add the email  to dictionary with occurances and type of email
        emailsDict[email] = {"Occurances": 1, "emailType": emailType(email)}


# convert to json
emailsJSON = json.dumps(emailsDict, indent=0)

# write to output file(result.json)
outputFile = open("result.json", "w")
outputFile.write(emailsJSON)
outputFile.close()
