def numbertoletterandgpa(numbergrade):
    if numbergrade >= 93.5:
        return ("A")
    elif numbergrade >= 89.5:
        return ("A-")
    elif numbergrade >= 86.5:
        return ("B+")
    elif numbergrade >= 82.5:
        return ("B")
    elif numbergrade >= 79.5:
        return ("B-")
    elif numbergrade >= 76.5:
        return ("C+")
    elif numbergrade >= 72.5:
        return ("C")
    elif numbergrade >= 69.5:
        return ("C-")
    elif numbergrade >= 66.5:
        return ("D+")
    elif numbergrade >= 62.5:
        return ("D")
    elif numbergrade >= 59.5:
        return ("D-")
    else:
        return ("F")