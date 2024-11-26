def addEmails():
    file = open("test.txt", "r")
    emails = set()
    emails.add("svm227@lehigh.edu")
    filewrite = open("write.txt", "w")
    for email in file:
        emails.add(email.strip())

    for email in emails:
        filewrite.write(email+"\n")

    
    

addEmails()

