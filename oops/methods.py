class Student:

  def __init__(self, age):
    self.__name = 'Student'
    self.age = age

  @classmethod
  def classM(student,self, age):
    return student(self.__name,age)

  @staticmethod
  def wtc():
    print("huuuu")

if __name__ == "__main__":

    s1=Student(20)
    s1.wtc()
    s1.classM("nooo",31)
    print(s1._Student__name, s1.age)
