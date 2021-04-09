''' Find the last 8 digits of 1777^^1855 (^^ denotes hyperexponentiation) '''

def main():
    ''' Driver function '''
    val = 1
    mod = 10**8
    for _ in range(1855):
        val = pow(1777, val, mod)
    print(val)

if __name__ == "__main__":
    main()
