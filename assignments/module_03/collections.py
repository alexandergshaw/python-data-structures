students = [
    {"name": "Alice", "grade": 91, "major": "CS"},
    {"name": "Bob", "grade": 54, "major": "Math"},
    {"name": "Carol", "grade": 78, "major": "CS"},
    {"name": "David", "grade": 63, "major": "Art"},
    {"name": "Eve", "grade": 45, "major": "Math"},
    {"name": "Frank", "grade": 88, "major": "CS"},
]


def get_passing_students(students):
    return [student for student in students if student["grade"] >= 60]


def get_average_grade(students):
    return sum(student["grade"] for student in students) / len(students) if students else 0


def count_by_major(students):
    counts = {}
    for student in students:
        major = student["major"]
        counts[major] = counts.get(major, 0) + 1
    return counts


def get_top_student(students):
    return max(students, key=lambda student: student["grade"]) if students else None


def filter_by_major(students, major):
    return [student for student in students if student["major"] == major]


def main():
    print("--- Student Report ---")
    print(f"Total students: {len(students)}")
    print(f"Passing students: {len(get_passing_students(students))}")
    print(f"Average grade: {get_average_grade(students):.2f}")
    print(f"Students by major: {count_by_major(students)}")
    top = get_top_student(students)
    print(f"Top student: {top['name']} ({top['grade']})")
    print("\nCS students:")
    for student in filter_by_major(students, "CS"):
        print(f"  {student['name']} — {student['grade']}")


main()
