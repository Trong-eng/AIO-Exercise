from abc import ABC, abstractmethod
class Person(ABC):
  def __init__(self,name,yob):
    self.name = name
    self.yob = yob
  def describe(self):
    pass
  def get_yob(self):
    return self.yob
class Student(Person):
  def __init__(self,name,yob,grade) :
    super().__init__(name=name,yob=yob)
    self.grade = grade
  def describe(self):
    print(f"name: {self.name}, yob: {self.yob}, grade: {self.grade}")
class Teacher(Person):
  def __init__(self,name,yob,subject) :
    super().__init__(name=name,yob=yob)
    self.subject = subject
  def describe(self):
    print(f"name: {self.name}, yob: {self.yob}, subject: {self.subject}")
class Doctor(Person):
  def __init__(self,name,yob,speciality) :
    super().__init__(name=name,yob=yob)
    self.speciality = speciality
  def describe(self):
    print(f"name: {self.name}, yob: {self.yob}, speciality: {self.speciality}")
teacher1=Teacher('Trọng','2005','Toán')
student1 = Student('Trang','2008','7')
doctor1 = Doctor('Nam','1999','tim mach')
class Ward:
  def __init__(self,name):
    self.name = name
    self.list_people = list()
  def add_people(self, person : Person):
    self.list_people.append(person)
  def describe(self):
    for people in self.list_people:
      people.describe()
  def count_doctor(self):
    count = 0
    for people in self.list_people:
      if isinstance(people,Doctor):
        count += 1
    return count
  def sort_yob(self):
    self.list_people.sort(key = lambda x: x.get_yob(),reverse = True)
  def compute_average_yob(self):
    sum = 0
    for people in self.list_people:
      sum += int(people.get_yob())
    return sum/len(self.list_people)
ward1 = Ward('Ward1')
ward1.add_people(teacher1)
ward1.add_people(student1)
ward1.add_people(doctor1)
print(ward1.count_doctor())
ward1.sort_yob()
ward1.describe()
ward1.compute_average_yob()