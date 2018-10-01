import sys

dayofmonth = {'1': 31, '2': 28,
              '3': 31, '4': 30,
              '5': 31, '6': 30,
              '7': 31, '8': 31,
              '9': 30, '10': 31,
              '11': 30, '12': 31}

MIN = input("Enter starting year: ")
MAX = input("Enter ending year: ")
MIN.strip()
MAX.strip()

if MIN.isdigit() is False or MAX.isdigit() is False:
    sys.exit("Incorrect input. Must be a number")
    
if int(MIN) > int(MAX):
    sys.exit("Starting year cannot be greater than ending year")
    
fname = str(MIN) + '-' + str(MAX) + '.txt'

print("Please choose a date format")
print("1 = monthdayyear")
print("2 = month-day-year")
print("3 = month/day/year")
dateFormat = input("Enter a number: ")
dateFormat.strip()

if dateFormat.isdigit() is False or int(dateFormat) > 3:
    sys.exit("Invalid selection")

f = open(fname, "w")

year = []
for z in range(int(MIN), int(MAX) + 1):
    year.append(z)
    
for y in year:
    for month in range(1, 13):
        for i in range(1, dayofmonth[str(month)] + 1):
            if int(dateFormat) == 1:
                f.write(str(month) + str(i) + str(y) + '\n')
            elif int(dateFormat) == 2:
                f.write(str(month) + '-' + str(i) + '-' + str(y) + '\n')
            else:
                f.write(str(month) + '/' + str(i) + '/' + str(y) + '\n')
                
print("Saved to: " + fname)
f.close()
