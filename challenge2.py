def isLeapYear(year):
  return bool(year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
year=int(input("Enter a year"))
if isLeapYear(year):
    print('{}is a leapyear.'.format(year))
else:
    print('{}is not a leapyear.'.format(year))