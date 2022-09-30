import datetime

dateFormatCodes = ["a", "A", "w", "d", "b", "B", "m", "y", "Y", "H", "I", "p", "M", "S", "f", "z", "Z", "j", "U", "W", "c", "x", "X", "%", "G", "u", "V"]

# turns format string into formatted date/time
def getDate(format):
    curDateTime = datetime.datetime.now()
    curDateTimeForm = curDateTime.strftime(format)
    return curDateTimeForm

# not yet implemented, still needs counterpart in gui.py
def checkDateFormat():
    while True:
        try:
            indexPercentDateFormat = []
            dateFormat = str(input("Please input your desired date Format:\n"))

            indexPercentDateFormat = [x for x in range(len(dateFormat)) if dateFormat.startswith('%', x)]
            if not indexPercentDateFormat:
                raise ValueError("There is no date format code in input.")

            indexDateFormatCodes = [dateFormatCodes.find(dateFormat[x + 1]) for x in indexPercentDateFormat]
            break
        except ValueError as errorMess:
            print(errorMess)
        except:
            print("This isn't a valid formatting. Check the date format codes for further reference.")

    return dateFormat