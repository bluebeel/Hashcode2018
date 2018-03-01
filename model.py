import sys

from model import *
import parser


def main():
    filename = "a_example.in"
    parsed = parser.parse(filename)
    R, C, F, N, B, T = parsed[0]
    town = [[0 for x in range(C)] for y in range(R)]
    town[0][0] = 1
    rides = []
    for ride in parsed[1]:
        a, b, x, y, s, f = list(map(int, ride.rstrip().split()))
        rides.append(((a, b), (x, y), (s, f)))
    print(rides)


    # Some logic

    out = ''
    with open(filename + '.in', 'w') as t:
        t.write(out)


if __name__ == '__main__':
    main()
