''' A square is drawn around a circle as shown in the diagram below on the
left. We shall call the blue shaded region the L-section. We shall call the
orange shaded region a concave triangle. What is the least value of n for which
the concave triangle occupies less than 0.1% of the L-section? '''

from math import pi
from scipy.integrate import quad

def main():
    ''' Area of L is a constant. Area of concave triangle found by breaking
    region into two sections and finding their areas. First is a right triangle
    with width 'y_intersect' and height 'x_intersect'. These are the (x, y)
    coordinates of where the circle and the line intersect. The other region's
    area is found by integrating from 'x_intersect' to 1 over the function for
    the bottom half of the circle '''
    n = 1
    l_area = (4 - pi) / 4
    triangle_area = l_area
    f = lambda x: 1 - (2*x-x**2)**0.5
    while triangle_area / l_area > 0.001:
        y_intersect = (n + 1 - n*(2/n)**0.5) / (n**2 + 1)
        x_intersect = y_intersect * n
        triangle_area = x_intersect * y_intersect / 2
        triangle_area += quad(f, x_intersect, 1)[0]
        n += 1
    print(n-1)

if __name__ == "__main__":
    main()
