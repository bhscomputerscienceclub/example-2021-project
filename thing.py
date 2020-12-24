from main import numbertoletterandgpa
from main import semestergradepercent


class Data:
    def _init_(self, q1_percent, q1_a_pts, q1_t_pts, q2_percent, q2_a_pts, q2_t_pts):
        course = self
        self.q1_percent = q1_percent
        self.q1_a_pts = q1_a_pts
        self.q1_t_pts = q1_t_pts
        self.q2_percent = q2_percent
        self.q2_a_pts = q2_a_pts
        self.q2_t_pts = q2_t_pts
        self.classtype = "no_exam"  # fix this
        self.semester_grade_wanted = 95  # fix this
        self.q1_grade_wanted = 90  # fix this
        self.q2_grade_wanted = 95  # fix this

    def exampercentneeded(self):
        examgrade = 0
        while (
            semestergradepercent(
                self.q1_percent, self.q2_percent, examgrade, self.classtype
            )
            < self.semester_grade_wanted
        ):
            examgrade += 0.1
        return examgrade

    def bonusneeded(self):
        bonuspoints = 0
        while (
            (self.q2_a_pts + bonuspoints) / self.q2_t_pts
        ) * 100 < self.q2_grade_wanted:
            bonuspoints += 0.5
        return bonuspoints

    def assignmentpercentneeded(self, assignment_total_pts):
        assignment_achieved_pts = 0
        while (
            (self.q2_a_pts + assignment_achieved_pts)
            / (self.q2_t_pts + assignment_total_pts)
        ) * 100 < self.q2_grade_wanted:
            assignment_achieved_pts += 0.5
        return assignment_achieved_pts
