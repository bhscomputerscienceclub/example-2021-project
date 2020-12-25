from main import numbertoletterandgpa
from main import semestergradepercent
from main import grades


class Data:
    def __init__(self, coursenum):
        self.classtype = "no_exam"  # fix this
        self.semester_grade_wanted = 98  # fix this
        self.q1_grade_wanted = 10  # doesnt matter
        self.q2_grade_wanted = 99  # fix this

        self.course_name = grades[0]["courses"][coursenum]["gradingTasks"][0][
            "courseName"
        ]
        self.q1_percent = grades[0]["courses"][coursenum]["gradingTasks"][0][
            "progressPercent"
        ]
        self.q2_percent = grades[1]["courses"][coursenum]["gradingTasks"][0][
            "progressPercent"
        ]
        self.q1_a_pts = grades[0]["courses"][coursenum]["gradingTasks"][0][
            "progressPointsEarned"
        ]
        self.q2_a_pts = grades[1]["courses"][coursenum]["gradingTasks"][0][
            "progressPointsEarned"
        ]
        self.q1_t_pts = grades[0]["courses"][coursenum]["gradingTasks"][0][
            "progressTotalPoints"
        ]
        self.q2_t_pts = grades[1]["courses"][coursenum]["gradingTasks"][0][
            "progressTotalPoints"
        ]

    def exam_percent_needed(self):
        if self.classtype == "no_exam":
            return "N/A"
        examgrade = 0
        while (
            semestergradepercent(
                self.q1_percent, self.q2_percent, examgrade, self.classtype
            )
            < self.semester_grade_wanted
        ):
            examgrade += 0.1
        return examgrade

    def bonus_needed(self):
        return (self.q2_grade_wanted/100*self.q2_t_pts)-self.q2_a_pts

    def assignment_percent_needed(self, assignment_total_pts):
        return (self.q2_grade_wanted(self.q2_t_pts + assignment_total_pts) - self.q2_a_pts) / assignment_total_pts


# course_name = grades[0]["courses"][0]["gradingTasks"][0]["courseName"]
# q1_percent = grades[0]["courses"][0]["gradingTasks"][0]["progressPercent"]
# q2_percent = grades[1]["courses"][0]["gradingTasks"][0]["progressPercent"]
# q1_a_pts = grades[0]["courses"][0]["gradingTasks"][0]["progressPointsEarned"]
# q2_a_pts = grades[1]["courses"][0]["gradingTasks"][0]["progressPointsEarned"]
# q1_t_pts = grades[0]["courses"][0]["gradingTasks"][0]["progressTotalPoints"]
# q2_t_pts = grades[1]["courses"][0]["gradingTasks"][0]["progressTotalPoints"]
li = list()
for i in range(0, len(grades[0]["courses"])):
    if "PHYSICS" not in grades[0]["courses"][i]["gradingTasks"][0]["courseName"]:
        li.append(Data(i))

for i in range(len(li)):
    print("Course Name = ", li[i].course_name)
    print("Bonus Needed = ", li[i].bonus_needed())
    print("Exam Percent Needed = ", li[i].exam_percent_needed())
    print("Assignment Percent Needed = ", li[i].assignment_percent_needed(50))
    print()
