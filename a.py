def exam_percent_needed(classtype, semester_grade_wanted, q1_percent,q2_percent):
        if classtype == "no_exam":
            return "N/A"
        exam_grade = 4*semester_grade_wanted-1.5*q1_percent-1.5*q2_percent
        exam_grade = 5*semester_grade_wanted-2*q1_percent-2*q2_percent
        return exam_grade
        
print(exam_percent_needed('ap',95,100,100))