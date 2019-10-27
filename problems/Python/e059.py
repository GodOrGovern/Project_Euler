''' Using the source file, which contains the encrypted ASCII codes, and the
knowledge that the plain text must contain common English words, decrypt the
message and find the sum of the ASCII values in the original text. '''

from itertools import permutations
from euler import src

def main():
    ''' Driver function '''
    encrypted = [int(n) for n in open(src+'e059').read().split(',')]
    decrypted = test_keys(encrypted)
    print(sum([ord(c) for c in decrypted]))

def test_keys(encrypted):
    ''' Brute-force decryption of 'encrypted' by testing possible keys '''
    key_vals = [x for x in range(97, 123)]
    for p in permutations(key_vals, 3):
        decrypted = decrypt(encrypted, p)
        if ' the ' in decrypted:
            return decrypted
    return ''

def decrypt(encrypted, key):
    ''' Decrypt 'encrypted' data by XORing with 'key'. Convert result using ASCII
    codes '''
    decrypted = ''
    key_len = len(key)
    for i, n in enumerate(encrypted):
        decrypted += chr(n ^ key[i % key_len])
    return decrypted

if __name__ == "__main__":
    main()
