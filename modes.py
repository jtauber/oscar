def mode(n):
    X = [i % 7 for i in range(0, 13, 2)]
    mode = [([-7] * n + [0] * (7 - n))[6 - j] for j in X]
    return [a + b for a, b in zip(mode, X)]


LYDIAN, IONIAN, MIXOLYDIAN, DORIAN, AEOLIAN, PHRYGIAN, LOCRIAN = (
    mode(i) for i in range(7)
)
