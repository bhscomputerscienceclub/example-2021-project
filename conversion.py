def numbertoletterandgpa(numbergrade):
    if numbergrade >= 93.5:
        return ("A", 4.0)
    elif numbergrade >= 89.5:
        return ("A-", 3.7)
    elif numbergrade >= 86.5:
        return ("B+", 3.3)
    elif numbergrade >= 82.5:
        return ("B", 3.0)
    elif numbergrade >= 79.5:
        return ("B-", 2.7)
    elif numbergrade >= 76.5:
        return ("C+", 2.3)
    elif numbergrade >= 72.5:
        return ("C", 2.0)
    elif numbergrade >= 69.5:
        return ("C-", 1.7)
    elif numbergrade >= 66.5:
        return ("D+", 1.3)
    elif numbergrade >= 62.5:
        return ("D", 1.0)
    elif numbergrade >= 59.5:
        return ("D-", 0.7)
    else:
        return ("F", 0.0)