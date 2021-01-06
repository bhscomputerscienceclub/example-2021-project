def physicsgradepercent(m, p, a, b, zeros, level):
    if level == "1":
        return 100*(.95*m + 0.8*p + 0.65*a + 0.45*b)/(m+p+a+b+zeros)
    if level == "2" or level == "c":
        return 100*(m + 0.8*p + 0.6*a + 0.4*b)/(m+p+a+b+zeros)