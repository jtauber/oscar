lydian = [0, 0, 0, 1, 0, 0, 0]
ionian = [0, 0, 0, 0, 0, 0, 0]
mixolydian = [0, 0, 0, 0, 0, 0, -1]
dorian = [0, 0, -1, 0, 0, 0, -1]
aeolian = [0, 0, -1, 0, 0, -1, -1]
phrygian = [0,-1, -1, 0, 0, -1, -1]
locrian = [0, -1, -1, 0, -1, -1, -1]

A = (0, aeolian)
B = (1, locrian)
C = (2, ionian)
D = (3, dorian)
E = (4, phrygian)
F = (5, lydian)
G = (6, mixolydian)

tonic = E
mode = locrian

def perm(l, n):
    return l[n:] + l[:n]


print [
    "ABCDEFG"[a] +
    {-2: "bb", -1: "b", 0: "", 1: "#", 2: "x"}[b]
    for a, b in zip(
       perm(range(7), tonic[0]),
       [a - b for a, b in zip(mode, tonic[1])]
    )
]
