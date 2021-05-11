''' Using a combination of grey square tiles and oblong tiles chosen from: red
tiles (measuring two units), green tiles (measuring three units), and blue
tiles (measuring four units) how many ways can a row measuring fifty units in
length be tiled '''

from euler import tilings

def main():
    ''' Driver function '''
    # One is added to account for tiling with no blocks
    print(tilings(50, 2, 4, mix_lengths=True)+1)

if __name__ == "__main__":
    main()
