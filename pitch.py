

def value(name):
    base = "FCGDAEB".find(name[0])
    if base == -1:
        raise ValueError
    return base + 7 * {"bb": -2, "b": -1, "": 0, "#": 1, "x": 2}[name[1:]]


def name(val):
    return "FCGDAEB"[val % 7] + {
        -2: "bb", -1: "b", 0: "", 1: "#", 2: "x"
    }[val // 7]


INTERVAL_1 = ("d" * 7 + "m" * 4 + "P" * 3 + "M" * 4 + "A" * 7)
INTERVAL_2 = "2637415" * 4


def interval_name(val):
    return INTERVAL_1[val + 12] + INTERVAL_2[val + 12]


def interval_value(name):
    s = INTERVAL_1.find(name[0])
    return s + INTERVAL_2[s:].index(name[1]) - 12
