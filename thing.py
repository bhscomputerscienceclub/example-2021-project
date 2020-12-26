from InfiniteCampus import IC_grades




class Data:
    def __init__(self, course_num, grades, semester_grade_wanted, q1_grade_wanted, q2_grade_wanted, class_type):

        # uncomment this when normal school schedule
        # if 'AP' in grades[0]["courses"][coursenum]["gradingTasks"][0]["courseName"]:
        #     self.classtype = "ap"
        # else:
        #     self.classtype = "regular"

        # self.class_type = "no_exam"
        # self.semester_grade_wanted = 98  # will be user input
        # self.q1_grade_wanted = 10  # will be user input
        # self.q2_grade_wanted = 99  # will be user input


        
        self.semester_grade_wanted = semester_grade_wanted
        self.q1_grade_wanted = q1_grade_wanted
        self.q2_grade_wanted = q2_grade_wanted
        self.class_type = class_type


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
