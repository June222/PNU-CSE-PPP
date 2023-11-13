# 폴더에 접근하기 위한 import
import os
# java 파일의 컴파일 및 실행을 위한 import
import subprocess

# global 변수 import
import platform_programming_grading_program as gp

# compile 진행 
def compile_all_java_files():
    # 1. 컴파일 할 파일 목록을 만듬
    set_list_to_compile()
    # 2. 정답 파일을 먼저 컴파일 함
    compile_my_file()
    # 3. 학생들의 코드에서 compile 및 import를 삭제함
    delete_students_code_line_with_package()
    # 4. 학생들의 파일을 컴파일 함
    compile_students_file()

# 컴파일 할 파일 목록 만들기
def set_list_to_compile():
    global ordered_list_to_compile

    print("List 만들기 실행")
    # 1. 추가적으로 컴파일 할 목록에
    ordered_list_to_compile = gp.additional_list_to_compile.copy()
    # 2. main class를 추가함
    ordered_list_to_compile.append(gp.main_class_name)
    print("Compile List: " + ", ".join(ordered_list_to_compile))
    print()

# 정답 파일들을 컴파일
def compile_my_file():
   
    print("initiating compile_my_file()")
    # list의 모든 java 파일을 컴파일
    for java_file_name in ordered_list_to_compile:
        java_file_name = java_file_name + ".java"
        # java 파일의 위치
        my_java_file_path = os.path.join(gp.current_lab_folder_path, java_file_name)
        # 위치와 폴더 위치를 같이 전달
        compile_java_file(my_java_file_path, gp.current_lab_folder_path)

    print("compile_my_file() done.")
    print()

# 학생들의 파일들을 컴파일
def compile_students_file():
    print("initiating compile_students_file()")
    # 현재 LAB에서 모든 학생들의 폴더에 대해
    for student_folder in os.listdir(gp.current_lab_folder_path):
        # 폴더 위치 확인
        student_folder_path = os.path.join(gp.current_lab_folder_path, student_folder)

        if not os.path.isdir(student_folder_path) :
            continue
        
        # list의 모든 java 파일을 컴파일
        for java_file_name in ordered_list_to_compile:
            java_file_name = java_file_name + ".java"
            # 학생의 java 파일 위치 확인
            student_java_file_path = os.path.join(student_folder_path, java_file_name)
            # 컴파일
            compile_java_file(student_java_file_path, student_folder_path)
        print()
    
    print("compile_students_file() done.")
    print()

# package 및 불필요한 import 삭제
def delete_students_code_line_with_package():
    print("init delete_students_code_line_with_package")
    
    for student_folder in os.listdir(gp.current_lab_folder_path):
        student_folder_path = os.path.join(gp.current_lab_folder_path, student_folder)

        if not os.path.isdir(student_folder_path):
            continue
        
        for student_java_file in os.listdir(student_folder_path):
            if student_java_file.endswith(".java"):
                student_java_file_path = os.path.join(student_folder_path, student_java_file)
            
                
                try:
                    # 파일의 코드를 읽어
                    with open(student_java_file_path, 'r', encoding = "UTF-8") as file:
                        content = file.read()
                    # 지워야할 line을 저장할 list
                    future_delete_list = []

                    # '\n'으로 코드를 분리
                    content_list_split_by_enter = content.split("\n")
                    # 매 line에서
                    for line in content_list_split_by_enter:
                        # import 및 package로 시작할 경우
                        if line.strip().startswith("import") or line.strip().startswith("package"):
                            # 두 띄어쓰기 다음 코드를 확인하여
                            secondWord = line.split(" ")[1][:-1]
                            # 지정된 조건이면 삭제할 list에 추가
                            if secondWord.startswith("kr") or secondWord.endswith("kr") or secondWord.startswith("Lab") or secondWord.startswith("lab") :
                                future_delete_list.append(line)
                    # 지울 line에 대하여
                    for line in future_delete_list:
                        # 코드에서 삭제
                        content_list_split_by_enter.remove(line)
                    # 없앴던 개행 문자를 추가하여 코드 복구
                    content = "\n".join(content_list_split_by_enter)
                    
                except:
                    print(student_java_file_path + " 읽기 불가능 합니다.") 

                try:
                    # package 및 import를 삭제한 코드를 덮어쓰기
                    with open(student_java_file_path, 'w', encoding="UTF-8") as file:
                        file.write(content)
                        print(student_java_file_path +" package를 지웠습니다.")
                except:
                    print(student_java_file_path + " 쓰기가 불가능 합니다.")
        print()
    print("delete_students_package_code() done.")
    print()

# java 파일을 컴파일
def compile_java_file(java_file_path: str, current_folder_path: str):
    try:
        # 1. 주석에 한글을 쓰는 학생들이 있어 UTF-8로 Encoding
        # 2. root folder와 학생들의 java 파일의 위치가 달라 이를 넣어줌
        # 3. Timeout은 5초로 설정
        compile_result = subprocess.run(["javac", "-encoding", "UTF-8", "-cp", current_folder_path , java_file_path], capture_output=True, text=True, timeout=5.0)

        # 컴파일이 완료된 경우
        if compile_result.returncode == 0:
            print(f"{java_file_path}의 컴파일이 완료되었습니다.")
        # 컴파일이 완료되지 못한 경우
        else:
            print(f"{java_file_path}의 컴파일이 아래의 이유로 성공하지 못했습니다.")
            print(compile_result.stderr);
    # 시간 초과가 된 경우
    except subprocess.TimeoutExpired:
        print("Execution timed out.")
