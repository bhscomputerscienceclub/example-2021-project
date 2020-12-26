from flask import Flask, render_template, request
from InfiniteCampus import IC_grades
from thing import Data
app = Flask(__name__)



@app.route('/',  methods=["GET", "POST"])
def function():
    a = ''
    b = ''
    c = ''
    d = ''
    e = ''
    
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        semester_grade_wanted = int(request.form.get('semester_grade_wanted'))
        q1_grade_wanted = int(request.form.get('q1_grade_wanted'))
        q2_grade_wanted = int(request.form.get('q2_grade_wanted'))
        class_type = request.form.get('class_type')
        assignment_pts = int(request.form.get('assignment_pts'))
        grades = IC_grades(username,password)
        li = list()
        for i in range(0, len(grades[0]["courses"])):
            if "PHYSICS" not in grades[0]["courses"][i]["gradingTasks"][0]["courseName"]:
                li.append(Data(i,grades,semester_grade_wanted,q1_grade_wanted,q2_grade_wanted,class_type))
        a = li[0].course_name
        b = li[0].bonus_needed()
        c = li[0].exam_percent_needed()
        d = li[0].assignment_percent_needed(assignment_pts)
        e = ''
    return render_template('index.html',a=a, b=b,c=c,d=d,e=e)

app.run(debug=True,port=5001)