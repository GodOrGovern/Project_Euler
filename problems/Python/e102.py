''' Using the source file containing the co-ordinates of one thousand "random"
triangles, find the number of triangles for which the interior contains the
origin '''

from euler import src_file

def main():
    ''' Driver function '''
    triangles = load_triangles(src_file('e102'))
    print(sum(origin_in(t) for t in triangles))

def load_triangles(infile):
    ''' Load coordinate points specifying vertices of triangles from 'infile'
    and return in 'triangles' '''
    triangles = []
    with open(infile) as data:
        for line in data:
            triangle = []
            cords = line.strip().split(',')
            for i, p in enumerate(cords[::2]):
                triangle.append([int(p), int(cords[2*i+1])])
            triangles.append(triangle)
    return triangles

def origin_in(ABC):
    ''' Determine if the origin lies within triangle 'ABC' '''
    origin = [0, 0]
    area1 = tri_area([ABC[0], ABC[1], origin])
    area2 = tri_area([ABC[0], ABC[2], origin])
    area3 = tri_area([ABC[1], ABC[2], origin])
    total_area = tri_area(ABC)
    return total_area == area1 + area2 + area3

def tri_area(tri):
    ''' Return the area of 'tri' '''
    return abs((tri[0][0] * (tri[1][1] - tri[2][1]) +
                tri[1][0] * (tri[2][1] - tri[0][1]) +
                tri[2][0] * (tri[0][1] - tri[1][1])) / 2)

if __name__ == "__main__":
    main()
