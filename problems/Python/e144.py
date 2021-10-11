''' In laser physics, a "white cell" is a mirror system that acts as a delay
line for the laser beam. The beam enters the cell, bounces around on the
mirrors, and eventually works its way back out. The specific white cell we will
be considering is an ellipse with the equation 4x**2 + y**2 = 100 The section
corresponding to −0.01 ≤ x ≤ +0.01 at the top is missing, allowing the light to
enter and exit through the hole. The light beam in this problem starts at the
point (0.0,10.1) just outside the white cell, and the beam first impacts the
mirror at (1.4,-9.6). Each time the laser beam hits the surface of the ellipse,
it follows the usual law of reflection "angle of incidence equals angle of
reflection." That is, both the incident and reflected beams make the same angle
with the normal line at the point of incidence. In the figure on the left, the
red line shows the first two points of contact between the laser beam and the
wall of the white cell; the blue line shows the line tangent to the ellipse at
the point of incidence of the first bounce. The slope m of the tangent line at
any point (x,y) of the given ellipse is: m = −4x/y The normal line is
perpendicular to this tangent line at the point of incidence. How many times
does the beam hit the internal surface of the white cell before exiting?  '''

from math import pi, tan, atan

def main():
    ''' Counts the number of times the light beam reflects off the ellipse
    before escaping and prints that value '''
    count = 0
    p1, p2 = (0, 10.1), (1.4, -9.6)
    while not (-0.01 < p2[0] < 0.01) or p2[1] < 0:
        count += 1
        p1, p2 = p2, intersect(p2, *new_line(p1, p2))
    print(count)

def new_line(p1, p2):
    ''' Returns the slope and y-intercept of the light beam originating at
    point p1 after it reflects off point p2. '''
    (x1, y1), (x2, y2) = p1, p2
    m1 = (y1 - y2) / (x1 - x2)
    m2 = -4*x2 / y2
    m3 = tan(pi + 2*atan(m2) - atan(m1))
    c3 = y2 - m3*x2
    return m3, c3

def intersect(p, m, c):
    ''' Returns the point where the light beam represented by the equation
    y=mx+c and originating at point p intersects with the ellipse '''
    # From the equation for the ellipse (x**2 / a**2) + (y**2 / b**2) = 1
    a, b = 5, 10
    t1 = -a**2*m*c
    t2 = a*b*(a**2*m**2 + b**2 - c**2)**0.5
    t3 = b**2 + a**2*m**2
    # Two points of intersection, but one is p
    x1 = (t1 + t2) / t3
    x2 = (t1 - t2) / t3
    new_x = x1 if (abs(p[0]-x1) > abs(p[0]-x2)) else x2
    new_y = m*new_x + c
    return new_x, new_y

if __name__ == "__main__":
    main()
