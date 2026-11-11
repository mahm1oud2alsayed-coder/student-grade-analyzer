def analyze_grades(scores):
    if not scores:
        return None

    total_students = len(scores)
    average = sum(scores) / total_students
    highest = max(scores)
    lowest = min(scores)
    passed_count = sum(1 for s in scores if s >= 50)
    pass_rate = (passed_count / total_students) * 100

    return {
        "total": total_students,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "pass_rate": pass_rate,
    }


def main():
    scores = [85, 42, 90, 78, 61, 49, 95, 73]
    results = analyze_grades(scores)

    print("--- Student Grade Report ---")
    print(f"Total Students : {results['total']}")
    print(f"Average Score  : {results['average']:.2f}")
    print(f"Highest Score  : {results['highest']}")
    print(f"Lowest Score   : {results['lowest']}")
    print(f"Pass Rate      : {results['pass_rate']:.1f}%")


if __name__ == "__main__":
    main()