from data_manager import load_courses, save_courses
from gpa_calculator import grade_to_gpa, calculate_weighted_gpa #精簡main版面

def print_menu():
    print("\n GPA 模擬器")
    print("1. 查看目前課程與 GPA")
    print("2. 新增一門課")
    print("3. 離開")


def main():
    courses = load_courses()  # 從檔案讀取課程資料

    while True:
        print_menu()
        choice = input("請選擇操作項目（輸入數字）：")

        if choice == "1":
            if not courses:
                print("目前尚未輸入任何課程。")
            else:
                print("\n目前課程：")
                total_credits = 0
                total_points = 0
                for course in courses:
                    name = course["name"] #轉換成json的格式來讀檔案
                    credit = course["credit"]
                    grade = course["grade"]
                    gpa_point = grade_to_gpa(grade)
                    print(f"{name}｜{credit} 學分｜等第：{grade}｜GPA：{gpa_point}")
                    total_credits += credit
                    total_points += credit * gpa_point

                overall_gpa = calculate_weighted_gpa(courses)
                print(f"\n 目前加權平均 GPA：{overall_gpa:.2f}")

        elif choice == "2":
            name = input("請輸入課程名稱：")
            credit = int(input("請輸入學分數："))
            grade = input("請輸入等第（例如 A、B+、C-）：").upper()
            courses.append({"name": name, "credit": credit, "grade": grade})
            save_courses(courses) # 將課程資料存到檔案中
            print("課程已新增！，可以輸入1來做確認")

        elif choice == "3":
            print("感謝使用 GPA 模擬器，再見！")
            break

        else:
            print("請輸入有效的選項（1~3）")


if __name__ == "__main__":
    main()
