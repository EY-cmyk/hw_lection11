class Person():
    def __init__(self, name, surname, age, form):
        self.name = name
        self.surname = surname
        self.age = age
        self.form = form

    def justlive(self):
        print(self.name + ' ' + 'просто существует')
    
    def haveproblems(self):
        print(self.name + ' ' +  self.surname.title() + ' ' + 'have some problems')

my_person = Person('Dima', 'Stetham', '22', '15-B')
my_person.justlive()
my_person.haveproblems()

class Student():
    def __init__(self, name, surname, age, form):
        self.name = name
        self.surname = surname
        self.age = age
        self.form = form

    def losebooks(self):
        print(self.name + ' ' + 'lose his books((')
    
    def sleeptoolong(self):
        print(self.name + ' ' + self.surname.title() + ' ' + 'prospal his lessons.')


my_student = Student('Igor', 'Malishev', '21', '3 course')
my_student.losebooks()
my_student.sleeptoolong()


class Teacher():
    def __init__(self, name, surname, age, salary, form, lesson):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
        self.form = form
        self.lesson = lesson

    def marktwo(self):
        print(self.name.title() + ' ' + 'поставила тебе 2 балла')
    
    def markeleven(self):
        print(self.name.title() + ' ' + 'поставила тебе 11 балов')
    
    def salarynima(self):
        print(self.name + ' ' + 'не получила' + ' ' + self.salary + ' ' + 'зарплаты(((')
    

my_teacher = Teacher('Tatiana', 'Mathematichka', '56', '13000', '10-A', 'Math')
my_teacher.marktwo()
my_teacher.markeleven()
my_teacher.salarynima()
