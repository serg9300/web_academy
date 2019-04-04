class New_stuff():
    add_teachers = 0
    add_students = 0
    def new (self, teachers, students):
        self.add_teachers = teachers
        self.add_students = students
class School_stuff():
    students = 500
    teachers = 20

    def add_stuff(self, newteachers, newstudents):
        self.teachers += newteachers
        self.students += newstudents

obj1 = New_stuff()
obj2 = School_stuff()

print(obj1.add_teachers, obj1.add_students)
print(obj2.teachers, obj2.students)

obj1.new(5,100)
obj2.add_stuff(obj1.add_teachers, obj1.add_students)

print(obj1.add_teachers, obj1.add_students)
print(obj2.teachers, obj2.students)

