students = [
  {'username':'joycedev','name': 'joyce', 'course': 'python', 'age': 18},
  {'id': 2, 'username': 'fatma15', 'name': 'fatma', 'course': 'java', 'age': 20}
]

class Student(model):
  username = charfield(max_length=255)
  name = charfield(max_length=1000)
  course = Texttfield(default="python")
  age = Integerfield(default=18)

  class Meta:
    database = database

    ;

    def initialize():
      try:
        Student.create_table()
        except operationalError:
          pass
          for student in students:
            try
            student.create(
              username= student.get('username'),
            )


