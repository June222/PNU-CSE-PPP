import input_data_series as ids
from compile_module import *
from set_module import *
from get_module import *

# ------------조작할 부분--------------#
# 채점할 LAB 번호(폴더의 이름의 마지막 부분)
current_lab_number = "07"
# 추가로 컴파일 할 파일 목록
additional_list_to_compile = ["Rectangle", "InvalidRectangleException"] # Compile 순서대로
# main class 파일 이름
main_class_name = "RectangleManager" # .java 빼고
# Scanner로 입력 받을 String
input_string = ids.data_07
# ------------조작할 부분--------------#



# ----------건드리지 마시오-------------#
# 채점할 LAB 폴더 위치
current_lab_folder_path = f'./Lab{current_lab_number}'
# main class를 포함한 컴파일할 파일들
ordered_list_to_compile = []
# 학생의 점수 저장
scores={}
# 학생의 출력문 저장
answers={}
# 학생의 main 코드 저장
codes={}
# ----------건드리지 마시오-------------#


def main():
    print()
    # 점수 확인만 하고 싶다면 아래 함수만 주석 처리 하면됨.
    compile_all_java_files()
    # 학생들의 정보 저장
    grade_students()
    # 학생들의 정보 확인
    get_students_detail()

# 학생들의 정보 확인
def get_students_detail():
    student_name = input("Enter Student Name or 'quit': ")
    while(student_name.lower() != 'quit'):
        print('////////////////////////////////////////////////')
        print('////////////////////////////////////////////////')
        get_student_code(student_name)
        get_student_answer(student_name)
        get_student_grade(student_name)
        student_name = input("Enter Student Name or 'quit': ")

if __name__ == "__main__":
    main()