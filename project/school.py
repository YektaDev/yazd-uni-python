"""
    File name: school.py
    Author: Ali Khaleqi Yekta - me@yekta.dev
    Date created: 2022-11-12
    Python Version: 3.11.0
"""

import getpass
import json
import os
import re
from datetime import datetime
from hashlib import sha256
from pathlib import Path
from random import shuffle

import matplotlib.pyplot as plt
from fpdf import FPDF

STUDENTS_FILE = 'student_accounts.json'
students = list()
active_student = None


class Color:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def clear():
    """
    Clears the console in a platform-specific manner.
    """
    print(Color.END)
    command = 'cls'  # cls is for Windows
    if os.name != 'nt':
        command = 'clear'  # if it isn't Windows it will use clear
    os.system(command)
    return 0


def pause():
    """
    Pauses the program until the user presses a key.
    """
    if os.name != 'nt':
        os.system("/bin/bash -c 'read -s -n 1 -p \"\"'")
    else:
        os.system('pause')


class Student:
    def __init__(self, name, lastname, national_code, student_code, school_name, address, password,
                 wrong_answer_questions, total_questions, score_date, marks):
        self.name = name
        self.lastname = lastname
        self.national_code = national_code
        self.student_code = student_code
        self.school_name = school_name
        self.address = address
        self.password = password
        self.wrong_answer_questions = wrong_answer_questions
        self.total_questions = total_questions
        self.score_date = score_date
        self.marks = marks

    def get_data(self):
        data = f'Name: {self.name} {self.lastname}\n'
        data += f'National Code: {self.national_code}\n'
        data += f'Student Code: {self.student_code}\n'
        data += f'School Name: {self.school_name}\n'
        data += f'Address: {self.address}\n'
        if len(self.marks) > 0:
            data += f'Total Wrong Answers: {self.wrong_answer_questions.__len__()}\n'
            data += f'Total Correct Answers: {self.total_questions - self.wrong_answer_questions.__len__()}\n'
            data += f'Total Questions: {self.total_questions}\n'
            data += f'Average Mark (out of 10): {sum(self.marks) / len(self.marks)}\n'
        else:
            data += '-' * 90
            data += '\nNo marks have been gained yet,\nso there is no data regarding the questions or marks.\n'
            data += '-' * 90
        return data


def read_students_from_file():
    """
    Reads the students from the file and returns a list of students.
    """
    try:
        with open(STUDENTS_FILE, 'r') as file:
            for json_dict in json.load(file):
                student = Student(json_dict['name'], json_dict['lastname'], json_dict['national_code'],
                                  json_dict['student_code'], json_dict['school_name'], json_dict['address'],
                                  json_dict['password'], json_dict['wrong_answer_questions'],
                                  json_dict['total_questions'], json_dict['score_date'], json_dict['marks'])
                students.append(student)
    except json.decoder.JSONDecodeError:
        print(f'{Color.RED}The file {STUDENTS_FILE} is corrupted!{Color.END}')
        exit(1)


def write_students_to_file():
    """
    Writes the students to the file.
    """
    with open(STUDENTS_FILE, 'w') as file:
        file.write(json.dumps(students, default=lambda o: o.__dict__, sort_keys=False, indent=2))


def input_menu(title, menu):
    """
    Prints a complete input menu with a title at the top. returns the input of the user.
    """
    long_line, double_line = '─' * (len(title) + 20), '══════════════════'
    rect, line = f'{Color.PINK}▪{Color.END}', f'{Color.RED}|{Color.END}'
    print(f'┌{long_line}┐')
    print(f'├──{line}──{line}─┤{rect}', Color.BOLD + Color.CYAN + title + Color.END, f'{rect}├─{line}──{line}──┤')
    print(f'├{long_line}┘')
    for key in menu.keys():
        print(f'│ {Color.RED}[{Color.END}{Color.YELLOW}{key}{Color.RED}]{Color.END}{Color.BOLD}{menu[key]}{Color.END}')
    return input(f'╞{double_line}╗\n╘{double_line}╝\n{rect} Enter a number: ')


def ask(question):
    """
    Asks a question and returns the answer.
    """
    return input(Color.END + Color.RED + '► ' + Color.END + Color.BOLD + question + ': ' + Color.END + Color.YELLOW)


def ask_new_pass(question):
    def is_strong(pw):
        one_letter_minimum = re.search('[a-zA-Z]', pw)
        one_num_minimum = re.search('[1-9]', pw)
        one_special_minimum = re.search('[^a-zA-Z0-9]', pw)
        return one_letter_minimum and one_num_minimum and one_special_minimum and len(pw) >= 8

    password = ''
    while not is_strong(password):
        if password != '':
            print(f'{Color.RED}The password is weak! Try a better one...{Color.END}')
        password = ask_pass(question)
    return password


def ask_pass(question):
    return getpass.getpass(Color.END + Color.RED + '► ' + Color.END + Color.BOLD + question + ': ' + Color.END)


def show_math_test_page(student):
    """
    The student enters a number and should then answer to some of its multiplication questions.
    """
    clear()
    print(f'─═─═─═─═─═─═─═─═─═─═─═ {Color.PINK}Math Test{Color.END} ═─═─═─═─═─═─═─═─═─═─═─')
    if student.wrong_answer_questions.__len__() == 0:
        print(f'{Color.GREEN}You have no wrong answers from before yet...{Color.END}')
    else:
        print('Before the test, take a look at your previous mistakes: ', student.wrong_answer_questions)

    number = int(ask('Enter a number'))
    print(f'{Color.CYAN}{Color.BOLD}Now answer the following questions:{Color.END}')

    wrong_i_list = list()
    i_list = [*range(1, 11)]
    shuffle(i_list)
    for i in i_list:
        answer = int(ask(f'{number} x {i}'))
        if answer != number * i:
            print(f'{Color.RED} [ X ] Not Right!{Color.END}')
            wrong_i_list.append(i)
        else:
            print(f'{Color.GREEN} [ ✓ ] Right!{Color.END}')
    print(f'{Color.CYAN}You have finished the test!{Color.END}')
    mark = 10 - len(wrong_i_list)
    print(f'Your mark is {Color.YELLOW}{mark}{Color.END}{Color.CYAN} out of 10!{Color.END}')
    for i in wrong_i_list:
        student.wrong_answer_questions.append(f'{number} x {i}')
    student.total_questions += 10
    student.score_date.append((mark, datetime.now().strftime('%Y-%m-%d')))
    student.marks.append(mark)
    write_students_to_file()
    pause()
    show_student_page(student)


def show_progress_chart_page(student):
    def show_chart(x, y):
        pos = [i for i in range(len(x))]
        plt.bar(pos, y, tick_label=x, width=0.5, color=['#2192FF', '#1D1CE5'])
        plt.xlabel('Date')
        plt.ylabel('Mark out of 10')
        plt.title('Marks Chart')
        plt.show()

    scores, dates = [], []
    for (score, date) in student.score_date:
        print(f'DATE: {date} - SCORE {score}')
        scores.append(score)
        dates.append(date)
    show_chart(dates, scores)
    show_student_page(student)


def show_report_card_page(student):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('arial', size=22, style='B')
    pdf.cell(200, 10, txt='Student Report Card', ln=1, align='C')
    pdf.set_font('arial', size=16, style='')
    ln = 1
    for line in student.get_data().split('\n'):
        ln += 1
        pdf.cell(200, 10, txt=line, ln=ln, align='L')
    filename = f'Report_{student.student_code}.pdf'
    pdf.output(filename)
    print(f'{Color.CYAN}The report card has been saved to {filename}{Color.END}')
    pause()
    show_student_page(student)


def show_student_page(student):
    while True:
        clear()
        choice = int(input_menu('Dashboard', {1: 'Math Test', 2: 'Progress Chart', 3: 'Report Card', 4: 'Logout'}))
        if choice == 1:
            show_math_test_page(student)
            return
        elif choice == 2:
            show_progress_chart_page(student)
            return
        elif choice == 3:
            show_report_card_page(student)
            return
        elif choice == 4:
            show_auth_page()
            return


def show_register_page():
    name = ask('Enter your name')
    lastname = ask('Enter your lastname')
    national_code = int(ask('Enter your national code'))
    student_code = int(national_code * 3 / 2)
    school_name = ask('Enter your school name')
    address = ask('Enter your address')
    password = sha256(ask_new_pass('Choose a password (it\'s hidden)').encode('utf-8')).hexdigest()
    student = Student(name, lastname, national_code, student_code, school_name, address, password, list(), 0, list(),
                      list())
    students.append(student)
    write_students_to_file()
    print(f'{Color.YELLOW}The registration is completed; {Color.PINK}Welcome!{Color.END}')
    print(f'Your student code is: {Color.UNDERLINE}{Color.BOLD}{Color.GREEN}{student_code}{Color.END}')
    print('Please remember it for future logins.')
    print(f'{Color.CYAN}Press any key to be redirected to the dashboard...{Color.END}')
    pause()
    show_student_page(student)


def show_login_page():
    student_code = int(ask('Enter your student code'))
    password = sha256(ask_pass('Enter your password (it\'s hidden)').encode('utf-8')).hexdigest()
    for student in students:
        if student.student_code == student_code and student.password == password:
            show_student_page(student)
            return
    print(f'{Color.RED}The student code or password is incorrect!{Color.END}')
    pause()
    show_auth_page()


def show_auth_page():
    while True:
        clear()
        choice = int(input_menu('School App', {1: 'Register', 2: 'Login', 3: 'Exit'}))
        if choice == 1:
            show_register_page()
            return
        elif choice == 2:
            show_login_page()
            return
        elif choice == 3:
            return


if __name__ == '__main__':
    if Path(STUDENTS_FILE).is_file():
        read_students_from_file()
    show_auth_page()
