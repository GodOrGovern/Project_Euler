''' Working from left-to-right if no digit is exceeded by the digit to its left
it is called an increasing number. Similarly if no digit is exceeded by the
digit to its right it is called a decreasing number.  We shall call a positive
integer that is neither increasing nor decreasing a "bouncy" number. Find the
least number for which the proportion of bouncy numbers is exactly 99%. '''

def main():
    ''' Checks if the number is equal when sorted or reverse sorted. Otherwise
    'bouncy' is incremented '''
    bouncy, num = 0, 100
    while bouncy / num < 0.99:
        num += 1
        n = list(str(num))
        n_sort = sorted(n)
        bouncy += n_sort != n and n_sort[::-1] != n
    print(num)

if __name__ == "__main__":
    main()
