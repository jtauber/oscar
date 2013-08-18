

def value(name):
    base = "FCGDAEB".find(name[0])
    if base == -1:
        raise ValueError
    return base + 7 * {"bb": -2, "b": -1, "": 0, "#": 1, "x": 2}[name[1:]]


def name(val):
    return "FCGDAEB"[val % 7] + {
        -2: "bb", -1: "b", 0: "", 1: "#", 2: "x"
    }[val // 7]
