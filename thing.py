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
        elif self.classtype == "ap":
            return (
                4 * self.semester_grade_wanted
                - 1.5 * self.q1_percent
                - 1.5 * self.q2_percent
            )
        else:
            return (
                5 * self.semester_grade_wanted
                - 2 * self.q1_percent
                - 2 * self.q2_percent
            )

    def bonus_needed(self):
        if (self.q2_grade_wanted / 100 * self.q2_t_pts) - self.q2_a_pts > 0:
            return (self.q2_grade_wanted / 100 * self.q2_t_pts) - self.q2_a_pts
        else:
            return 0

    def assignment_percent_needed(self, assignment_total_pts):
        return (
            (
                self.q2_grade_wanted / 100 * (self.q2_t_pts + assignment_total_pts)
                - self.q2_a_pts
            )
            / assignment_total_pts
            * 100
        )

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