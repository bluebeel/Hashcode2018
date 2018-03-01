import sys
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
    res = []
    visited = []

    for vehicle in range(1, F+1):
        print("Vehicle {}".format(vehicle))
        v_rides = []
        for i, ride in enumerate(rides):
            if ride not in visited:
                print("---- RIDE ----")
                start = town[0][0]
                step = 0
                if town[ride[0][0]][ride[0][1]] != 1:
                    print("The ride starting point is different from the start point")
                    print("Let's move to the starting ride point")
                    step += abs(ride[0][0]-0) + abs(ride[0][1]-0)
                if step < ride[2][0]:
                    print("The rider should wait: {} more".format(ride[2][0]-step))
                    step += ride[2][0]
                print("We are at step {} the ride start now".format(step))
                step += abs(ride[0][0]-ride[1][0]) + abs(ride[0][1]-ride[1][1])
                print("We are at step {} the ride finished, moved from ({},{}) to ({},{})".format(step, ride[0][0], ride[0][1], ride[1][0], ride[1][1]))
                if step < ride[2][1]:
                    print("Finished earlier, {} steps left".format(T - step))
                    visited.append(ride)
                    town[ride[1][0]][ride[1][1]] = 1
                    for i, ride in enumerate(rides):
                        if ride not in visited:
                            print("---- RIDE ----")
                            if town[ride[0][0]][ride[0][1]] != 1:
                                print("The ride starting point is different from the actual point")
                                print("Let's move to the starting ride point")
                                step += abs(ride[0][0]-0) + abs(ride[0][1]-0)
                            if step < ride[2][0]:
                                print("The rider should wait: {} more".format(ride[2][0]-step))
                                step += ride[2][0]
                            print("We are at step {} the ride start now".format(step))
                            step += abs(ride[0][0]-ride[1][0]) + abs(ride[0][1]-ride[1][1])
                            print("We are at step {} the ride finished, moved from ({},{}) to ({},{})".format(step, ride[0][0], ride[0][1], ride[1][0], ride[1][1]))
                            if step < ride[2][1]:
                                print("Finished in time, {} steps".format(step))
                                v_rides.append(i)
                                visited.append(ride)
                                break;
                            elif step <= T:
                                print("finished in the given limit")
                                v_rides.append(i)
                                visited.append(ride)
                                break;
                            else:
                                print("Finished later")
                                pass
                else:
                    print("Finished later")
                    v_rides.append(i)
                    print("We delete this ride")
                    visited.append(ride)
                    break

        res.append([vehicle, v_rides])

    print(res)


    # Some logic

    out = ''
    with open(filename + '.out', 'w') as t:
        for line in res:
            out += "{} ".format(len(line[1]))
            out += ''.join(map(str, line[1]))
            out += '\n'
        t.write(out)


if __name__ == '__main__':
    main()
