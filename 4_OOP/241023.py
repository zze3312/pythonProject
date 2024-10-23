# 클래스(Class)와 객체(Object)
#  - 객체지향 프로그래밍 언어 : 데이터(객체)를 기반으로 프로그램을 만드는 프로그래밍 언어
#  - 객체 : 여러가지 속성을 가질 수 있는 대상
#   ※ 추상화 : 복잡한 자료, 모듈, 시스템 등으로부터 핵심적인 개념 또는 기능을 간추려 내는것

def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_avg(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return f"{student["name"]}\t{student_get_sum(student)}\t{student_get_avg(student)}"

students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92)
]

print("이름\t\t총점\t평균")
for student in students:
    print(student_to_string(student))

#  - 위 소스에서 학생이 객체는 학생
#  - 클래스(class) : 객체를 쉽고 편리하게 생성하기 위해 만들어진 구문
#  - class 클래스명:
#        클래스 내용
#  - 인스턴스(instance) : 클래스를 기반으로 만들어진 객체
#  - 생성자(constructor) : 클래스 이름과 같은 인스턴스를 생성할 때 쓰는 함수
#    > class 클래스명:
#        def __init__(self, 추가 매개변수):
#            pass
#    > 클래스 내부의 함수(메서드)의 첫번째 매개변수로는 반드시 self를 입력해야 함
#    > self는 자기자신을 나타내는 딕셔너리.
#    > self가 가지고 있는 속성과 기능에 접근할 때는 self.<식별자> 형태로 접근
#      예제)
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print(students[0].name)
print(students[0].korean)
print(students[0].math)
print(students[0].english)
print(students[0].science)

#  - 소멸자(destructor) : 인스턴스가 소멸될 때 호출되는 함수
#    > __del__(self) 형태로 함수를 선언
#     예제)
class Test:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} - 생성되었습니다")
    def __del__(self):
        print(f"{self.name} - 파괴되었습니다")

test = Test("A")

#  - 메소드(method) : 클래스가 가지고 있는 함수
#    > class 클래스명:
#          def 메소드 이름(self, 추가 매개변수):
#              pass
#      예제)
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average()}"

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print("이름\t\t총점\t평균")
for student in students:
    print(student.to_string())

#  - 상속 : 어떤 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스를 만드는 방법
#  - isinstance() : 어떤 클래스를 기반으로 만들었는지 확인하게 해주는 함수 - 결과 : T/F
#    > isinstance(인스턴스, 클래스)

class Student:
    def __init__(self):
        pass

student = Student()
print("isinstance(student, Student):", isinstance(student, Student))
print("type(student):", type(student))

# 예제
class Student:
    def study(self):
        print("공부를 합니다")

class Teacher:
    def teach(self):
        print("학생을 가르칩니다")

classroom = [Student(), Student(), Teacher(), Student(), Student()]

for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()

#  - 클래스 변수 : class구문 바로 아래의 단계에서 변수를 선언
class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print(f"{Student.count}번째 학생이 생성되었습니다")

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print()
print(f"현재 생성된 총 학생 수는 {Student.count}명 입니다.")

#  - 클래스 함수 : 클래스가 가진 함수
#  - 함수에 데코레이터(decorator) @classmethod 를 붙여주면됨
#  - class 클래스명:
#        @classmethod
#        def 클래스명(cls, 매개변수):
#            pass
#    > 클래스함수의 첫 매개변수는 클래스 자체가 들어옴(cls)

class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("------학생 목록------")
        print("이름\t\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("--------------------")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def __str__(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average()}"


Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린", 95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)

Student.print()

# 상속 : 다른 기본형태의 클래스를 가져와 교체하여 사용하는 방법
# 다중상속 : 상속되어있는것을 가져와 교체하여 사용하는 방법
# 부모(parent) 클래스 : 상속 당하는 클래스
# 자식(child) 클래스 : 상속 하는 클래스

class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다")

    def test(self):
        print("Parent 클래스의 test() 메소드 입니다.")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의 __init()__ 메소드가 호출되었습니다")

    # 오버라이딩 - 없으면 부모의 test()실행됨
    def test(self):
        print("Child 클래스의 test() 메소드 입니다.")

child = Child()
child.test()
print(child.value)

# 예외처리
#  - try-except 문 : 오류 발생 시 except 부분 실행
#  - try:
#        ...
#    except [발생오류 [as 오류변수]]:
#        ...

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)

#  - try-finally 문 : 오류 발생 후에도 실행시키는 부분
#  - 여러 개의 오류 처리 : except 를 추가 or 괄호로 묶어서 처리
try:
    a = [1, 2]
    print(a[3])
    4 / 0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")
except IndexError:
    print("인덱싱 할 수 없습니다")

#
