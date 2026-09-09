from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Student data
students = []
current_id = 1


# ---------------- HOME PAGE ----------------
@app.route('/')
def index():
    return render_template('index.html')


# ---------------- GET STUDENTS ----------------
@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)


# ---------------- ADD STUDENT ----------------
@app.route('/api/students', methods=['POST'])
def add_student():
    global current_id

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Student data is required"
        }), 400

    student = {
        "id": current_id,
        "name": data.get("name"),
        "email": data.get("email"),
        "phone": data.get("phone"),
        "course": data.get("course"),
        "department": data.get("department"),
        "year": data.get("year")
    }

    students.append(student)
    current_id += 1

    return jsonify(student), 201


# ---------------- UPDATE STUDENT ----------------
@app.route('/api/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):

    data = request.get_json()

    for student in students:

        if student["id"] == student_id:

            student["name"] = data.get("name", student["name"])
            student["email"] = data.get("email", student["email"])
            student["phone"] = data.get("phone", student["phone"])
            student["course"] = data.get("course", student["course"])
            student["department"] = data.get(
                "department",
                student["department"]
            )
            student["year"] = data.get(
                "year",
                student["year"]
            )

            return jsonify(student)

    return jsonify({
        "error": "Student not found"
    }), 404


# ---------------- DELETE STUDENT ----------------
@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):

    global students

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return jsonify({
                "message": "Student deleted successfully"
            })

    return jsonify({
        "error": "Student not found"
    }), 404


# ---------------- RUN SERVER ----------------
if __name__ == '__main__':
    app.run(port=5001, debug=True)