from flask import Flask, render_template, request






app = Flask(__name__)

def categorize_grade(marks):
    """
    Categorize student grades as Pass or Fail based on a passing criterion (e.g, passing grade 50).
    """
    return "Pass" if marks>= 50 else "Fail"
@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        student_name = request.form["name"]
        student_marks = int(request.form["marks"])
        grade = categorize_grade(student_marks)
        return render_template("index.html",grade=grade, name=student_name, marks=student_marks)
    return render_template("index.html", grade=None)
if __name__ == "__main__":
    app.run(debug=True)