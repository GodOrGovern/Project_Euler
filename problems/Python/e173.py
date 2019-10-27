''' We shall define a square lamina to be a square outline with a square "hole"
so that the shape possesses vertical and horizontal symmetry. Using up to one
million tiles how many different square laminae can be formed? '''

def main():
    ''' Driver function '''
    print(laminae(10**6))

def laminae(max_tiles):
    ''' Determines how many different laminae can be formed using 'max_tiles'
    tiles '''
    hole_length = 1
    cur = laminae_num(hole_length, max_tiles)
    total = cur
    while cur:
        hole_length += 1
        cur = laminae_num(hole_length, max_tiles)
        total += cur
    return total

def laminae_num(hole_length, max_tiles):
    ''' Determines how many different laminae can be formed with a hole having
    side-length 'hole_length' and using up to 'max_tiles' tiles '''
    perimeter = hole_length*4 + 4
    total_tiles = perimeter
    count = 0
    while total_tiles <= max_tiles:
        count += 1
        perimeter += 8
        total_tiles += perimeter
    return count

if __name__ == "__main__":
    main()
