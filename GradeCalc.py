from flask import Flask, render_template, request, redirect, url_for
from InfiniteCampus import IC_grades
from data import Data
import random

app = Flask(__name__)

userdata = {}


@app.route("/", methods=["GET", "POST"])
def function():
    global userdata
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

            li = []
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
                ret[i].append(li[i].q2_bonus_needed())
                ret[i].append(li[i].q2_assignment_percent_needed(assignment_pts))

            num = random.randint(1, 10000000000000000000000)
            while userdata.get(num, False):
                num = random.randint(1, 10000000000000000000000)
            userdata[num] = ret
            return redirect(url_for("functionn", ret=num))
    return render_template(
        "index.html", Invalid_User=Invalid_User, Invalid_Number=Invalid_Number
    )


@app.route("/results", methods=["GET", "POST"])
def functionn():
    try:
        num = int(request.args["ret"])
        ret = userdata[num]
    except:
        return redirect(url_for("function", Invalid_User=False, Invalid_Number=False))

    return render_template("results.html", len=len(ret), ret=ret)


app.run(use_reloader=True, debug=True, port=5001)
