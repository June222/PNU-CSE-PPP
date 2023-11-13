import subprocess
import os

# 현재 채점할 LAB 번호
current_lab_number = "04"
# .java가 붙은 main 함수가 있는 파일 이름
my_file_name = "StringSetManager.java"
# .java를 지운 main 함수가 있는 파일 이름
class_name = "StringSetManager"

# 학생들의 파일이(java) 저장된 폴더 위치
students_folder_path = f'./Lab{current_lab_number}'
# 정답 파일이(java) 저장된 위치
answer_file_path = f"./Lab{current_lab_number}/{my_file_name}"

# 점수 저장
scores={}
# 정답(출력문) 저장
answers={}
# main class 코드 저장
codes={}

# 각 LAB 번호에 맞는 input data
input_data_4 = """add Hello
Add Java
add hello
aDD Java
remove Hello
remove java
add Good
remove Java
clean
add PNU
add is
add Wonderful
quit
"""

input_data_3 = """ADD 10
add 20
LIST
Sum
Add 30
suM
Sum
Summ
list
Quit
"""

input_data_5 = """add
James 1
list
add
Brown 2
list
find
Brown 2
find
Brown 1
add
Kim 4
list
clear
list
find
Brown 2
add
Brown 2
find
Brown 2
list
find
brown 2
quit
"""


input_data = input_data_4




def main():
    
    run_with_input()

    get_students_detail()

    print("수고했어요!")

# 초기 LAB에는 input data가 필요하지 않아 이 코드만 남음
# input data(Scanner)가 필요한 코드 실행 시
def run_with_input():
    # 정답 출력문 return
    correct_answer = run_java_program_input(answer_file_path, students_folder_path, input_data)
    # log 남김
    print("정답:\n" + correct_answer)

    # 각 학생의 폴더 찾기
    for student_folder in os.listdir(students_folder_path):
        student_folder_path = os.path.join(students_folder_path, student_folder)

        # 폴더일 경우에만(정답 java 파일은 무시)
        if not os.path.isdir(student_folder_path):
            continue
        
        # parsing
        student_name = student_folder.split('-')[0]

        # 학생의 java 파일을 찾기
        for student_java_file in os.listdir(student_folder_path):
            if student_java_file.endswith(".java"):
                # 학생의 java 파일 위치
                student_java_file_path = os.path.join(student_folder_path, student_java_file)
                # 학생의 정보 저장
                set_student_details(student_name, student_java_file_path, student_folder_path, correct_answer, with_input = True)
                

# 학생의 정보 저장
def set_student_details(student_name, student_java_file_path, student_folder_path, correct_answer, with_input: bool):
    # input data가 필요한 경우
    if with_input :
        student_answer = run_java_program_input(student_java_file_path, student_folder_path, input_data)
    # 필요하지 않은 경우
    else :
        student_answer = run_java_program(student_java_file_path)
    
    student_answer = str(student_answer)
    # 동명이인 청리
    if student_name in scores.keys():
        student_name = student_name + "2"

    set_student_grade(student_name, student_answer, correct_answer)
    set_student_code(student_name, student_java_file_path)
    set_student_answer(student_name, student_answer)

    print(student_name +  ": done")

# 학생의 출력문 저장
def set_student_answer(student_name, student_answer):
    answers[student_name] = student_answer

# 학생의 성적 저장
def set_student_grade(student_name,student_answer, correct_answer):
    score = compare_outputs(student_answer, correct_answer)
    scores[student_name] = score

# 학생의 main Code 저장
def set_student_code(student_name, student_java_file_path):
    # main code 읽기
    try:
        with open(student_java_file_path, "r") as file:
            student_java_code = file.read()
            codes[student_name] = student_java_code
    except:
            codes[student_name] = "Cannot Read File."

# java 파일 컴파일
def run_java_program(java_file):
    try:
        result = subprocess.run(["java", java_file],capture_output=True, text=True, timeout=5.0)
        return result.stdout
    except subprocess.TimeoutExpired:
        return "Execution timed out."
    
# java 파일 컴파일 및 실행
def run_java_program_input(java_file, student_folder_path, input_str):
    try:
        # java 파일 컴파일
        # 1. 주석에 한글을 넣는 학생들이 있어 UTF-8 로 Encoding
        # 2. 컴파일할 파일을 [] 안에 입력
        compile_result = subprocess.run(["javac", "-encoding", "UTF-8",  java_file], capture_output=True, text=True, timeout=5.0)

        # compile이 잘 된 경우
        if compile_result.returncode == 0:
            # 1. python 파일의 위치와 java 파일의 위치가 다르므로 실행 시 문제가 생김
            # 이는 -classpath로 해결
            # 2. Scanner로 input data 입력시 input Argument 사용
            result = subprocess.run(["java","-classpath", student_folder_path, class_name], input = input_str, capture_output=True, text=True, timeout=5.0)
            # 실행이 잘 될 경우
            if result.returncode == 0 :
                return result.stdout
            # 실행이 잘 되지 않은 경우
            else :
                return result.stderr
        
        # compile이 잘 되지 않은 경우
        return compile_result.stderr
    except subprocess.TimeoutExpired:
        return "Execution timed out."


# 출력문에서 " ", "\t", "\n", 제거 
def compare_outputs(student_output, correct_output):
    if str(student_output).strip().replace(" ","").replace('\n',"").replace('\t',"") == str(correct_output).strip().replace(" ","").replace('\n',"").replace('\t',""):
        return 100
    else :
        return 0

# 학생 정보 확인
def get_students_detail():
    student_name = input("Enter Student Name or 'quit': ")
    while(student_name.lower() != 'quit'):
        print('////////////////////////////////////////////////')
        print('////////////////////////////////////////////////')
        get_student_code(student_name)
        get_student_answer(student_name)
        get_student_grade(student_name)
        student_name = input("Enter Student Name or 'quit': ")


def get_student_grade(student_name):
    print(f"{student_name}: {scores.get(student_name)}")

def get_student_code(student_name):
    print(f"코드:\n{codes.get(student_name)}")

def get_student_answer(student_name):
    print(f"출력문:\n {answers.get(student_name)}")



main()