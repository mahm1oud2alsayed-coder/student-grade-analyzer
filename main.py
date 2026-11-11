def analyze_grades(student_records):
    if not student_records:
        return None

    total_students = len(student_records)
    scores = [record["score"] for record in student_records]
    
    average = sum(scores) / total_students
    top_student = max(student_records, key=lambda x: x["score"])
    lowest_student = min(student_records, key=lambda x: x["score"])
    
    passed_count = sum(1 for s in scores if s >= 50)
    pass_rate = (passed_count / total_students) * 100

    return {
        "total": total_students,
        "average": average,
        "top_student": top_student,
        "lowest_student": lowest_student,
        "pass_rate": pass_rate,
    }


def main():
    # Sample dataset mapping student names to scores
    student_records = [
        {"name": "Alice", "score": 85},
        {"name": "Bob", "score": 42},
        {"name": "Charlie", "score": 90},
        {"name": "David", "score": 78},
        {"name": "Emma", "score": 61},
        {"name": "Frank", "score": 49},
        {"name": "Grace", "score": 95},
        {"name": "Henry", "score": 73},
    ]

    results = analyze_grades(student_records)

    print("--- Student Grade Report ---")
    print(f"Total Students : {results['total']}")
    print(f"Average Score  : {results['average']:.2f}")
    print(f"Top Performer  : {results['top_student']['name']} ({results['top_student']['score']})")
    print(f"Lowest Score   : {results['lowest_student']['name']} ({results['lowest_student']['score']})")
    print(f"Pass Rate      : {results['pass_rate']:.1f}%")


if __name__ == "__main__":
    main()