import sys
import re
import argparse
from collections import namedtuple
import datetime

parser = argparse.ArgumentParser(description = "generates negative headache data from file of positives")
parser.add_argument("-i", "--inputfile", dest="inputfile")
parser.add_argument("-o", "--outputfile", dest="outputfile")
parser.add_argument("-s", "--stopDate", dest="stopDate")
parser.add_argument("-d", "--debug", dest="debug", action="store_true")
args = parser.parse_args()

print(args.inputfile, args.outputfile, args.debug)

# gets the names of the input file and output file
if args.inputfile is None:
    print(parser.print_help())
    sys.exit()

infile = args.inputfile
outfile = open(args.outputfile, "w")

# gets the stop date
stopDateDefined = False
if args.stopDate:
    stopDateDefined = True
    stopYearString = args.stopDate.split("/")[0]
    stopMonthString = args.stopDate.split("/")[1]
    stopDayString = args.stopDate.split("/")[2]

    if int(stopYearString) == 0 or int(stopMonthString) == 0 or int(stopDayString) == 0:
        print("cannot parse the stop date; use a format like 2017/06/25")
        sys.exit()
    else:
        stopYear = int(stopYearString)
        stopMonth = int(stopMonthString)
        stopDay = int(stopDayString)

    if args.debug:
        print("year: \"%(stopYear)i\" month: \"%(stopMonth)s\" day: \"%(stopDay)s\"" % {"stopYear": stopYear, "stopMonth": stopMonth, "stopDay": stopDay})

# reads each line from the input file
with open(infile) as f:
    content = f.readlines()

# strips blanks from each line
content = [x.strip() for x in content]

# sets up correct number of days in each month; ignores leap years
Month = namedtuple("Month", "number num_days")
jan = Month(1, 31)
feb = Month(2, 28)
mar = Month(3, 31)
apr = Month(4, 30)
may = Month(5, 31)
jun = Month(6, 30)
jul = Month(7, 31)
aug = Month(8, 31)
sep = Month(9, 30)
oct = Month(10, 31)
nov = Month(11, 30)
dec = Month(12, 31)

months = [ jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec ]

# sets up names of weekdays as they may appear in the input file
def weekdays(s):
    if "monday" in s.lower():
        return "monday"
    elif "tuesday" in s.lower():
        return "tuesday"
    elif "wednesday" in s.lower():
        return "wednesday"
    elif "thursday" in s.lower():
        return "thursday"
    elif "friday" in s.lower():
        return "friday"
    elif "saturday" in s.lower():
        return "saturday"
    elif "sunday" in s.lower():
        return "sunday"
    else:
        return "weekday"

# sets up weekday names indexed monday = 0, tuesday = 1, ..., sunday = 6

weekdayNames = [ "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday" ]

# defines a separator character
sep = ";"

stopLoop = False

for yearNum in list(range(2015, 2017 + 1)):

    for monthNum in list(range(1, 12 + 1)):

        num_days_this_month = months[monthNum - 1].num_days

        for dayNum in list(range(1, num_days_this_month + 1)):

            eventFound = False

            for line in content:
                columns = line.split(";")

                columnYear = int(columns[0])
                columnMonth = int(columns[1])
                columnDay = int(columns[2])

                if columnYear == yearNum and columnMonth == monthNum and columnDay == dayNum:
                    eventFound = True

                    weekdayNum = datetime.date(columnYear, columnMonth, columnDay).weekday()
                    columnWeekdayString = weekdayNames[ weekdayNum ]
                    columnHour = columns[4]
                    columnMinute = columns[5]
                    columnPeriodOfDay = columns[6]
                    columnComment = columns[7]
                    columnIsHeadache = "1"

                    foundLine = (str(columnYear) + sep +
                                str(columnMonth) + sep +
                                str(columnDay) + sep +
                                str(weekdayNum) + sep +
                                columnHour + sep +
                                columnMinute + sep +
                                columnPeriodOfDay + sep +
                                columnComment + sep +
                                columnWeekdayString + sep +
                                columnIsHeadache)
                    break

            if eventFound == True:
                newLine = foundLine
            else:
                newWeekday = datetime.date(yearNum, monthNum, dayNum).weekday()
                columnWeekdayString = weekdayNames[ newWeekday ]
                newHour = ""
                newMinute = ""
                newPeriodOfDay = ""
                newComment = ""
                newIsHeadache = "0"
                newLine = (str(yearNum) + sep +
                            str(monthNum) + sep +
                            str(dayNum) + sep +
                            str(newWeekday) + sep +
                            newHour + sep +
                            newMinute + sep +
                            newPeriodOfDay + sep +
                            newComment + sep +
                            columnWeekdayString + sep +
                            str(newIsHeadache))

            if args.debug:
                print(newLine)
            outfile.write(newLine + "\n")

            # stops if past the given stop-date
            if stopDateDefined == True:
                if yearNum == stopYear and monthNum == stopMonth and dayNum == stopDay:
                    stopLoop = True
                    break

        if stopLoop == True:
            break

    if stopLoop == True:
        break


outfile.close()
