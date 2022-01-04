class Student:
    _id = 0

    def __init__(self, name):
        self.id = Student._id + 1
        self.name = name
        Student._id += 1

    def get_name(self):
        return self.name

    def __str__(self):
        return f'Id: {self.id} and name {self.name}'


class Register:
    def register(self, obj):
        with open('students.txt', 'w') as file:
            file.write(str(obj))

    def get(self, id):
        with open('students.txt', 'r') as file:
            for line in file.readlines():
                if id in line:
                    return line


register = Register()
student = Student('Test')
register.register(student)
