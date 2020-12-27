from flask import Flask, render_template, request
from InfiniteCampus import IC_grades
from thing import Data

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def function():
    ret = []
    Invalid_Number = False
    Invalid_User = False
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        try:
            semester_grade_wanted = int(request.form.get("semester_grade_wanted"))
            q1_grade_wanted = int(request.form.get("q1_grade_wanted"))
            q2_grade_wanted = int(request.form.get("q2_grade_wanted"))
            assignment_pts = int(request.form.get("assignment_pts"))
            grades = IC_grades(username, password)
        except ValueError:
            Invalid_Number = True
        except KeyError:
            Invalid_User = True
        else:
            
            li = list()
            for i in range(0, len(grades[0]["courses"])):
                if (
                    "PHYSICS"
                    not in grades[0]["courses"][i]["gradingTasks"][0]["courseName"]
                ):
                    li.append(
                        Data(
                            i,
                            grades,
                            semester_grade_wanted,
                            q1_grade_wanted,
                            q2_grade_wanted,
                        )
                    )
            for i in range(0, len(li)):
                ret.append([])
                ret[i].append(li[i].course_name)
                ret[i].append(li[i].exam_percent_needed())
                ret[i].append(li[i].bonus_needed())
                ret[i].append(li[i].assignment_percent_needed(assignment_pts))
    return render_template("index.html", Invalid_User = Invalid_User, Invalid_Number = Invalid_Number, len=len(ret), ret=ret)


app.run(use_reloader=True, debug=True, port=5001)
