import datetime

# language read from settings.txt
lang = 0
'''still needs to be implemented'''


# date format info in supported languages
langDateFormatValues = [("Weekday as locale’s abbreviated name.", "Wochentag als abgekürzter Name im Gebietsschema."), ("Weekday as locale’s full name.", "Wochentag als vollständiger Name im Gebietsschema."), ("Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.", "Wochentag als Dezimalzahl, wobei 0 Sonntag und 6 Samstag entspricht."), ("Day of the month as a zero-padded decimal number.", "Tag des Monats als Dezimalzahl mit vorangehender Nullstelle (sofern benötigt)."), ("Month as locale’s abbreviated name.", "Monat als abgekürzter Name im Gebietsschema"), ("Month as locale’s full name.", "Monat als vollständiger Name im Gebietsschema"), ("Month as a zero-padded decimal number.", "Monat als Dezimalzahl mit vorangehender Nullstelle (sofern benötigt)."), ("Year without century as a zero-padded decimal number.", "Jahr ohne Jahrhundert als Dezimahlzahl mit vorangehender Nullstelle (sofern benötigt)."), ("Year with century as a decimal number.", "Jahr mit Jahrhundert als Dezimalzahl."), ("Hour (24-hour clock) as a zero-padded decimal number.", "Stunde (24-Stunden Format) als Dezimalzahl mit vorangehender Null (sofern benötigt)."), ("Hour (12-hour clock) as a zero-padded decimal number.", "Stunde (12-Stunden Format) als Dezimalzahl mit vorangehender Null (sofern benötigt)."), ("Locale’s equivalent of either AM or PM.", "Das gebietsschematische Äquivalent zu entweder AM oder PM."), ("Minute as a zero-padded decimal number.", "Minute als Dezimalzahl mit vorangehender Null (sofern benötigt)."), ("Second as a zero-padded decimal number.", "Sekunde als Dezimahlzahl mit vorangehender Null (sofern benötigt)."), ("Microsecond as a decimal number, zero-padded to 6 digits.", "Mkrosekunde als Dezimalzahl mit vorangehenden Nullen mit insgesamt bis zu 6 Stellen."), ("UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).", "UTC Versatz im Format ±HHMM[SS[.ffffff]] (leerer String wenn das Objekt naiv ist)."), ("Time zone name (empty string if the object is naive).", "Zeitzonenname (leerer String wenn das Objekt naiv ist)."), ("Day of the year as a zero-padded decimal number.", "Tag des Jahres als Dezimalzahl mit vorangehender Null."), ("Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.", "Wochennummer des Jahres (Sonntag als erster Tag der Woche) als Dezimalzahl mit vorangehender Null. All Tage in einem neuen Jahr die dem ersten Sonntag vorgehen werden als Woche 0 gezählt."), ("Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0.", ""), ("Locale’s appropriate date and time representation.", "Wochennummer des Jahres (Montag als erster Tag der Woche) als Dezimalzahl mit vorangehender Null. All Tage in einem neuen Jahr die dem ersten Montag vorgehen werden als Woche 0 gezählt."), ("Locale’s appropriate date representation.", "Datum nach Gebietsschema."), ("Locale’s appropriate time representation.", "Uhrzeit nach Gebietsschema."), ("A literal '%' character.", "Das '%' Symbol."), ("ISO 8601 year with century representing the year that contains the greater part of the ISO week.", "ISO 8601 Jahr mit Jahrhundert, wobei das Jahr mit dem größeren Anteil der ISO Woche dargestellt wird."), ("ISO 8601 weekday as a decimal number where 1 is Monday.", "ISO 8601 Wochentag als Dezimalzahl, wobei 1 der Montag ist."), ("ISO 8601 week as a decimal number with Monday as the first day of the week. Week 01 is the week containing Jan 4.", "ISO 8601 Woche als Dezimalzahl mit Montag als ersten Tag der Woche. Woche 01 ist die Woche die den 4. Januar beinhält.")]
# loads date format info in currently set language
langDateFormatValuesLoaded = [x[lang] for x in langDateFormatValues]

dateFormatCodes = ["a", "A", "w", "d", "b", "B", "m", "y", "Y", "H", "I", "p", "M", "S", "f", "z", "Z", "j", "U", "W", "c", "x", "X", "%", "G", "u", "V"]
prefixdateFormatCodes = "%"


# turns format string into formatted date/time
def getDate(format):
    curDateTime= datetime.datetime.now()
    curDateTimeForm = curDateTime.strftime(format)
    return curDateTimeForm

# ((needs input bugfixing: very easy to write wrong input!))
    # tooltip as guide which expressions to use
    # and also try except and formatting help while entering -->> !! still improvable !!
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