from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mongoengine import Document, StringField, IntField, connect
from bson import ObjectId
import certifi
 
# -----------------------------
# FastAPI App
# -----------------------------
 
app = FastAPI(
    title="Student Management API",
    description="FastAPI CRUD with MongoDB",
    version="1.0"
)
 
 
# -----------------------------
# MongoDB Connection
# -----------------------------
 
MONGO_URL = (
    "mongodb+srv://farooqy6696_db_user:"
    "Farooqkhan2718"
    "@cluster0.n48yboy.mongodb.net/"
    "student_db?retryWrites=true&w=majority"
)

connect(
    host=MONGO_URL,
    tls=True,
    tlsCAFile=certifi.where()
)
 
 
# -----------------------------
# Pydantic Model
# -----------------------------
 
class StudentCreate(BaseModel):
    name: str
    age: int
    course: str
 
 
class StudentUpdate(BaseModel):
    name: str
    age: int
    course: str
 
 
# -----------------------------
# MongoDB Model
# -----------------------------
 
class Student(Document):
    name = StringField(required=True)
    age = IntField(required=True)
    course = StringField(required=True)
 
    meta = {
        "collection": "students"
    }
 
 
# -----------------------------
# Home API
# -----------------------------
 
@app.get("/")
def home():
    return {
        "message": "Student Management API is working"
    }
 
 
# -----------------------------
# CREATE Student
# -----------------------------
 
@app.post("/students")
def create_student(student: StudentCreate):
 
    new_student = Student(
        name=student.name,
        age=student.age,
        course=student.course
    )
 
    new_student.save()
 
    return {
        "message": "Student created successfully",
        "student": {
            "id": str(new_student.id),
            "name": new_student.name,
            "age": new_student.age,
            "course": new_student.course
        }
    }
 
 
# -----------------------------
# GET All Students
# -----------------------------
 
@app.get("/students")
def get_students():
 
    students = Student.objects()
 
    return [
        {
            "id": str(student.id),
            "name": student.name,
            "age": student.age,
            "course": student.course
        }
        for student in students
    ]
 
 
# -----------------------------
# GET Student By ID
# -----------------------------
 
@app.get("/students/{student_id}")
def get_student(student_id: str):
 
    if not ObjectId.is_valid(student_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )
 
    student = Student.objects(id=student_id).first()
 
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
 
    return {
        "id": str(student.id),
        "name": student.name,
        "age": student.age,
        "course": student.course
    }
 
 
# -----------------------------
# UPDATE Student
# -----------------------------
 
@app.put("/students/{student_id}")
def update_student(
    student_id: str,
    student_data: StudentUpdate
):
 
    if not ObjectId.is_valid(student_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )
 
    student = Student.objects(id=student_id).first()
 
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
 
    student.name = student_data.name
    student.age = student_data.age
    student.course = student_data.course
 
    student.save()
 
    return {
        "message": "Student updated successfully",
        "student": {
            "id": str(student.id),
            "name": student.name,
            "age": student.age,
            "course": student.course
        }
    }
 
 
# -----------------------------
# DELETE Student
# -----------------------------
 
@app.delete("/students/{student_id}")
def delete_student(student_id: str):
 
    if not ObjectId.is_valid(student_id):
        raise HTTPException(
            status_code=400,
            detail="Invalid student ID"
        )
 
    student = Student.objects(id=student_id).first()
 
    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )
 
    student.delete()
 
    return {
        "message": "Student deleted successfully"
    }
 