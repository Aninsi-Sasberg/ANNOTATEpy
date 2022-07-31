import datetime

# language read from settings.txt
lang = 0
'''still needs to be implemented'''


# date format info in supported languages
langDateFormatValues = [("Weekday as locale’s abbreviated name.", ""), ("Weekday as locale’s full name.", ""), ("Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.", ""), ("Day of the month as a zero-padded decimal number.", ""), ("Month as locale’s abbreviated name.", ""), ("Month as locale’s full name.", ""), ("Month as a zero-padded decimal number.", ""), ("Year without century as a zero-padded decimal number.", ""), ("Year with century as a decimal number.", ""), ("Hour (24-hour clock) as a zero-padded decimal number.", ""), ("Hour (12-hour clock) as a zero-padded decimal number.", ""), ("Locale’s equivalent of either AM or PM.", ""), ("Minute as a zero-padded decimal number.", ""), ("Second as a zero-padded decimal number.", ""), ("Microsecond as a decimal number, zero-padded to 6 digits.", ""), ("UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).", ""), ("Time zone name (empty string if the object is naive).", ""), ("Day of the year as a zero-padded decimal number.", ""), ("Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.", ""), ("Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.", ""), ("Locale’s appropriate date and time representation.", ""), ("Locale’s appropriate date representation.", ""), ("Locale’s appropriate time representation.", ""), ("A literal '%' character.", ""), ("ISO 8601 year with century representing the year that contains the greater part of the ISO week (%V).", ""), ("ISO 8601 weekday as a decimal number where 1 is Monday.", ""), ("ISO 8601 week as a decimal number with Monday as the first day of the week. Week 01 is the week containing Jan 4.", ""), ]
# loads date format info in currently set language
langDateFormatValuesLoaded = [x[lang] for x in langDateFormatValues]

dateFormatCodes = ["a", "A", "w", "d", "b", "B", "m", "y", "Y", "H", "I", "p", "M", "S", "f", "z", "Z", "j", "U", "W", "c", "x", "X", "%", "G", "u", "V"]
prefixdateFormatCodes = "%"

def getDate(format):
    curDateTime= datetime.datetime.now()
    curDateTimeForm = curDateTime.strftime(format)
    return curDateTimeForm

# needs input bugfixing: very easy to write wrong input!
    # tooltip as guide which expressions to use
    # and also try except and formatting help while entering
def checkDateFormat():
    while True:
        try:
            indexPercentDateFormat = []
            dateFormat = str(input("Please input the REGEX . . . . . I AM HUNGWY"))
            
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
'''needs to be tested'''



dateFormatPass = checkDateFormat()

print(getDate(dateFormatPass))