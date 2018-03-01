
def parse(filename):
    with open(filename) as f:
        inputstr = f.readlines()
    firstline = list(map(int, inputstr[0].split()))
    return (firstline, inputstr[1:])

filename = "e_high_bonus.in"
parsed = parse(filename)
R, C, F, N, B, T = parsed[0]
town = [[0 for x in range(C)] for y in range(R)]
town[0][0] = 1
px, py, ha = 0, 0, 0
rides = []
scores = []


for i, ride in enumerate(parsed[1]):
    a, b, x, y, s, f = list(map(int, ride.rstrip().split()))
    rides.append(((a, b), (x, y), (s, f))) # liste tous les rides
    score = (abs(x-a)+abs(y-b))**2 / (max(abs(px-a) + abs(py-b), f-ha))

    scores.append((i, score))


scores.sort(key=lambda tup: tup[1])
scores.reverse()
res = []
for v in range(1, F+1):
    res.append([v, [scores[v-1][0]]])
print(res)

out = ''
with open(filename + '.out', 'w') as t:
    for line in res:
        out += "{} ".format(len(line[1]))
        out += ' '.join(map(str, line[1]))
        out += '\n'
    t.write(out)

print(res)
