from main import numbertoletterandgpa
from main import semestergradepercent

def exampercentneeded(grade1, grade2, classtype, semestergradewanted):
    examgrade = 0
    while semestergradepercent(grade1, grade2, examgrade, classtype) < semestergradewanted:
        examgrade += .1
    return(examgrade)

def bonusneeded(bcurrentpoints, btotalpoints, bonusgradewanted):
    bonuspoints = 0
    while ((bcurrentpoints + bonuspoints)/btotalpoints)*100 < bonusgradewanted:
        bonuspoints += 0.5
    return(bonuspoints)

def assignmentpercentneeded(acurrentpoints, atotalpoints, assignmenttotalpoints, assignmentgradewanted):
    assignmentachievedpoints = 0
    while ((acurrentpoints + assignmentachievedpoints)/(atotalpoints + assignmenttotalpoints))*100 < assignmentgradewanted:
        assignmentachievedpoints += 0.5
    return(assignmentachievedpoints)
