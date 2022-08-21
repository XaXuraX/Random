a = int (input ("Enter a year : "))

# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
if (a % 400 == 0) and (a % 100 == 0):
    print(a, " is a leap year")

# not divided by 100 means not a century year
# year divided by 4 is a leap year
elif (a % 4 ==0) and (a % 100 != 0):
    print( a, "is a leap year")

# if not divided by both 400 (century year) and 4 (not century year)
# year is not leap year
else:
    print( a, " is not a leap year")
