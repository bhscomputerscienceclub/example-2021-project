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

def semestergrade(grade1, grade2, exam, classtype):
  if classtype == "noexam":
    semesternumbergrade = 0.5*grade1 + 0.5*grade2
  elif classtype == "ap":
    semesternumbergrade = 0.375*grade1 + 0.375*grade2 + 0.25*exam
  else:
    semesternumbergrade = 0.4*grade1 + 0.4*grade2 + 0.2*exam
  
  print("Percent:" + str(semesternumbergrade))
  letterandgpa = numbertoletterandgpa(semesternumbergrade)
  print("Grade:" + str(letterandgpa[0]))
  print("GPA:" + str(letterandgpa[1]))
