''' How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)? '''

def main():
    ''' Finds the day at the start of each month. Sunday occurs when day=0. The
    start year is 1901 '''
    year, day, sundays = 1, 2, 0
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while year < 101:
        for n in range(12):
            if year % 4 == 0 and n == 1:
                day = (months[n] + day + 1) % 7
            else:
                day = (months[n] + day) % 7
            if day == 0 and (n != 12 or year != 101):
                sundays += 1
        year += 1
    print(sundays)

if __name__ == "__main__":
    main()
