def parse(filename):
    with open(filename) as f:
        inputstr = f.readlines()
    firstline = list(map(int, inputstr[0].split()))
    return (firstline, inputstr[1:])
