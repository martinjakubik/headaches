import sys
import re
import argparse

parser = argparse.ArgumentParser(description = "formats headache data")
parser.add_argument("-i", "--inputfile", dest="inputfile")
parser.add_argument("-o", "--outputfile", dest="outputfile")
parser.add_argument("-d", "--debug", dest="debug", action="store_true")
args = parser.parse_args()

print(args.inputfile, args.outputfile, args.debug)

if args.inputfile is None:
    print(parser.print_help())
    sys.exit()

infile = args.inputfile
outfile = open(args.outputfile, "w")

with open(infile) as f:
    content = f.readlines()

content = [x.strip() for x in content]

def months(s):
    return {
            "jan": "1",
            "feb": "2",
            "mar": "3",
            "apr": "4",
            "may": "5",
            "jun": "6",
            "june": "6",
            "jul": "7",
            "july": "7",
            "aug": "8",
            "august": "8",
            "sep": "9",
            "sept": "9",
            "oct": "10",
            "nov": "11",
            "dec": "12",
        }.get(s, "0")

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

sep = ";"


i = 0
for line in content:
    i = i + 1
    semicolonPos = line.find(";")
    year = line[:semicolonPos]
    lineAfterYear = line[semicolonPos + 1:]

    spacePos = lineAfterYear.find(" ")
    weekdayWord = lineAfterYear[:spacePos]
    lineAfterWeekday = lineAfterYear[spacePos:].strip()

    spacePos = lineAfterWeekday.find(" ")
    month = lineAfterWeekday[:spacePos]
    lineAfterMonth = lineAfterWeekday[spacePos:].strip()

    spacePos = lineAfterMonth.find(" ")
    dayWord = lineAfterMonth[:spacePos]
    daySearch = re.search("[0-9]*", dayWord)

    if not daySearch is None:
        day = daySearch.group(0)
    else:
        day = 0

    lineAfterSpace = lineAfterMonth[spacePos + 1:]

    monthNum = months(month.lower())
    weekday = weekdays(weekdayWord)

    newline = year + sep + monthNum + sep  + day + sep + weekday + sep + lineAfterSpace
    if args.debug:
        print(newline)
    outfile.write(newline + "\n")

outfile.close()
