def collect_scores():
    count = int(input("How many students? "))
    while not 1 <= count <= 50:
        count = int(input("Invalid. Enter a number between 1 and 50: "))

    scores = []
    for student in range(1, count + 1):
        score = int(input(f"Enter score for student {student} (0-100): "))
        if score == -1:
            print(f"Skipping student {student}")
            continue
        if score == 999:
            print("Early exit triggered.")
            break
        while not 0 <= score <= 100:
            score = int(input("Invalid score. Try again: "))
            if score == -1:
                print(f"Skipping student {student}")
                break
            if score == 999:
                print("Early exit triggered.")
                break
        else:
            scores.append(score)
            continue
        if score == 999:
            break
    return scores


def grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def main():
    scores = collect_scores()
    for student, score in enumerate(scores, 1):
        print(f"Student {student}: {score} → {grade(score)}")
    if scores:
        passed = sum(score >= 60 for score in scores)
        failed = len(scores) - passed
        print("--- Class Statistics ---")
        print(f"Highest: {max(scores)}")
        print(f"Lowest: {min(scores)}")
        print(f"Average: {sum(scores) / len(scores):.2f}")
        print(f"Passed: {passed} | Failed: {failed}")


if __name__ == "__main__":
    main()
