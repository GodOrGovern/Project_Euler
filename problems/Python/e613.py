''' Dave is doing his homework on the balcony and, preparing a presentation
about Pythagorean triangles, has just cut out a triangle with side lengths
30cm, 40cm and 50cm from some cardboard, when a gust of wind blows the triangle
down into the garden. Another gust blows a small ant straight onto this
triangle. The poor ant is completely disoriented and starts to crawl straight
ahead in random direction in order to get back into the grass. Assuming that
all possible positions of the ant within the triangle and all possible
directions of moving on are equiprobable, what is the probability that the ant
leaves the triangle along its longest side?  Give your answer rounded to 10
digits after the decimal point. '''

from math import pi, acos
from scipy.integrate import dblquad

def main():
    ''' Uses Law of Cosines to find a function for the angle formed by (0, 0),
    (30, 40), and (x, y). This function is then integrated over the boundary of
    the triangle and divided by the area and 2*pi to obtain an average
    percentage for that angle '''
    f = lambda x, y: pi-acos((-x**2-y**2+30*x+40*y)/((x**2+y**2)**0.5*((30-x)**2+(40-y)**2)**0.5))
    chance = dblquad(f, 0, 40, lambda x: 0.75*x, lambda x: 30)[0] / 600 / (2*pi)
    print(str(chance)[:12])

if __name__ == "__main__":
    main()
