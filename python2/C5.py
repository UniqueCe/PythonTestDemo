from C6 import Human

class Student(Human):

    def __init__(self, school, name, age):
        self.school = school
        # Human.__init__(self, name, age)
        super(Student, self).__init__(name, age)

    def do_homework(self):
        print("做作业")


# stu1 = Student("阿斯达", 98)
# print(stu1.name)

stu2 = Student("学校", "历史", 43)
stu2.do_homework()
stu2.get_name()

print(stu2.name, stu2.school, stu2.age)


 


