from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage
students = []
current_id = 1


# ============================================================
# HOME PAGE
# ============================================================

@app.route('/')
def home():
    return render_template('index.html')


# ============================================================
# GET ALL STUDENTS
# ============================================================

@app.route('/api/students', methods=['GET'])
def get_students():

    return jsonify(students)


# ============================================================
# ADD STUDENT
# ============================================================

@app.route('/api/students', methods=['POST'])
def add_student():

    global current_id

    data = request.get_json()

    if not data:
        return jsonify({
            'error': 'Student data is required'
        }), 400

    if not data.get('name'):
        return jsonify({
            'error': 'Student name is required'
        }), 400

    student = {
        'id': current_id,
        'name': data.get('name'),
        'email': data.get('email'),
        'phone': data.get('phone'),
        'course': data.get('course'),
        'department': data.get('department'),
        'year': data.get('year')
    }

    students.append(student)

    current_id += 1

    return jsonify(student), 201


# ============================================================
# UPDATE STUDENT
# ============================================================

@app.route('/api/students/<int:student_id>', methods=['PUT', 'PATCH'])
def update_student(student_id):

    data = request.get_json()

    if not data:
        return jsonify({
            'error': 'Student data is required'
        }), 400

    for student in students:

        if student['id'] == student_id:

            if 'name' in data:
                student['name'] = data['name']

            if 'email' in data:
                student['email'] = data['email']

            if 'phone' in data:
                student['phone'] = data['phone']

            if 'course' in data:
                student['course'] = data['course']

            if 'department' in data:
                student['department'] = data['department']

            if 'year' in data:
                student['year'] = data['year']

            return jsonify(student)

    return jsonify({
        'error': 'Student not found'
    }), 404


# ============================================================
# DELETE STUDENT
# ============================================================

@app.route('/api/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):

    global students

    for student in students:

        if student['id'] == student_id:

            students.remove(student)

            return '', 204

    return jsonify({
        'error': 'Student not found'
    }), 404


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == '__main__':

    app.run(
        host='127.0.0.1',
        port=5000,
        debug=True
    )