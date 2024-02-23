from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
#to allow access in my front end
from flask_cors import CORS,cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'application/json'
#To prevent sorting when jsonifying
app.json.sort_keys = False
engine = create_engine("postgresql://lalva224:1234@localhost/school_flask")

#avoid manual class definitions!!!

#prepare db tables. Engine is where the uri is stored. reflect is telling it to reflect class definitons.
Base = automap_base()
Base.prepare(autoload_with = engine)

#find and store the tables
Students = Base.classes.students
Subjects = Base.classes.subjects
Teachers = Base.classes.teachers

#app.config did this for us but now we need to do it explicitly. This is permission to edit the dataabse it contains all the add, edit , delete methods.
session = Session(engine)

@app.route('/students/',methods=['GET'])
def get_student_data():
    #cant query directly though class table, need to do it through session
    student_data = session.query(Students).all()
    student_list = [
            {
                'ID' : student.id,
                'First Name': student.first_name,
                'Last Name': student.last_name,
                'Age' : student.age,
                'Class':{
                    'Subject' : find_subject_name_by_id(student.subject_id),
                    'Teacher': find_teacher_name_by_subject_id(student.subject_id)
                }
            }
            for student in student_data
    ]
    return jsonify(student_list)

@app.route('/teachers/',methods = ['GET'])
def get_teacher_data():
    teacher_objects= session.query(Teachers).all()
    teacher_list = [
        {
            'Teacher First Name': teacher.first_name,
            'Teacher Last Name' : teacher.last_name,
            'Age': teacher.age,
            'Subject':{
                'Subject Name:' : find_subject_name_by_id(teacher.subject_id),
                'Students': get_students_by_subject_id(teacher.subject_id)
            }
        }
        for teacher in teacher_objects
    ]
    return jsonify(teacher_list)

@app.route('/subjects/',methods=['GET'])
def get_subject_data():
    subject_objects = session.query(Subjects).all()
    subject_list = [
        {
            'Subject Id' : subject.id,
            'Subject Name' : subject.subject_name,
            'Students': get_students_by_subject_id(subject.id),
            'Teachers' : get_teachers_by_subject_id(subject.id)
        }
        for subject in subject_objects
    ]
    return jsonify(subject_list)
#
def get_teachers_by_subject_id(subject_id_):
    teacher_objects = session.query(Teachers).filter(Teachers.subject_id==subject_id_).all()
    teacher_list = [
        {
            'First Name': teacher.first_name,
            'Last Name': teacher.last_name
        }
        for teacher in teacher_objects
    ]
    return teacher_list

def get_students_by_subject_id(subject_id_):
    student_data = session.query(Students).filter(Students.subject_id ==subject_id_).all()
    student_list = [
        {
            'Student First Name': student.first_name,
            'Student Last Name' : student.last_name
        }
        for student in student_data
    ]
    return student_list


def find_subject_name_by_id(subject_id):
    subject_data = session.query(Subjects).filter(Subjects.id ==subject_id).all()
    return subject_data[0].subject_name

def find_teacher_name_by_subject_id(subject_id_):
    teacher_data = session.query(Teachers).filter(Teachers.subject_id ==subject_id_).all()
    return f"{teacher_data[0].first_name } {teacher_data[0].last_name}"


if __name__ == '__main__':
    app.run(debug = True)