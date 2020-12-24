from main import numbertoletterandgpa
from main import semestergradepercent
from main import grades


class Data:
    def __init__(self, coursenum):
        # course = self
        # self.q1_percent = q1_percent
        # self.q1_a_pts = q1_a_pts
        # self.q1_t_pts = q1_t_pts
        # self.q2_percent = q2_percent
        # self.q2_a_pts = q2_a_pts
        # self.q2_t_pts = q2_t_pts
        self.classtype = "no_exam"  # fix this
        self.semester_grade_wanted = 98  # fix this
        self.q1_grade_wanted = 98  # fix this
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
        bonuspoints = 0
        while (
            (self.q2_a_pts + bonuspoints) / self.q2_t_pts
        ) * 100 < self.q2_grade_wanted:
            bonuspoints += 0.5
        return bonuspoints

    def assignment_percent_needed(self, assignment_total_pts):
        assignment_achieved_pts = 0
        while (
            (self.q2_a_pts + assignment_achieved_pts)
            / (self.q2_t_pts + assignment_total_pts)
        ) * 100 < self.q2_grade_wanted:
            assignment_achieved_pts += 0.5
        return assignment_achieved_pts


# course_name = grades[0]["courses"][0]["gradingTasks"][0]["courseName"]
# q1_percent = grades[0]["courses"][0]["gradingTasks"][0]["progressPercent"]
# q2_percent = grades[1]["courses"][0]["gradingTasks"][0]["progressPercent"]
# q1_a_pts = grades[0]["courses"][0]["gradingTasks"][0]["progressPointsEarned"]
# q2_a_pts = grades[1]["courses"][0]["gradingTasks"][0]["progressPointsEarned"]
# q1_t_pts = grades[0]["courses"][0]["gradingTasks"][0]["progressTotalPoints"]
# q2_t_pts = grades[1]["courses"][0]["gradingTasks"][0]["progressTotalPoints"]

a = Data(1)
print(a.course_name)
print(a.bonus_needed())
print(a.exam_percent_needed())
print(a.assignment_percent_needed(1))
