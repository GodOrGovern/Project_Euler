''' A modified Collatz sequence of integers is obtained from a starting value
a_1 in the following way:
    a_{n+1} = (1*a_n + 0) / 3 if a_n = 0 (mod 3) ("D")
              (4*a_n + 2) / 3 if a_n = 1 (mod 3) ("U")
              (2*a_n - 1) / 3 if a_n = 2 (mod 3) ("d")
The sequence terminates when some a_n = 1. Given any integer, we can list out
the sequence of steps. What is the smallest a_1 that begins with the sequence
"UDDDUdddDDUDDddDdDddDDUDDdUUDd"? '''

def main():
    ''' Driver function '''
    print(get_smallest_a("UDDDUdddDDUDDddDdDddDDUDDdUUDd", 10**15))

def get_smallest_a(sequence, low):
    ''' Return the smallest a_1 > low that produces a modified Collatz sequence
    beginning with the parameter sequence '''
    # Treating a_1 as a variable, all numbers in the resulting sequence will be
    # of the form (x*a+y)/z where x, y, z are integers. Any given series of steps
    # produces a unique (x, y, z) triple which can be determined by iteratively
    # plugging the current values into the equation for the current step
    x, y, z = 1, 0, 1
    for step in sequence:
        if step == 'D':
            x, y, z = x, y, 3*z
        elif step == 'U':
            x, y, z = 4*x, 2*z+4*y, 3*z
        elif step == 'd':
            x, y, z = 2*x, 2*y-z, 3*z
    # (x*a + y) = 0 (mod z) so a = (x^-1)*(-y) (mod z)
    a_1 = pow(x, -1, z)*(-y) % z
    return z*((low//z)+1) + a_1


if __name__ == "__main__":
    main()
