def print_menu():
    print("\n GPA 模擬器")
    print("1. 查看目前課程與 GPA")
    print("2. 新增一門課")
    print("3. 離開")


def main():
    courses = []

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
                    name, credit, grade = course
                    gpa_point = grade_to_gpa(grade)
                    print(f"{name}｜{credit} 學分｜等第：{grade}｜GPA：{gpa_point}")
                    total_credits += credit
                    total_points += credit * gpa_point

                overall_gpa = total_points / total_credits if total_credits > 0 else 0
                print(f"\n 目前加權平均 GPA：{overall_gpa:.2f}")

        elif choice == "2":
            name = input("請輸入課程名稱：")
            credit = int(input("請輸入學分數："))
            grade = input("請輸入等第（例如 A、B+、C-）：").upper()
            courses.append((name, credit, grade))
            print("課程已新增！，可以輸入1來做確認")

        elif choice == "3":
            print("感謝使用 GPA 模擬器，再見！")
            break

        else:
            print("請輸入有效的選項（1~3）")


# 將GPA轉換為分數
def grade_to_gpa(grade):
    gpa_scale = {
        "A+": 4.3,
        "A": 4.0,
        "A-": 3.7,
        "B+": 3.3,
        "B": 3.0,
        "B-": 2.7,
        "C+": 2.3,
        "C": 2.0,
        "C-": 1.7,
        "F": 0.0
    }
    return gpa_scale.get(grade, 0.0)  # 若今天輸入奇怪的東西會被算做0


if __name__ == "__main__":
    main()
