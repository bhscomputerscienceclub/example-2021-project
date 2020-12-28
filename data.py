from InfiniteCampus import IC_grades


class Data:
    def __init__(
        self,
        course_num,
        grades,
        semester_grade_wanted,
        q1_grade_wanted,
        q2_grade_wanted,
    ):

        
        if 'AP' in grades[0]["courses"][course_num]["gradingTasks"][0]["courseName"]:
            self.gpatype = "ap"
        elif 'HONORS' in grades[0]["courses"][course_num]["gradingTasks"][0]["courseName"]:
            self.gpatype = "honors"
        else:
            self.gpatype = "regular"

        self.class_type = "no_exam" #for this school year

        self.semester_grade_wanted = semester_grade_wanted
        self.q1_grade_wanted = q1_grade_wanted
        self.q2_grade_wanted = q2_grade_wanted

        self.course_name = grades[0]["courses"][course_num]["gradingTasks"][0][
            "courseName"
        ]
        self.q1_percent = grades[0]["courses"][course_num]["gradingTasks"][0][
            "progressPercent"
        ]
        self.q2_percent = grades[1]["courses"][course_num]["gradingTasks"][0][
            "progressPercent"
        ]
        self.q1_a_pts = grades[0]["courses"][course_num]["gradingTasks"][0][
            "progressPointsEarned"
        ]
        self.q2_a_pts = grades[1]["courses"][course_num]["gradingTasks"][0][
            "progressPointsEarned"
        ]
        self.q1_t_pts = grades[0]["courses"][course_num]["gradingTasks"][0][
            "progressTotalPoints"
        ]
        self.q2_t_pts = grades[1]["courses"][course_num]["gradingTasks"][0][
            "progressTotalPoints"
        ]
        self.q1_letter_grade = grades[0]["courses"][course_num]["gradingTasks"][0][
            "score"
        ]
        self.q2_letter_grade = grades[1]["courses"][course_num]["gradingTasks"][0][
            "score"
        ]

    def exam_percent_needed(self):
        if self.class_type == "no_exam":
            return "N/A"
        elif self.class_type == "ap":
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
            
    def q2_bonus_needed(self):
        if (self.q2_grade_wanted / 100 * self.q2_t_pts) - self.q2_a_pts > 0:
            return (self.q2_grade_wanted / 100 * self.q2_t_pts) - self.q2_a_pts
        else:
            return 0

    def q2_assignment_percent_needed(self, assignment_total_pts):
        return (
            (
                self.q2_grade_wanted / 100 * (self.q2_t_pts + assignment_total_pts)
                - self.q2_a_pts
            )
            / assignment_total_pts
            * 100
        )
