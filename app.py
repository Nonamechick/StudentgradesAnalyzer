from flask import Flask, render_template, request

app = Flask(__name__)

def categorize_grade(marks):
    """
    Categorize student grades as Pass or Fail based on a passing criterion (e.g, passing grade 50).
    """
    if marks >= 50:
        return "Pass"
    elif marks < 0:
        return "Impossible"
    else:
        return "Fail"

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores  # Dictionary of subjects and scores
        self.grades = {}      # Dictionary to store grades
        self.gpa = 0.0        # GPA of the student
    
    def calculate_grades(self):
        grade_scale = {
            (90, 100): 'A',
            (80, 89): 'B',
            (70, 79): 'C',
            (60, 69): 'D',
            (0, 59): 'F'
        }
        
        for subject, score in self.scores.items():
            for (low, high), grade in grade_scale.items():
                if low <= score <= high:
                    self.grades[subject] = grade
                    break
    
    def calculate_gpa(self):
        grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
        total_points = sum(grade_points[self.grades[subject]] for subject in self.grades)
        self.gpa = round(total_points / len(self.grades), 2)
    
    def generate_feedback(self):
        if self.gpa >= 3.5:
            return "Excellent performance! Keep up the great work!"
        elif self.gpa >= 3.0:
            return "Good job! Aim for even higher achievements."
        elif self.gpa >= 2.0:
            return "Satisfactory performance, but there's room for improvement."
        else:
            return "Needs improvement. Focus more on studies."

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        student_name = request.form["name"]
        subjects = int(request.form["subjects"])
        scores = {}
        
        for i in range(subjects):
            subject = request.form[f"subject_{i+1}"]
            score = float(request.form[f"score_{i+1}"])
            scores[subject] = score
        
        student = Student(student_name, scores)
        student.calculate_grades()
        student.calculate_gpa()
        feedback = student.generate_feedback()
        
        return render_template("index.html", student=student, feedback=feedback)
    
    return render_template("index.html", student=None)

if __name__ == "__main__":
    app.run(debug=True)
