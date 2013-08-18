def mode(mode_number):
    X = [0, 2, 4, 6, 1, 3, 5]
    mode = [([-7] * mode_number + [0] * (7 - mode_number))[6 - j] for j in X]
    return [a + b for a, b in zip(mode, X)]


LYDIAN, IONIAN, MIXOLYDIAN, DORIAN, AEOLIAN, PHRYGIAN, LOCRIAN = (
    mode(i) for i in range(7)
)
