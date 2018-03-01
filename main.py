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

    for vehicle in range(1, F+1):
        print("Vehicle {}".format(vehicle))
        for ride in rides:
            start = town[0][0]
            step = 0
            if town[ride[0][0]][ride[0][1]] != 1:
                print("The ride starting point is different from the start point")
                step += abs(a-0) + abs(b-0)
                print("Steps number: {}".format(step))

    # Some logic

    out = ''
    with open(filename + '.in', 'w') as t:
        t.write(out)


if __name__ == '__main__':
    main()
