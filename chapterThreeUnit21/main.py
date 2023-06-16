class Student:
    scores = []

    def __init__(self, name, student_id, eng_quiz, math_quiz, science_quiz):
        self.__name = name
        self.__student_id = student_id
        # self.__eng_quiz = eng_quiz
        # self.__math_quiz = math_quiz
        # self.__science_quiz = science_quiz

    def __str__(self):
        return 'Name : {0}, ID : {1}'.format(self.__name, self.__student_id)

    def set_eng_quiz(self, eng_quiz):
        self.__eng_quiz = eng_quiz

    def set_math_quiz(self, math_quiz):
        self.__math_quiz = math_quiz

    def set_science_quiz(self, science_quiz):
        self.__science_quiz = science_quiz

    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def get_eng_quiz(self):
        return self.__eng_quiz

    def get_math_quiz(self):
        return self.__math_quiz

    def get_science_quiz(self):
        return self.__science_quiz

    def get_total_score(self):
        return self.__eng_quiz + self.__math_quiz + self.__science_quiz

    def get_avg_score(self):
        return (self.__eng_quiz + self.__math_quiz + self.__science_quiz) / 3


def main():
    stud_name = input('Enter the student\'s name : ')
    stud_id = input('Enter the student\'s ID : ')

    student1 = Student(stud_name, stud_id, 0, 0, 0)

    stud1_eng_quiz = int(input('Enter the student\'s English quiz score : '))
    student1.set_eng_quiz(stud1_eng_quiz)

    stud1_math_quiz = int(input('Enter the student\'s mathematics quiz score : '))
    student1.set_math_quiz(stud1_math_quiz)

    stud1_science_quiz = int(input('Enter the student\'s science quiz score : '))
    student1.set_science_quiz(stud1_science_quiz)

    print(student1)
    print('English quiz score : {0}, Mathematics quiz score : {1}\nScience quiz score : {2},'
          .format(student1.get_eng_quiz(), student1.get_math_quiz(), student1.get_science_quiz()))
    print('Total : {0}, Average : {1}'.format(student1.get_total_score(), student1.get_avg_score()))


main()
