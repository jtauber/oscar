def mode(n):
    """
    returns the offsets from the tonic (in circle-of-fifth steps) for mode n
    """
    return [
        ((2 * i) % 7) + ([-7] * n + [0] * (7 - n))[6 - ((2 * i) % 7)]
        for i in range(7)
    ]


LYDIAN, IONIAN, MIXOLYDIAN, DORIAN, AEOLIAN, PHRYGIAN, LOCRIAN = (
    mode(i) for i in range(7)
)
