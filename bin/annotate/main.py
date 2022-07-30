import datetime

def getDate(regex):
    curDateTime= datetime.datetime.now()
    curDateTimeForm = curDateTime.strftime(regex)
    return curDateTimeForm

#needs input bugfixing: very easy to write wrong input!
    # tooltip as guide which expressions to use
    # and also try except and formatting help while entering
dateRegex = str(input("Please input the REGEX . . . . . I AM HUNGWY"))

print(getDate(dateRegex))