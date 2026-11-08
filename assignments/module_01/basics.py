def main():
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    gpa = float(input("What is your GPA? "))
    birth_year = 2026 - age

    print("--- Student Profile ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Approximate birth year: {birth_year}")
    print(f"GPA: {gpa:.2f}")

    if gpa >= 3.5:
        status = "Excellent"
    elif gpa >= 3.0:
        status = "Good"
    elif gpa >= 2.0:
        status = "Satisfactory"
    else:
        status = "Needs improvement"
    print(f"GPA status: {status}")


if __name__ == "__main__":
    main()
